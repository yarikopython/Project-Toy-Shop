from textual.app import App, ComposeResult
from textual.widgets import Button, Header


class ProjectToyShop(App):
    def on_button_pressed(self, event: Button.Pressed) -> None:

    def compose(self) -> ComposeResult:
        yield Button("Create toy", id="create_toy")
        yield Header()
