# !/usr/bin/env python
import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))

from manimlib.imports import *
from colour import *

class Shapes(Scene):
    def construct(self):
        def draw():
            square = Square()
            line = Line((-1,-1,0), (1,1,0), color=YELLOW)
            self.play(ShowCreation(square))
            self.wait(0.3)
            self.play(ShowCreation(line))
            self.wait(0.3)
            self.play(Rotate(square, angle= -45*DEGREES), Rotate(line, angle= -45*DEGREES))
            self.wait()
            self.play(Transform(square, line))
            self.wait()
        draw()
        
        pass

# python3 -m manim manim-scripts/shapes.py Shapes -pl --media_dir "/Users/tomaspietravallo/Desktop/quarantine-stuff/manim-output"
