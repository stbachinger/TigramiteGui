import ipywidgets as widgets


class ParameterSelectionWidget:
    """Parameter Selection Template; should have an accordion widget filled with a Drop-down widget displaying values"""

    def __init__(self, values, value_types):
        self.values = values
        self.value_types = value_types
        self.add_parameter_button = widgets.Button(
            description="+"
        )
        self.parameters_widget = widgets.VBox(
            children=[widgets.HBox([values, self.add_parameter_button])]
        )
        self.parameter_accordion = widgets.Accordion(
            children=[self.parameters_widget]
        )
        self.parameter_accordion.set_title(0, "Parameter Selection")
        self.add_parameter_button.on_click(self.on_button_clicked)

    def show(self):
        return self.parameter_accordion

    def on_button_clicked(self, b):
        self.parameters_widget.children = tuple(list(self.parameters_widget.children) + [self.add_parameter_button])

    def add_new_parameter(self):
        print("tada")
