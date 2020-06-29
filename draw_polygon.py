# !/usr/bin/env python
import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))

from manimlib.imports import *
from colour import *

class DrawPolygon(Scene):
    def construct(self):
        Square =   [(0,1.4,0),   #P1
                    (1.4,0,0),    #P2
                    (0,-1.4,0),    #P3
                    (-1.4,0,0),    #P4
                    ]
        first_fold =    [(0,1.4,0),
                        (1.20,0.21,0),
                        (1.20,-0.21,0),
                        (0,-1.4,0),
                        (-1.20,-0.21,0),
                        (-1.20,0.21,0),
                        (0,1.4,0)
                        ]
        second_fold =    [(0,1.4,0),
                        (0.34, 1.2,0),
                        (0.34, -1.2,0),
                        (0,-1.4,0),
                        (-0.34, -1.2,0),
                        (-0.34, 1.2,0),
                        (0, 1.4,0)
                        ]

        poly_square = Polygon(*Square)
        poly_first_fold = Polygon(*first_fold)
        poly_second_fold = Polygon(*second_fold)
        self.play(ShowCreation(poly_square))
        self.wait()
        self.play(ReplacementTransform(poly_square, poly_first_fold))
        self.wait()
        self.play(ReplacementTransform(poly_first_fold, poly_second_fold))
        self.wait()

# python3 -m manim manim-scripts/draw_polygon.py DrawPolygon -pl --media_dir "/Users/tomaspietravallo/Desktop/quarantine-stuff/manim-output"
