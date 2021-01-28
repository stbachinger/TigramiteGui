import ipywidgets as widgets
from ipywidgets import Widget
from PrototypeWidgets import plots_widget
from PrototypeWidgets import constants


class PlotOut(Widget):
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
        return widgets.VBox([self.title, self.out, self.plot_selection_widget])

    def get_current_values(self):
        return self.plot_selection_widget.value

    def clear(self):
        self.out.clear_output()

    def get_output(self):
        return self.out
