from TextElement import TextElement

class TextEditor:
    """ Client"""

    def __init__(self, text: TextElement) -> None:
        self.text = text

    def render(self) -> str:
        return self.text.render()