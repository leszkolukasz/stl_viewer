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
        
    def get_points(self, x, y):      
        """self.points = np.zeros((3*len(self.mesh.points), 3))
        for i in range(len(self.mesh.points)):
            self.points[i, 0] = np.sum(self.mesh.points[i, ::3])
            self.points[i, 1] = np.sum(self.mesh.points[i, 1::3])
            self.points[i, 2] = np.sum(self.mesh.points[i, 2::3])
            self.points[i] /= 3
            self.points[3*i] = self.mesh.points[i, 0:3]
            self.points[3*i+1] = self.mesh.points[i, 3:6]
            self.points[3*i+2] = self.mesh.points[i, 6:9]"""
        if x != 0:
            self.mesh.rotate([0, 1, 0], -x/100)
        if y != 0:
            self.mesh.rotate([1, 0, 0], -y/100)

        return self.mesh.points
    
    def get_normals(self):
        return self.mesh.get_unit_normals()