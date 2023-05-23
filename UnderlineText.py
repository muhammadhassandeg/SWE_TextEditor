from TextDecorator import TextDecorator

class UnderlineDecorator(TextDecorator):
    """ Concrete Decorator"""

    def render(self) -> str:
        return f"<u>{self.text_element.render()}</u>"
