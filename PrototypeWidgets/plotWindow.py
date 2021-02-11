"""Handles the PlotOut Class"""
# License: GNU General Public License v3.0
import ipywidgets as widgets
from ipywidgets import Widget
from PrototypeWidgets import plots_widget
from PrototypeWidgets import constants


class PlotOut(Widget):
    """Handles plotting functionality"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.out = widgets.Output(
            layout={
                'border': '1px solid black',
                'min_width': '300px',
                'width': 'auto',
                'height': '300px',
                'overflow': 'scroll'

            })
        self.plot_selection_widget = plots_widget(constants.PLOTS, constants.PLOTS[0])
        self.title = widgets.HTML(
            value="<H3>Plots</H3>",
        )

    def show(self):
        """Shows the output widget"""
        return widgets.VBox([self.title, self.out, self.plot_selection_widget])

    def get_current_values(self):
        """Returns current values"""
        return self.plot_selection_widget.value

    def get_output(self):
        """Gets output from output widget"""
        return self.out
