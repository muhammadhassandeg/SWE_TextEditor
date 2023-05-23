from TextElement import TextElement
from typing import List
from Word import Word

class Sentence(TextElement):
    """ Composite """

    def __init__(self, words: List[Word]) -> None:
        self.words = words

    def render(self) -> str:
        return " ".join([word.render() for word in self.words])





