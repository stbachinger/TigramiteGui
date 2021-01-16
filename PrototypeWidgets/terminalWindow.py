import ipywidgets as widgets
from ipywidgets import Widget


class TerminalOutput(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.out_put = widgets.Output(
            layout={'border': '1px solid black'}, )

    def show(self):
        return self.out_put

    def clear(self):
        self.out_put.clear_output()

    def get_output(self):
        return self.out_put
