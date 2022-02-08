"""Implements class that operates on vectors stored in stl file"""

import numpy as np
import stl

class Mesh():
    def __init__(self, path=None):
        self.mesh = None
        self.points = None
        if path is not None:
            self.load_file(path)
        
    def load_file(self, path):
        self.mesh = stl.mesh.Mesh.from_file(path)
        
    def is_loaded(self):
        return self.mesh is not None
        
    def get_points(self, rotate_x, rotate_y):
        if rotate_x != 0:
            self.mesh.rotate([0, 1, 0], rotate_x/100)
        if rotate_y != 0:
            self.mesh.rotate([1, 0, 0], rotate_y/100)

        return self.mesh.points
    
    def get_normals(self):
        return self.mesh.get_unit_normals()