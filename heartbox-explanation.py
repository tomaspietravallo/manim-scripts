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
                TexMobject(r'l', r'= {{1\over2}\times {1\over2}}\times \sqrt{a^{2} + a^{2}}'), #1
                TexMobject(r'l', r'= {1\over4}\times \sqrt{a^{2} + a^{2}}'), #2
                TexMobject(r'l', r'= {1\over4}\times \sqrt{2a^{2}}'), #3
                TexMobject(r'l', r'= {1\over4}\times \sqrt{2} \times a'), #4
                TexMobject(r'l', r'= {\sqrt{2} \times a \over 4}'), #5
                TexMobject(r'\text{Area}', r'= {\sqrt{2} \times a \over 4} \times {\sqrt{2} \times a \over 4}') #6
            ]
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

            self.play(FadeOut(square)) # Fade out square

            self.wait()

            for index, equation in enumerate(equations):
                equations[index] = equation.move_to(2.0*DOWN)
                equations[index][0].set_color(YELLOW)

            # 1/2 The line twice
            line_halve = Line((-0.7, 0, 0), (0.7, 0, 0), color=YELLOW)
            line_halve_twice = Line((-0.35, 0, 0), (0.35, 0, 0), color=YELLOW)
            self.play(ReplacementTransform(after_hypotenuse, equations[1]))
            self.wait(0.3)
            self.play(Transform(line, line_halve))
            self.wait(0.3)
            self.play(Transform(line, line_halve_twice))
            self.wait(0.5)
            #############
            
            reTitle('Despejamos la equacion...')

            # Nothing important part of the system
            for index, equation in enumerate(equations):
                if index <= 1:
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

            self.play(ApplyMethod(equations[5].move_to, 0*UP), FadeOut(line))
            duplicate = equations[5]
            self.add(duplicate_eq_5)
            self.wait()

            highlighter = SurroundingRectangle(equations[6], color=BLUE)
            self.play(ReplacementTransform(equations[5], equations[6]))
            self.wait(0.3)

            self.play(ShowCreationThenDestruction(highlighter))
            self.wait()

        draw()
        
        pass

# python3 -m manim manim-scripts/heartbox-explanation.py ExplanationPartOne -pl --media_dir "/Users/tomaspietravallo/Desktop/quarantine-stuff/manim-output"
