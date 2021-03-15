"""Handles the SelectionWindow Class"""
# License: GNU General Public License v3.0
import ipywidgets as widgets
from ipywidgets import Widget
from PrototypeWidgets import DropdownSelectionWidget, DataUploadWidgets


class SelectionWindow(Widget):
    """Handles the Selection functionality"""
    def __init__(self, data_path, methods, method_parameters, tests, test_parameters, plots, plot_parameters, **kwargs):
        super().__init__(**kwargs)
        self.methods_widget = DropdownSelectionWidget(methods, methods[0], "Methods:",
                                                      method_parameters)
        self.test_widget = DropdownSelectionWidget(tests, tests[0], "Tests:",
                                                   test_parameters)
        self.data_widget = DataUploadWidgets(data_path, "Data:")
        self.mask_widget = DataUploadWidgets(data_path, "Masks: ")
        self.plot_widget = DropdownSelectionWidget(plots, plots[0], "Plots: ", plot_parameters)
        self.accordion = widgets.Accordion(
            children=[
                self.data_widget,
                self.mask_widget,
                self.methods_widget.widget,
                self.test_widget.widget,
                self.plot_widget,
            ])
        self.accordion.set_title(2, 'Method')
        self.accordion.set_title(3, 'Test')
        self.accordion.set_title(0, 'Data')
        self.accordion.set_title(1, 'Mask')
        self.accordion.set_title(4, 'Plot')

    def get_current_values(self):
        """Gets the current values from its attributes"""
        return self.data_widget.value, self.mask_widget.value, self.methods_widget.get_value(), \
               self.test_widget.get_value(), self.methods_widget.get_parameter_values(), self.test_widget.get_parameter_values()
