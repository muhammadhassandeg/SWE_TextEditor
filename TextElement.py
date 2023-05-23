from abc import ABC, abstractmethod

class TextElement(ABC):
    """ Component """
    @abstractmethod
    def render(self) -> str:
        pass


