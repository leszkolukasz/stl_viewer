from abc import ABC, abstractmethod

class Render(ABC):
    @abstractmethod
    def __init__(self, window, mesh, resolution):
        pass
    
    @abstractmethod
    def render(self):
        pass