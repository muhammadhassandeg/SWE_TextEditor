from TextDecorator import TextDecorator


class ItalicDecorator(TextDecorator):
    """ Concrete Decorator"""

    def render(self) -> str:
        return f"<i>{self.text_element.render()}</i>"
