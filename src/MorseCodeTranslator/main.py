from textual import on,events ,getters
from textual.app import App,ComposeResult
from textual.screen import Screen
from textual.containers import ScrollableContainer ,Horizontal
from textual.binding import Binding
from textual.widgets import Static, Footer ,Button,Header ,Input
import string

# STR_UNDERCASE=string.ascii_lowercase
MORSECODE_DIC = {"a":".-","b":"-...","c":"-.-.","d":"-..","e":".",
                "f":"..-.","g":"--.","h":"....","i":"..","j":".---",
                "k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.",
                "q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--",
                "x":"-..-","y":"-.--","z":"--.."}


class MorseTextPage(Screen):
    def compose(self) -> ComposeResult:
        yield Input(placeholder="what is ur code")

class TextMorsePage(Screen):
    userText : str =getters.query_one("#textInput")
    staticMessage : str = getters.query_one("#translated")
     
    def compose(self) -> ComposeResult:
        #adding id name for button and input for better readablity 
        with Horizontal(id="text_container"):
            yield Input(placeholder="Hello World",valid_empty=False,classes="inputs",id="textInput") 
            yield Button("Translate","success",id="translateBtn")
            yield Button("Home","default",id="homeBtn")
        yield Static("It translate to ...",id="translated")
    
    def translateTextToMorse(self,text) -> list[str]:
        translated : list[str]=[]
        for char in text:
            if char == " ":
                translated.append("/")
                continue
            elif char not in string.ascii_lowercase:
                self.notify(f"the {char} is not valid",severity="error")
                translated.append("#")
                break
            translated.append(MORSECODE_DIC[char])
        return translated
    
    @on(Button.Pressed,"#translateBtn")
    def on_translate(self) -> None:
        value = self.userText.value.lower()
        translated = self.translateTextToMorse(value)
        self.staticMessage.update(" ".join(translated))
    
    @on(Input.Submitted)
    def on_submit(self,event:Input.Submitted) -> None: 
        # value = event.value.lower()
        # translated = self.translateTextToMorse(value)
        # self.staticMessage.update(" ".join(translated))
        self.on_translate()
        

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
    
    @on(Button.Pressed,"#homeBtn")
    def on_homeBtn(self,):
        self.pop_screen()
        
    @on(Button.Pressed,"#morse")
    def show_morse_textPage(self):
        self.push_screen("morseTextPage")
        
    
def main():
    MorseCodeTranslator().run()

if __name__ == "__main__":
    main()