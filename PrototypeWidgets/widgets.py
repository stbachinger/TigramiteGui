# this includes all the widgets needed for the notebook
import ipywidgets as widgets
from ipywidgets import DOMWidget, register


class MethodWidget:
    def __init__(self):
        self

    def get_widget(self):
        return widgets.Dropdown(
            options=["PCMCI", "PCMCI+"],
            value="PCMCI",
            description="Method:",
            disabled=False
        )

