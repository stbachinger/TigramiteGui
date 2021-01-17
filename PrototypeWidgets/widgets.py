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
        self.parameters = None
        self.add_parameter_button = widgets.Button(
            description="+"
        )
        self.add_parameter_button.on_click(self.on_button_clicked)
        self.parameter_dropdown = None
        self.parameters_widget = None
        self.parameter_accordion = None
        self.current_parameter = None
        self.used_parameters = []
        self.setup(parameter_dict)

    def setup(self, params):
        self.parameters = params
        #print(params)
        values = []
        for x in self.parameters:
            values.append(x)
        self.parameter_dropdown = widgets.Dropdown(options=values)
        self.parameter_dropdown.observe(self.on_change, names="value")
        self.parameters_widget = widgets.VBox(
            children=[widgets.HBox([self.parameter_dropdown, self.add_parameter_button])]
        )
        self.parameter_accordion = widgets.Accordion(
            children=[self.parameters_widget]
        )
        self.parameter_accordion.set_title(0, "Parameter Selection")
        self.current_parameter = values[0]
        return self

    def show(self):
        return self.parameter_accordion

    def on_button_clicked(self, b):
        widget = self.add_new_parameter()
        self.used_parameters.append(widget)
        self.parameters_widget.children = tuple(list(self.parameters_widget.children) + [widget.show()])

    def add_new_parameter(self):
        parameter = self.parameters[self.current_parameter]
        return Parameter(parameter)

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
        return self.setup(params)


class Parameter(Widget):
    def __init__(self, parameter, **kwargs):
        super().__init__(**kwargs)
        self.name = '%s' % parameter["name"]
        self.para_dict = parameter
        self.parameter = None
        if parameter["dtype"] == "int":
            self.parameter = widgets.IntSlider(description=self.name)
        elif parameter["dtype"] == "float":
            self.parameter = widgets.FloatSlider(description=self.name)
        elif parameter["dtype"] == "str":
            self.parameter = widgets.Text(description=self.name)
        elif parameter["dtype"] == "bool":
            self.parameter = widgets.Checkbox(description=self.name)
        elif parameter["dtype"] == "dict":
            self.parameter = widgets.Text(description=self.name)
        elif parameter["dtype"] == "selection":
            self.parameter = widgets.Dropdown(description=self.name, options=parameter["selection"])
        else:
            raise Exception("something is wrong!")

    def show(self):
        return self.parameter

    def get_current_value(self):
        return self.para_dict["name"], self.parameter.value


class DropdownSelectionWidget(Widget):

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

    def show(self):
        return widgets.VBox([self.drop_down, self.parameter_accordion.show()])

    def get_value(self):
        return self.drop_down.value

    def on_change(self, change):
        if change['type'] == 'change' and change['name'] == 'value':
            print('change '+ change['new'])
            self.parameter_accordion.update(self.parameter_dict[change['new']])

    def get_parameter_values(self):
        return self.parameter_accordion.get_currently_selected_parameters()


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
