# !/usr/bin/env python
import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))

from manimlib.imports import *
from colour import *

class ExplanationPartOne(Scene):
    def construct(self):

        def draw():
            title = TextMobject("Equaciones Problema N°4").move_to(2*UP)
            self.play(Write(title, run_time=2.0))
            self.wait(0.5)

            def reTitle(newTitle = ''):
                _newTitle = TextMobject(f'{newTitle}').move_to(2*UP)
                self.play(Transform(title, _newTitle))
                self.wait(0.3)

            equations = [
                TexMobject(r'l', r'= \sqrt{a^{2} + a^{2}}'), #0
                TexMobject(r'l', r'= {3\over4}\times \sqrt{a^{2} + a^{2}}'), #1
                TexMobject(r'l', r'= {1\over4}\times \sqrt{a^{2} + a^{2}}'), #2
                TexMobject(r'l', r'= {1\over4}\times \sqrt{2a^{2}}'), #3
                TexMobject(r'l', r'= {1\over4}\times \sqrt{2} \times a'), #4
                TexMobject(r'l', r'= {\sqrt{2} \times a \over 4}'), #5
            ]
            first_fold =[(0,1.4,0),
                        (1.06,0.21,0),
                        (1.06,-0.21,0),
                        (0,-1.4,0),
                        (-1.06,-0.21,0),
                        (-1.06,0.21,0),
                        (0,1.4,0)
                        ]
            second_fold =[(0,1.4,0),
                        (0.34, 1.2,0),
                        (0.34, -1.2,0),
                        (0,-1.4,0),
                        (-0.34, -1.2,0),
                        (-0.34, 1.2,0),
                        (0, 1.4,0)
                        ]

            poly_first_fold = Polygon(*first_fold)
            poly_second_fold = Polygon(*second_fold)
            duplicate_eq_5 = TexMobject(r'l', r'= {\sqrt{2} \times a \over 4}')
            duplicate_eq_5[0].set_color(YELLOW)
            square = Square()
            line = Line((-1,-1,0), (1,1,0), color=YELLOW)
            label_y = TexMobject("a").next_to(square, LEFT)
            label_x = TexMobject("a").next_to(square, DOWN)
            text_x = TexMobject(r"\times")
            after_hypotenuse = TexMobject(r'l', r'= \sqrt{a^{2} + a^{2}}')
            after_hypotenuse[0].set_color(YELLOW)

            after_hypotenuse.move_to(2.0*DOWN)
            text_x.move_to(2.0*DOWN)

            self.play(ShowCreation(square)) # Show square

            reTitle('Definimos el problema')

            self.play(Write(label_x), Write(label_y)) # Show labels

            self.wait(0.3)

            self.play( # Move labels  & write LateX '\times'
                Write(text_x),
                ApplyMethod(label_y.next_to, text_x, LEFT),
                ApplyMethod(label_x.next_to, text_x, RIGHT),
            )

            self.wait(0.3)

            self.play(
                ShowCreation(line), 
                FadeOut(label_y), 
                FadeOut(label_x), 
                ReplacementTransform(text_x, after_hypotenuse)) # Show hypotenuse and transfrom labels/eq

            reTitle('Calculamos la diagonal / hipotenusa')

            self.play( # Rotate square and line
                Rotate(square, angle= -45*DEGREES),
                Rotate(line, angle= -45*DEGREES),
            )

            # self.play(FadeOut(square)) # Fade out square

            self.wait()

            for index, equation in enumerate(equations):
                equations[index] = equation.move_to(2.0*DOWN)
                equations[index][0].set_color(YELLOW)

            # 1/2 The line twice
            line_three_fourths = Line((-1.06, 0, 0), (1.06, 0, 0), color=YELLOW)
            line_one_fourth = Line((-0.35, 0, 0), (0.35, 0, 0), color=YELLOW)
            self.play(ReplacementTransform(after_hypotenuse, equations[1]))
            self.play(Transform(line, line_three_fourths), ReplacementTransform(square, poly_first_fold))
            self.wait(0.6)
            self.play(Transform(line, line_one_fourth), ReplacementTransform(poly_first_fold, poly_second_fold), ReplacementTransform(equations[1], equations[2]))
            self.wait(0.5)
            #############
            
            reTitle('Despejamos la equacion...')

            # Nothing important part of the system
            for index, equation in enumerate(equations):
                if index <= 2:
                    pass
                elif index < 5:
                    self.play(ReplacementTransform(equations[index - 1], equation))
                    self.wait(0.4)
            ##################
            reTitle('Y llegamos al resultado')
            # Write last equation and move stuff around
            highlighter = SurroundingRectangle(equations[5], color=BLUE)
            self.play(ReplacementTransform(equations[4], equations[5]))
            self.play(ShowCreationThenDestruction(highlighter))
            self.wait(0.3)

            # This end sequence is MESSY, it has errors, it wasn't used
            final_square = Square(color=BLUE).scale(0.35355)
            self.play(ReplacementTransform(poly_second_fold, final_square), ApplyMethod(line.next_to, args=[final_square, DOWN], buff=0))
            # duplicate = equations[5]
            # self.add(duplicate_eq_5)
            self.wait()

        draw()
        
        pass

class Intro(Scene):
    def construct(self):
        title = TextMobject("Problema N°4 - Caja Corazon")
        subTitle = TextMobject("Constanza Etchebere y Tomas Pietravallo")\
            .to_edge(DOWN)\
            .scale(0.45)
        self.play(Write(title, run_time=2.0), Write(subTitle, run_time=3))
        self.wait(0.3)
        self.play(FadeOut(title), FadeOut(subTitle))

class ShowSquare(Scene):
    def construct(self):
        square = Square()
        line = Line((-1,-1,0), (1,1,0), color=YELLOW)
        label_y = TexMobject("a").next_to(square, LEFT)
        label_x = TexMobject("a").next_to(square, DOWN)
        text_x = TexMobject(r"\times")
        text_x.move_to(2.0*DOWN)
        after_hypotenuse = TexMobject(r'l', r'= \sqrt{a^{2} + a^{2}}')
        after_hypotenuse[0].set_color(YELLOW)
        after_hypotenuse.move_to(2.0*DOWN)

        title = TextMobject('Definimos el problema').move_to(2*UP)
        self.play(Write(title)) # Title

        self.play(ShowCreation(square)) # Square

        self.play(Write(label_x), Write(label_y)) # Show labels

        self.wait(0.3)

        self.play( # Move labels  & write LateX '\times'
            Write(text_x),
            ApplyMethod(label_y.next_to, text_x, LEFT),
            ApplyMethod(label_x.next_to, text_x, RIGHT),
        )

        self.wait(0.3)

        title_reference = TextMobject("Tomamos como referencia la hipotenusa").move_to(2*UP)

        self.play( # Show hypotenuse and transfrom labels/eq
            ShowCreation(line), 
            FadeOut(label_y), 
            FadeOut(label_x), 
            ReplacementTransform(text_x, after_hypotenuse),
            ReplacementTransform(title, title_reference)
        )

        self.wait(0.5)

        self.play( # Rotate square and line
            Rotate(square, angle= -45*DEGREES),
            Rotate(line, angle= -45*DEGREES),
        )
        
        self.wait()

class LineTransform(Scene):
    def construct(self):
        title_reference = TextMobject("Tomamos como referencia la hipotenusa").move_to(2*UP)
        square = Square().rotate(-45*DEGREES)
        line = Line((-1,-1,0), (1,1,0), color=YELLOW).rotate(-45*DEGREES)
        after_hypotenuse = TexMobject(r'l', r'= \sqrt{a^{2} + a^{2}}')
        after_hypotenuse[0].set_color(YELLOW)
        after_hypotenuse.move_to(2.0*DOWN)

        self.add( # Match previous scene
            title_reference,
            square,
            line,
            after_hypotenuse,
        )

        self.wait(0.3)

        self.play(FadeOut(square)) # Remove square

        self.wait(0.3)

        equations_one = TexMobject(r'l', r'= {3\over4}\times \sqrt{a^{2} + a^{2}}').move_to(2*DOWN) #1
        equations_one[0].set_color(YELLOW)
        equations_two = TexMobject(r'l', r'= {1\over4}\times \sqrt{a^{2} + a^{2}}').move_to(2*DOWN) #2
        equations_two[0].set_color(YELLOW)
        title_process = TextMobject("Expresamos matematicamente lo visto armando la caja").move_to(2*UP)
        line_three_fourths = Line((-1.06, 0, 0), (1.06, 0, 0), color=YELLOW)
        line_one_fourth = Line((-0.35, 0, 0), (0.35, 0, 0), color=YELLOW)

        self.play(ReplacementTransform(title_reference, title_process))
        self.wait(0.5)
        self.play(ReplacementTransform(after_hypotenuse, equations_one), ReplacementTransform(line, line_three_fourths))
        
        self.wait(0.7)

        self.play(ReplacementTransform(equations_one, equations_two), ReplacementTransform(line_three_fourths, line_one_fourth))
        
        self.wait()

class Rearrange(Scene):
    def construct(self):
        line_one_fourth = Line((-0.35, 0, 0), (0.35, 0, 0), color=YELLOW)
        title_process = TextMobject("Expresamos matematicamente lo visto armando la caja").move_to(2*UP)
        title_rearrage = TextMobject("Despejamos la ecuacion").move_to(2*UP)

        equations = [
            TexMobject(r'l', r'= {1\over4}\times \sqrt{a^{2} + a^{2}}'), #0
            TexMobject(r'l', r'= {1\over4}\times \sqrt{2a^{2}}'), #1
            TexMobject(r'l', r'= {1\over4}\times \sqrt{2} \times a'), #2
            TexMobject(r'l', r'= {\sqrt{2} \times a \over 4}'), #3
        ]

        for index, equation in enumerate(equations):
            equations[index] = equation.move_to(2.0*DOWN)
            equations[index][0].set_color(YELLOW)

        self.add(line_one_fourth, title_process, equations[0])

        self.play(ReplacementTransform(title_process, title_rearrage))

        self.wait(0.5)

        self.play(ReplacementTransform(equations[0], equations[1]))
        self.wait(0.75)
        self.play(ReplacementTransform(equations[1], equations[2]))
        self.wait(0.75)
        self.play(ReplacementTransform(equations[2], equations[3]))
        self.wait()

class ResultPartOne(Scene):
    def construct(self):
        result = TexMobject(r'l', r'= {\sqrt{2} \times a \over 4}').move_to(2*DOWN)
        line_one_fourth = Line((-0.35, 0, 0), (0.35, 0, 0), color=YELLOW)
        title_rearrage = TextMobject("Despejamos la ecuacion").move_to(2*UP)
        title_result = TextMobject("¡¡Y llegamos al resultado!!").move_to(UP*1.5)

        self.add(result, line_one_fourth)
        self.play(FadeOut(line_one_fourth), ReplacementTransform(title_rearrage, title_result, run_time=0.75), ApplyMethod(result.move_to, 0*DOWN))

        highlighter = SurroundingRectangle(result, color=BLUE)
        self.play(ShowCreationThenDestruction(highlighter, run_time=1))
        self.wait()
        
