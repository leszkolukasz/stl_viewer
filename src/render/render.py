from abc import ABC, abstractmethod

class Render(ABC):
    @abstractmethod
    def __init__(self, window, mesh):
        pass
    
    @abstractmethod
    def render(self):
        pass