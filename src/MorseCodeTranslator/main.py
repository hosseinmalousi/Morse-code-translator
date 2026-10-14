from textual import on,events
from textual.app import App,ComposeResult
from textual.containers import ScrollableContainer ,Horizontal
from textual.screen import Screen
from textual.binding import Binding
from textual.widgets import Static, Footer ,Button,Header ,Input

class TextMorsePage(Screen): 
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Hello World")
        yield Button("Translate","success")

class MorseCodeTranslator(App):
    CSS_PATH = "./style.css"
    SCREENS ={"textMorsePage":TextMorsePage}
    BINDINGS = [
        Binding(key="q",action="quit",description="Quit the app")
    ]
    
    def compose(self) -> ComposeResult:
        self.title = "MorseCode trasnlator"
        yield Header(show_clock=True)
        yield Footer()
        with ScrollableContainer():
            yield Static("Hello, World!")
            with Horizontal(id="buttons"):
                yield Button("Text",id="text",variant="primary")
                yield Button("Morse",id="morse",variant="warning")
                 
    
    @on(Button.Pressed,"#text")
    def show_text_morsePage(self):
        self.push_screen("textMorsePage")
        
    
def main():
    MorseCodeTranslator().run()

if __name__ == "__main__":
    main()