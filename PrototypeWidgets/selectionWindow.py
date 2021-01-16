import ipywidgets as widgets
from PrototypeWidgets.widgets import accordionWidget, run_button_widget
import PrototypeWidgets.constants as constants


def selection_window():
    accordion = accordionWidget(constants.DATA_PATH)
    run_button = run_button_widget()
    return widgets.VBox([accordion, run_button])
