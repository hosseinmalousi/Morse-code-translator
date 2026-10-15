from textual import on,events ,getters
from textual.app import App,ComposeResult
from textual.screen import Screen
from textual.containers import ScrollableContainer ,Horizontal
from textual.binding import Binding
from textual.widgets import Static, Footer ,Button,Header ,Input





class MorseTextPage(Screen):
    def compose(self) -> ComposeResult:
        yield Static("Morse to text")

class TextMorsePage(Screen):
    #finishing this page
    
    
    staticMessage = getters.query_one("Static")
    
    #placing the user input to a func for translation 
     
    def compose(self) -> ComposeResult:
        #adding id name for button and input for better readablity 
        yield Input(placeholder="Hello World")
        #adding a event for saving user input in the the var like enter 
        yield Button("Translate","success")
        yield Static("hihih")
    
    @on(Input.Submitted)
    def on_submit(self,event:Input.Submitted):
        #here i must call teh func for translating to morse code 
        value = event.value
        self.staticMessage.update(value)
        

class MorseCodeTranslator(App):
    CSS_PATH = "./style.css"
    SCREENS ={"textMorsePage":TextMorsePage,"morseTextPage":MorseTextPage}
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
        
    @on(Button.Pressed,"#morse")
    def show_morse_textPage(self):
        self.push_screen("morseTextPage")
        
    
def main():
    MorseCodeTranslator().run()

if __name__ == "__main__":
    main()