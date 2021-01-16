# this includes all the widgets needed for the notebook
import os
import ipywidgets as widgets
from ipywidgets import Widget


class MethodWidget:
    def __init__(self):
        self.widget = widgets.Dropdown(
            options=["PCMCI", "PCMCI+"],
            value="PCMCI",
            description="Method:",
            disabled=False
        )

    def get_widget(self):
        return widgets.Dropdown(
            options=["PCMCI", "PCMCI+"],
            value="PCMCI",
            description="Method:",
            disabled=False
        )


'''Widget used for data and mask upload'''


def data_upload_widget(path_of_data, name):
    list_dir = []
    for entry in os.scandir(path_of_data):
        list_dir.append(entry.name)
    list_dir.append("none")
    return widgets.Dropdown(
        options=list_dir,
        value='none',
        description=name,
        disabled=False
    )


class ParameterSelectionWidget(Widget):
    """Parameter Selection Template; should have an accordion widget filled with a Drop-down widget displaying values"""

    def __init__(self, parameter_dict, **kwargs):
        super().__init__(**kwargs)
        parameters = parameter_dict
        self.parameters = parameters
        self.add_parameter_button = widgets.Button(
            description="+"
        )
        values = []
        for x in parameters:
            values.append(x)
        self.parameter_dropdown = widgets.Dropdown(options=values)
        self.parameters_widget = widgets.VBox(
            children=[widgets.HBox([widgets.Dropdown(options=values), self.add_parameter_button])]
        )
        self.parameter_accordion = widgets.Accordion(
            children=[self.parameters_widget]
        )
        self.parameter_accordion.set_title(0, "Parameter Selection")
        self.add_parameter_button.on_click(self.on_button_clicked)
        self.parameter_dropdown.observe(self.on_change)

    def show(self):
        return self.parameter_accordion

    def on_button_clicked(self, b):
        widget = self.add_new_parameter()
        self.parameters_widget.children = tuple(list(self.parameters_widget.children) + [widget])

    def add_new_parameter(self):
        parameter = self.parameters[self.parameter_dropdown.value]
        print(parameter)
        descr = parameter["name"]  # parameter.name
        if parameter["dtype"] == "int":
            return widgets.IntSlider(descrition=descr)
        elif parameter["dtype"] == "float":
            return widgets.FloatSlider(description=descr)
        elif parameter["dtype"] == "str":
            return widgets.Text(description=descr)
        elif parameter["dtype"] == "bool":
            return widgets.Checkbox()
        elif parameter["dtype"] == "dict":
            return widgets.Checkbox()
        elif parameter["dtype"] == "select":
            return widgets.Checkbox()
        else:
            raise Exception("something is wrong!")
        print("tada")

    def on_change(self, change):
        print(change)
        print("called")
        if change['type'] == 'change' and change['name'] == 'value':
            print("changed to %s" % change['new'])
            self.parameter_dropdown.value = change['new']


class DropdownSelectionWidget(Widget):

    def __init__(self, options, value, description, parameter_dict, **kwargs):
        super().__init__(**kwargs)
        self.drop_down = widgets.Dropdown(
            options=options,
            value=value,
            description=description,
            disabled=False
        )
        self.parameter_accordion = ParameterSelectionWidget(parameter_dict[self.drop_down.value])

    def show(self):
        return widgets.VBox([self.drop_down, self.parameter_accordion.show()])

    def get_value(self):
        return self.drop_down.value


def run_button_widget():
    return widgets.Button(description="Run")


def plots_widget(plots, value):
    return widgets.Dropdown(
        options=plots,
        value=value,
        description="Plot:",
        disabled=False,
        continuous_update=False,
    )


def plots_show_button():
    return widgets.Button(description="Show")
