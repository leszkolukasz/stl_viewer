import math
import numpy as np
from abc import ABC, abstractmethod

class Render(ABC):
    @abstractmethod
    def __init__(self, window, mesh, config):
        pass
    
    @abstractmethod
    def render(self):
        pass
    
    def rgb_to_hex(self, rgb):
        return "#%02x%02x%02x" % rgb 

    def get_projection(self, point, width, height, scale=1):
        x = int((width/2 + scale*((point[0])*self.config['fov']*self.config['zoom']/(point[2] + self.config['distance'])) + self.config['move_offset'][0]))
        y = int(height/2 - ((point[1])*self.config['fov']*self.config['zoom']/(point[2] + self.config['distance'])) + self.config['move_offset'][1])
        return (x, y)

    def get_line(self, p1, p2, full=False):
        scale = 1 if full else self.config['resolution'].get()/100
        if p1[0] == p2[0] and p1[1] == p2[1]:
            yield p1
            
        elif p1[0] == p2[0]:
            dist = abs(p1[1]-p2[1])
            density = int(max(2, scale*dist))
            for i in np.linspace(min(p1[1], p2[1]), max(p1[1], p2[1]), density, endpoint=True):
                yield [p1[0], int(i)]
                
        else:
            a = (p2[1]-p1[1])/(p2[0]-p1[0])
            b = p1[1] - a*p1[0]
            dist = math.dist(p1, p2)
            density = int(max(2, scale*dist))
            for i in np.linspace(min(p1[0], p2[0]), max(p1[0], p2[0]), density, endpoint=True):
                yield [i, int(a*i+b)]