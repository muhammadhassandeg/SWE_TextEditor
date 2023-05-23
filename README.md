# SWE_TextEditor
Project for software engineering subject

Project is an implementation of the Composite and Decorator Design Patterns to create a text editor application. The application allows users to compose and format text documents using a hierarchical structure of text elements and various formatting options.

The Composite Design Pattern is used to represent the hierarchical structure of text elements, which include Word, Sentence, and Paragraph classes. The Word class represents a leaf node in the hierarchy, while the Sentence and Paragraph classes represent composite nodes. The Sentence class contains a list of Word objects, while the Paragraph class contains a list of Sentence objects.

The Decorator Design Pattern is used to add various formatting options to the text. The TextDecorator class is an abstract class that wraps around a TextElement object and adds a formatting option to it. The BoldDecorator, ItalicDecorator, and UnderlineDecorator classes are concrete decorator classes that inherit from the TextDecorator class and add bold, italic, and underline formatting options to the text, respectively.

The TextEditor class is the client class that takes a TextElement object as input and has a render method that returns the text representation of the input TextElement. The render method is used to render the text document with the formatting options added by the decorator classes.

In the following example , we create instances of Word, Sentence, and Paragraph objects and pass them to a TextEditor object. We also create instances of decorator classes and wrap them around text elements to add formatting options. The TextEditor object is then used to render the text document with the formatting options added by the decorator classes.
```
word1 = Word("Hello")
word2 = Word("world")
sentence1 = Sentence([word1, word2])

paragraph1 = Paragraph([sentence1])
bold_sentence = BoldDecorator(sentence1)
italic_paragraph = ItalicDecorator(paragraph1)
underline_text = UnderlineDecorator(bold_sentence)
text_editor = TextEditor(underline_text)

print(text_editor.render())
```
```
>>> <u><b>Hello world</b></u>
```
