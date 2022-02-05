import math
import numpy as np
from render.render import Render

def get_projection(point, z, Z, scale, w, h):
    x = int(w/2 + (point[0]*z/(point[2] + Z))*scale)
    y = int(h/2 - (point[1]*z/(point[2] + Z))*scale)
    return [x, y]

def get_line(p1, p2, resolution):
    resolution = resolution.get()
    if p1[0] == p2[0] and p1[1] == p2[1]:
        yield p1
        
    elif p1[0] == p2[0]:
        dist = abs(p1[1]-p2[1])
        how_many = int(max(2, resolution/100*dist))
        for i in np.linspace(min(p1[1], p2[1]), max(p1[1], p2[1]), how_many, endpoint=True):
            yield [p1[0], int(i)]
            
    else:
        a = (p2[1]-p1[1])/(p2[0]-p1[0])
        b = p1[1] - a*p1[0]
        print(a, b)
        dist = math.dist(p1, p2)
        how_many = int(max(2, resolution/100*dist))
        for i in np.linspace(min(p1[0], p2[0]), max(p1[0], p2[0]), how_many, endpoint=True):
            yield [i, int(a*i+b)]

class RenderDotted(Render):
    def __init__(self, window, mesh, resolution):
        self.window = window
        self.mesh = mesh
        self.resolution = resolution
    
    def render(self):
        z = 2
        Z = 3
        scale = 100
        points = self.mesh.get_points()
        normals = self.mesh.get_normals()
        self.window.create_rectangle(0, 0, self.window.winfo_width(), self.window.winfo_height(), fill='black')
        
        for i in range(len(points)):
            print(points[i])
            a = get_projection(points[i, 0:3], z, Z, scale, self.window.winfo_width(), self.window.winfo_height())
            b = get_projection(points[i, 3:6], z, Z, scale, self.window.winfo_width(), self.window.winfo_height())
            c = get_projection(points[i, 6:9], z, Z, scale, self.window.winfo_width(), self.window.winfo_height())
            print(a, b, c)
            
            for projection in get_line(a, b, self.resolution):
                if projection[0] >= 0 and projection[1] >= 0 and projection[0] <= self.window.winfo_width() and projection[1] <= self.window.winfo_height():
                    self.window.create_oval(projection[0]-2, projection[1]-2, projection[0]+2, projection[1]+2, fill='white')
                    
            for projection in get_line(a, c, self.resolution):
                if projection[0] >= 0 and projection[1] >= 0 and projection[0] <= self.window.winfo_width() and projection[1] <= self.window.winfo_height():
                    self.window.create_oval(projection[0]-2, projection[1]-2, projection[0]+2, projection[1]+2, fill='white')
                    
            for projection in get_line(b, c,self.resolution):
                if projection[0] >= 0 and projection[1] >= 0 and projection[0] <= self.window.winfo_width() and projection[1] <= self.window.winfo_height():
                    self.window.create_oval(projection[0]-2, projection[1]-2, projection[0]+2, projection[1]+2, fill='white')
            
            
        