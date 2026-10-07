from textual.app import App,ComposeResult
from textual.binding import Binding
from textual.widgets import Label, Footer ,Button

class MorseCodeTranslator(App):
    CSS_PATH = "./style.css"
    
    BINDINGS = [
        Binding(key="q",action="quit",description="Quit the app")
    ]
    
    def compose(self) -> ComposeResult:
        yield Label("Hello, World!")
        yield Button("Text")
        yield Button("Morse")
        yield Footer()

def main():
    MorseCodeTranslator().run()

if __name__ == "__main__":
    main()