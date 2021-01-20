import ipywidgets as widgets
from ipywidgets import Widget
from PrototypeWidgets import DropdownSelectionWidget, constants as constants, data_upload_widget
import PrototypeWidgets.constants as constants


class SelectionWindow(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.methods_widget = DropdownSelectionWidget(constants.METHODS, constants.METHODS[0], "Methods:",
                                                        constants.METHOD_PARAMETER)
        self.test_widget = DropdownSelectionWidget(constants.TESTS, constants.TESTS[0], "Tests:",
                                                     constants.TEST_PARAMETER)
        self.data_widget = data_upload_widget(constants.DATA_PATH, "Data:")
        self.mask_widget = data_upload_widget(constants.DATA_PATH, "Masks: ")
        self.accordion = widgets.Accordion(
            children=[self.data_widget, self.mask_widget, self.methods_widget.widget, self.test_widget.widget])
        self.accordion.set_title(2, 'Method')
        self.accordion.set_title(3, 'Test')
        self.accordion.set_title(0, 'Data')
        self.accordion.set_title(1, 'Mask')

    def get_current_values(self):
        return self.data_widget.value, self.mask_widget.value, self.methods_widget.get_value(), \
               self.test_widget.get_value(), self.methods_widget.get_parameter_values(), self.test_widget.get_parameter_values()
