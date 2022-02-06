from abc import ABC, abstractmethod

class Render(ABC):
    @abstractmethod
    def __init__(self, window, mesh, resolution, zoom, move_x, move_y, rot_x, rot_y):
        pass
    
    @abstractmethod
    def render(self):
        pass