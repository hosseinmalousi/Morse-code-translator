from textual.app import App,ComposeResult
from textual.widgets import Label

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Label("Hello, World!")
        yield Label("hello, to u")

def main():
    MyApp().run()

if __name__ == "__main__":
    main()