"""Implements dotted renderer"""

import math
import numpy as np

from render.render import Render

class RenderDotted(Render):
    def __init__(self, window, mesh, config):
        self.window = window
        self.mesh = mesh
        self.config = config
    
    def render(self):
        points = self.mesh.get_points(
            self.config['rotation_offset'][0], self.config['rotation_offset'][1]
        )
        self.config['rotation_offset'][0] = 0
        self.config['rotation_offset'][1] = 0
        normals = self.mesh.get_normals()
        self.window.create_rectangle(0, 0, self.window.winfo_width(), self.window.winfo_height(), fill='black')
        
        for i in range(len(points)):
            a = self.get_projection(points[i, 0:3], self.window.winfo_width(), self.window.winfo_height())
            b = self.get_projection(points[i, 3:6], self.window.winfo_width(), self.window.winfo_height())
            c = self.get_projection(points[i, 6:9], self.window.winfo_width(), self.window.winfo_height())
            normal = np.array(normals[i]) @ (np.array([0, 1, -1])/1.4142135623730951)
            
            if normal < 0:
                continue
            
            normal = int(normal*255)
            
            for (p1, p2) in zip([a, a, b], [b, c, c]):
                for projection in self.get_line(p1, p2):
                    if (projection[0] >= 0 and
                        projection[1] >= 0 and
                        projection[0] <= self.window.winfo_width() and
                        projection[1] <= self.window.winfo_height()
                    ):
                        self.window.create_oval(
                            projection[0]-2,
                            projection[1]-2,
                            projection[0]+2,
                            projection[1]+2,
                            fill=self.rgb_to_hex((normal, normal, normal))
                        )
        