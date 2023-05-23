from typing import List
from TextElement import TextElement
from Sentence import Sentence

class Paragraph(TextElement):
    """ Composite"""

    def __init__(self, sentences: List[Sentence]) -> None:
        self.sentences = sentences

    def render(self) -> str:
        return "\n".join([sentence.render() for sentence in self.sentences])


