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
        subTitle = TextMobject("Constanza Etchebehere y Tomas Pietravallo")\
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

class ResultPartOne(Scene): # This scene ended up being really long, it was faster but it seems like a bit of a mess
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

class IntroPartTwo(Scene):
    def construct(self):
        result = TexMobject(r'l', r'= {\sqrt{2} \times a \over 4}').move_to(0*UP)
        title_result = TextMobject("¡¡Y llegamos al resultado!!").move_to(UP*1.5)
        title_question = TextMobject(r"Y si quisieramos sacar el tamaño del papel para\\caja determinada?")
        title_response = TextMobject(r"Partiremos de la igualdad obtenida anteriormente")
        title_rearrange = TextMobject(r"Despejamos para (a)").move_to(2*UP)
        subtitle = TextMobject(r"a", r" = lados de la hoja necesaria")\
            .scale(0.5) \
            .next_to(title_rearrange, DOWN)
        subtitle[0].set_color(YELLOW)
        self.add(result, title_result)
        self.play(ApplyMethod(result.move_to, 2*DOWN), ApplyMethod(title_result.move_to, 0*UP), ReplacementTransform(title_result, title_question))

        self.wait(2)

        highlighter = SurroundingRectangle(result, color=BLUE)

        self.play(ReplacementTransform(title_question, title_response))
        self.play(ShowCreationThenDestruction(highlighter, run_time=0.75))

        self.wait(2.5)
        recolor = TexMobject(r'l = {\sqrt{2} \times', r'a', r'\over 4}')
        recolor[0].set_color(WHITE)
        recolor[1].set_color(YELLOW)
        self.play(ApplyMethod(result.move_to, 0*UP), ReplacementTransform(title_response, title_rearrange), ReplacementTransform(result, recolor), FadeIn(subtitle))
        self.wait(2)

        first_step = TexMobject(r'4l = {\sqrt{2} \times', r' a}')
        first_step[1].set_color(YELLOW)
        self.play(ReplacementTransform(recolor, first_step))

        equation_pre_rationalize = TexMobject(r'{4l\over{\sqrt{2}}} = ', r'{a}')
        equation_pre_rationalize[1].set_color(YELLOW)

        self.wait()
        self.play(ReplacementTransform(first_step, equation_pre_rationalize))

        self.wait(0.5)

        title_rationalize = TextMobject(r"Realizamos la racionalizacion").move_to(2*UP)
        self.play(ReplacementTransform(title_rearrange, title_rationalize))
        self.wait(0.5)

        equation_rationalize_first_step = TexMobject(r'{4l\over{\sqrt{2}}} \times {\sqrt{2}\over\sqrt{2}} = ', r"{a}")
        equation_rationalize_first_step[1].set_color(YELLOW)
        self.play(ReplacementTransform(equation_pre_rationalize, equation_rationalize_first_step))
        self.wait(0.5)

        equation_rationalized = TexMobject(r'{4l\times{\sqrt{2}}\over 2} = ', r'{a}')
        equation_rationalized[1].set_color(YELLOW)
        self.play(ReplacementTransform(equation_rationalize_first_step, equation_rationalized))
        self.wait()

        title_simplify = TextMobject(r"Simplificamos 4l con el denominador").move_to(2*UP)
        self.play(ReplacementTransform(title_rationalize, title_simplify))
        self.wait()

        last_equation = TexMobject(r'{2l\times{\sqrt{2}}} = ', r'{a}')
        last_equation[1].set_color(YELLOW)

        highlighter = SurroundingRectangle(result, color=BLUE)

        self.play(ReplacementTransform(equation_rationalized, last_equation))
        title_end = TextMobject(r"¡¡Y llegamos al resultado!!").move_to(1.5*UP)

        self.play(ReplacementTransform(title_simplify, title_end), FadeOut(subtitle))
        self.play(ShowCreationThenDestruction(highlighter, run_time=0.75))

        self.wait(2)
        self.play(FadeOutAndShiftDown(last_equation), FadeOutAndShiftDown(title_end))

        endcard = TextMobject(r"Realizado por alumnos del PAN (2020)") \
            .move_to(1*UP)\
            .scale(1.08)
        endcard_students = TextMobject(r"Constanza Etchebehere y Tomas Pietravallo") \
            .scale(1) \
            .next_to(endcard, DOWN)
        endcard_subject = TextMobject(r"Matematica - Profesor Mauricio Sentenac") \
            .scale(1.011) \
            .next_to(endcard_students, DOWN)
        endcard_github = TextMobject(r"Realizado con Manim - Codigo Abierto bajo Licencia MIT\\github/tomaspietravallo/manim-scripts/heartbox-explanation.py") \
            .scale(0.3) \
            .to_edge(DOWN)

        self.play(FadeInFrom(endcard, DOWN))
        self.play(FadeInFrom(endcard_students, DOWN))
        self.play(FadeInFrom(endcard_subject, DOWN))
        self.play(FadeInFrom(endcard_github, DOWN))

        self.wait(3)

        self.play(FadeOut(endcard), FadeOut(endcard_students), FadeOut(endcard_subject), FadeOut(endcard_github))

