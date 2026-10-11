
from textual.app import ComposeResult
from textual.widgets import Static, Button,Input,Placeholder

class TextMorsePage(Static): 
    def compose(self) -> ComposeResult:
        yield Input(placeholder="Hello World")
        yield Button("Translate","success")