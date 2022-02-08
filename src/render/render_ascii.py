"""Implements ASCII renderer"""

import math
import numpy as np

from render.render import Render

class RenderAscii(Render):
    def __init__(self, window, mesh, render_frame, config):
        self.window = window
        self.mesh = mesh
        self.render_frame = render_frame
        self.config = config
    
    def render(self):
        self.config['zoom'] /= 20
        self.font_size = self.config['resolution'].get()
        self.output = np.full((int(1.5*self.window.winfo_width()/self.font_size), int(self.window.winfo_height()//self.font_size)), 32)
        
        points = self.mesh.get_points(
            self.config['rotation_offset'][0], self.config['rotation_offset'][1]
        )
        self.config['rotation_offset'][0] = 0
        self.config['rotation_offset'][1] = 0
        normals = self.mesh.get_normals()
        self.window.create_rectangle(0, 0, self.window.winfo_width(), self.window.winfo_height(), fill='black')
        
        for i in range(len(points)):
            a = self.get_projection(points[i, 0:3], self.output.shape[0], self.output.shape[1], 1.93)
            b = self.get_projection(points[i, 3:6], self.output.shape[0], self.output.shape[1], 1.93)
            c = self.get_projection(points[i, 6:9], self.output.shape[0], self.output.shape[1], 1.93)
            normal = np.array(normals[i]) @ (np.array([0, 1, -1])/1.4142135623730951)
            
            if normal < 0:
                continue
            
            normal = int(normal*12)
            
            for (p1, p2) in zip([a, a, b], [b, c, c]):
                for projection in self.get_line(p1, p2, True):
                    if (projection[0] >= 0 and
                        projection[1] >= 0 and
                        projection[0] < self.output.shape[0] and
                        projection[1] < self.output.shape[1]
                    ):
                        self.output[int(projection[0]), int(projection[1])] = ord((list(".,-~:;=!*#$@"))[min(normal, 11)])
                        
        txt = ""
        for i in range(self.output.shape[1]):
            for j in range(self.output.shape[0]):
                txt += chr(self.output[j, i])
            txt += '\n'
        print(self.output.shape)
        self.window.create_text(int(self.window.winfo_width()/2), int(self.window.winfo_height()/2), text=txt, font=('Courier', self.font_size), fill='white')
        self.config['zoom'] *= 20
        