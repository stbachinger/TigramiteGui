"""This file contains all the widget functionality"""

# Author: Sarah Bachinger <sarahbachinger@gmx.de>
# License: GNU General Public License v3.0
import os
import ipywidgets as widgets
from ipywidgets import Widget


def DataUploadWidgets(path_of_data, name):
    """Widget used for data and mask upload"""
    list_dir = []
    for entry in os.scandir(path_of_data):
        if ".npy" in entry.name:
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
        self.current_parameter_widgets = []
        self.parameters = None
        self.add_parameter_button = widgets.Button(
            description="+"
        )
        self.parameter_dropdown = widgets.Dropdown(options=[])
        self.parameters_widget = widgets.VBox(children=[])
        self.parameter_accordion = widgets.Accordion(children=[])
        self.current_parameter = None
        self.used_parameters = []
        self.parameter_accordion.set_title(0, "Parameter Selection")
        self.setup(parameter_dict)

    def setup(self, params):
        """Sets the different parameters up; call when update"""
        self.parameters = params
        values = []
        for x in self.parameters:
            values.append(x)
        self.parameter_dropdown.options = values
        self.parameter_dropdown.observe(self.on_change, names="value")
        self.parameters_widget.children = [widgets.HBox([self.parameter_dropdown, self.add_parameter_button])]
        self.parameter_accordion.children = [self.parameters_widget]
        self.current_parameter = values[0]
        self.add_parameter_button.on_click(self.add_parameter_to_parameter_widget)
        return self

    def add_parameter_to_parameter_widget(self, b):
        """adds """
        parameter = Parameter(self.parameters[self.current_parameter])
        self.current_parameter_widgets.append(parameter.widget)
        self.used_parameters.append(parameter)
        self.parameters_widget.children = tuple(list(self.parameters_widget.children) + [parameter.widget])

    def on_change(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            self.current_parameter = change['new']

    def get_currently_selected_parameters(self):
        dict_values = {}
        for para in self.used_parameters:
            name, value = para.get_current_value()
            dict_values[name] = value
        return dict_values

    def update(self, params):
        self.used_parameters = []
        self.parameters_widget.children = [widgets.HBox([self.parameter_dropdown, self.add_parameter_button])]
        self.setup(params)


class Parameter(Widget):
    def __init__(self, parameter, **kwargs):
        super().__init__(**kwargs)
        self.name = '%s' % parameter["name"]
        self.para_dict = parameter
        self.widget = None
        if parameter["dtype"] == "int":
            self.widget = widgets.IntSlider(description=self.name)
        elif parameter["dtype"] == "float":
            self.widget = widgets.FloatSlider(description=self.name)
        elif parameter["dtype"] == "str":
            self.widget = widgets.Text(description=self.name)
        elif parameter["dtype"] == "bool":
            self.widget = widgets.Checkbox(description=self.name)
        elif parameter["dtype"] == "dict":
            self.widget = widgets.Text(description=self.name)
        elif parameter["dtype"] == "selection":
            self.widget = widgets.Dropdown(description=self.name, options=parameter["selection"])
        else:
            raise Exception("something is wrong!")

    def get_current_value(self):
        return self.para_dict["name"], self.widget.value


class DropdownSelectionWidget(Widget):
    """Handles functionality for Method and Parameter Selection; consists of a Dropdown Menu and a
    ParameterAccordion instance"""

    def __init__(self, options, value, description, parameter_dict, **kwargs):
        super().__init__(**kwargs)
        self.drop_down = widgets.Dropdown(
            options=options,
            value=value,
            description=description,
            disabled=False
        )
        self.parameter_dict = parameter_dict
        self.drop_down.observe(self.on_change, names="value")
        self.parameter_accordion = ParameterSelectionWidget(self.parameter_dict[self.drop_down.value])
        self.widget = widgets.VBox([self.drop_down, self.parameter_accordion.parameter_accordion])

    def get_value(self):
        return self.drop_down.value

    def on_change(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            # print('change '+ change['new'])
            self.update(self.parameter_dict[change['new']])

    def update(self, params):
        self.parameter_accordion.update(params)

    def get_parameter_values(self):
        return self.parameter_accordion.get_currently_selected_parameters()


def plots_widget(plots, value):
    """Dropdown widget for plot selection"""
    return widgets.Dropdown(
        options=plots,
        value=value,
        description="Plot:",
        disabled=False,
        continuous_update=False,
    )


def run_button_widget():
    """run button"""
    return widgets.Button(description="Run")


def plots_show_button():
    """show button"""
    return widgets.Button(description="Show")
