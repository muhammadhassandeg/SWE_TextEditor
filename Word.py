from TextElement import TextElement

class Word(TextElement):
    """ Leaf"""

    def __init__(self, text: str) -> None:
        self.text = text

    def render(self) -> str:
        return self.text



