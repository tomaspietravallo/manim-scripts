# !/usr/bin/env python
import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))

from manimlib.imports import *
from colour import *

class WriteText(Scene): 
    def construct(self): 
        equations = [
            TexMobject(r'l = a \times a'),
            TexMobject(r'l = \sqrt{a^{2} + a^{2}}'),
            TexMobject(r'l = {{1\over2}\times {1\over2}}\times \sqrt{a^{2} + a^{2}}'),
            TexMobject(r'l = {1\over4}\times \sqrt{a^{2} + a^{2}}'),
            TexMobject(r'l = {1\over4}\times \sqrt{2a^{2}}'),
            TexMobject(r'l = {1\over4}\times \sqrt{2} \times a'),
            TexMobject(r'l = {\sqrt{2} \times a \over 4}'),
            TexMobject(r'\text{Area} = {\sqrt{2} \times a \over 4} \times {\sqrt{2} \times a \over 4}')
        ]
        title = TextMobject("Equaciones Problema N°4").move_to(2*UP)
        self.play(Write(title, run_time=1.5))

        for index, equation in enumerate(equations):
            if index == 0:
                self.play(Write(equation, run_time=0.8))
            elif index <= 5:
                self.play(ReplacementTransform(equations[index - 1], equation))
            else:
                eq = equations[index - 1]
                self.play(ApplyMethod(eq.move_to, 1.5*UP), 
                ApplyMethod(title.move_to, 2.5*UP),
                Write(equation))
                highlighter = SurroundingRectangle(eq, stroke_color=BLUE)
                self.play(FadeIn(highlighter))
                self.wait(0.5)
                self.play(FadeOut(highlighter))
                self.wait(0.2)
                highlighter2 = SurroundingRectangle(equation, stroke_color=BLUE)
                self.play(FadeIn(highlighter2))
                self.wait(1)
                self.play(FadeOut(highlighter2))
            self.wait(0.5)



# python3 -m manim manim-scripts/heartbox-explanation.py WriteText -pl --media_dir "/Users/tomaspietravallo/Desktop/quarantine-stuff/manim-output"

# python3 -m manim example_scenes.py SquareToCircle -pl --media_dir "/Users/tomaspietravallo/Desktop/quarantine-stuff/manim-output"