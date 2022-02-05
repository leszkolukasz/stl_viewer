from abc import ABC, abstractmethod

class Render(ABC):
    @abstractmethod
    def __init__(self, window):
        pass
    
    @abstractmethod
    def render(self):
        pass