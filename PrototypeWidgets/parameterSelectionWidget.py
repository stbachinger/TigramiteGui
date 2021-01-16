import ipywidgets as widgets


class ParameterSelectionWidget:
    """Parameter Selection Template; should have an accordion widget filled with a Drop-down widget displaying values"""

    def __init__(self, values, values_types, values_default):
        self.values = values
        self.values_types = values_types
        self.values_default = values_default
        parameters = {}
        for i in range(len(values)):
            parameters[values[i]] = self.Parameter(values[i], values_types[i], values_default[i])
        self.parameters = parameters
        self.add_parameter_button = widgets.Button(
            description="+"
        )
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
        print("bla")
        descr = "parameter"#parameter.name
        if parameter.t == "int":
            return widgets.IntSlider(descrition=descr)
        elif parameter.t == "float":
            return widgets.FloatSlider(description=descr)
        elif parameter.t == "str":
            return widgets.Text(description=descr)
        elif parameter.t == "bool":
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

    class Parameter:
        def __init__(self, name, t, d):
            self.name = name
            self.t = t
            self.d = d

        def __str__(self):
            return "Parameter " + self.name + self.t + self.d
