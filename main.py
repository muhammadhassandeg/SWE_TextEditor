from TextEditor import TextEditor
from Word import Word
from Sentence import Sentence
from Paragraph import Paragraph
from BoldText import BoldDecorator
from ItalicText import ItalicDecorator
from UnderlineText import  UnderlineDecorator


word1 = Word("Hello")
word2 = Word("world")
sentence1 = Sentence([word1, word2])

paragraph1 = Paragraph([sentence1])
bold_sentence = BoldDecorator(sentence1)
italic_paragraph = ItalicDecorator(paragraph1)
underline_text = UnderlineDecorator(bold_sentence)
text_editor = TextEditor(underline_text)

print(text_editor.render())



