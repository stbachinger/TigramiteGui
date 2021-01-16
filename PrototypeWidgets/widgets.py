# this includes all the widgets needed for the notebook
import os
import PrototypeWidgets.constants as constants
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
        descr = parameter["name"] # parameter.name
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


def dropdown_selection_widget(options, value, description, parameter_dict):
    drop_down = widgets.Dropdown(
        options=options,
        value=value,
        description=description,
        disabled=False
    )
    parameter_accordion = ParameterSelectionWidget(parameter_dict[drop_down.value])
    return widgets.VBox([drop_down, parameter_accordion.show()])


def run_button_widget():
    return widgets.Button(description="Run")


def accordionWidget(path_of_data):
    methods_widget = dropdown_selection_widget(constants.METHODS, constants.METHODS[0], "Methods:", constants.METHOD_PARAMETER)
    test_widget = dropdown_selection_widget(constants.TESTS, constants.TESTS[0], "Tests:", constants.TEST_PARAMETER)
    data_widget = data_upload_widget(path_of_data, "Data:")
    mask_widget = data_upload_widget(path_of_data, "Masks: ")
    accordion = widgets.Accordion(
        children=[data_widget, mask_widget, methods_widget, test_widget])
    accordion.set_title(2, 'Method')
    accordion.set_title(3, 'Test')
    accordion.set_title(0, 'Data')
    accordion.set_title(1, 'Mask')
    return accordion



