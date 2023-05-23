from TextElement import TextElement
from abc import ABC, abstractmethod

class TextDecorator(TextElement):
    """ Decorator"""

    def __init__(self, text_element: TextElement) -> None:
        self.text_element = text_element

    @abstractmethod
    def render(self) -> str:
        pass

