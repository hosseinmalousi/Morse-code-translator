from textual.app import App,ComposeResult
from textual.containers import ScrollableContainer ,Horizontal
from textual.binding import Binding
from textual.widgets import Static, Footer ,Button,Header
from home import Home
from text_morse import TextMorsePage
class MorseCodeTranslator(App):
    CSS_PATH = "./style.css"
    
    BINDINGS = [
        Binding(key="q",action="quit",description="Quit the app")
    ]
    
    def compose(self) -> ComposeResult:
        self.title = "MorseCode trasnlator"
        yield Header(show_clock=True)
        yield Footer()
        yield Home()
        yield TextMorsePage()
        

def main():
    MorseCodeTranslator().run()

if __name__ == "__main__":
    main()