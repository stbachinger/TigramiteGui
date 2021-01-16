import ipywidgets as widgets
from ipywidgets import Widget
from PrototypeWidgets import plots_widget
from PrototypeWidgets import constants


class PlotOut(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.out = widgets.Output(layout={'border': '1px solid black'})
        self.plots = plots_widget(constants.PLOTS, constants.PLOTS[0])

    def show(self):
        return widgets.VBox([self.plots, self.out])

    def get_current_values(self):
        return self.plots.value

    def clear(self):
        self.out.clear_output()

    def get_output(self):
        return self.out
