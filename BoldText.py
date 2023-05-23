from TextDecorator import TextDecorator

class BoldDecorator(TextDecorator):
    """ Concrete Decorator"""

    def render(self) -> str:
        return f"<b>{self.text_element.render()}</b>"


