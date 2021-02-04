import ipywidgets as widgets
import PrototypeWidgets.selectionWindow as sw
from PrototypeWidgets.plotWindow import PlotOut
from PrototypeWidgets.widgets import run_button_widget, plots_show_button
from PrototypeWidgets.methods import calculate_results, make_plot
from PrototypeWidgets.terminalWindow import TerminalOutput
import PrototypeWidgets.constants as constants


class ProjectWindow:
    """Project Window should contain: SelectionWindow, PlotWindow, TerminalWindow"""

    def __init__(self, data_path=constants.DATA_PATH, methods=constants.METHODS,
                 method_parameters=constants.METHOD_PARAMETER, tests=constants.TESTS,
                 test_parameter=constants.TEST_PARAMETER):
        self.plots_button = plots_show_button()
        self.SelectionWindow = sw.SelectionWindow(data_path, methods, method_parameters, tests, test_parameter)
        self.run_button = run_button_widget()
        self.results = None
        self.pcmci = None
        self.run_button.on_click(self.on_run_button_clicked)
        self.terminal_out = TerminalOutput()
        self.plot_out = PlotOut()
        self.plots_button.on_click(self.on_plot_button_clicked)

    def show(self):
        return widgets.VBox(
            [
                self.SelectionWindow.accordion,
                widgets.HBox([self.run_button]),
                widgets.HBox([self.terminal_out.show(),
                              widgets.VBox(
                                  [self.plot_out.show(), self.plots_button]
                              )])
            ])

    def on_run_button_clicked(self, b):
        data, mask, method, test, method_params, test_params = self.SelectionWindow.get_current_values()
        self.pcmci, self.results = calculate_results(data, mask, method, test, method_params, test_params,
                                                     self.terminal_out.get_output())

    def on_plot_button_clicked(self, b):
        plot_type = self.plot_out.get_current_values()
        result = make_plot(plot_type, self.pcmci, self.results, self.plot_out.get_output())
