from textual import events, on
from textual.app import ComposeResult
from textual.containers import ScrollableContainer ,Horizontal
from textual.binding import Binding
from textual.widgets import Static,Button
from text_morse import TextMorsePage
class Home(Static):
    
    @on(Button.Pressed,"#text")
    def show_text_morsePage(self):
        self.styles.display = "none"
        TextMorsePage().styles.display = "block"
    
    def compose(self) -> ComposeResult:
        with ScrollableContainer():
            yield Static("Hello, World!")
            with Horizontal(id="buttons"):
                yield Button("Text",id="text",variant="primary")
                yield Button("Morse",id="morse",variant="warning")