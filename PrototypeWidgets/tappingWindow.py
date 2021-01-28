import ipywidgets as widgets
from ipywidgets import Widget
from PrototypeWidgets import ProjectWindow


class TappingWindow(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        tab_contents = ['P0', 'P1', 'P2', 'P3', 'P4']
        self.tab = widgets.Tab()
        self.projects = [ProjectWindow().show()]
        self.add_button = widgets.Button(description="+")
        self.add_button.on_click(self.add_button)
        self.tab.children = tuple(list(self.projects) + [self.add_button])
        self.titel = []
        self.tab.set_title(0, 'P0')

    def add_button_click(self, b):
        self.projects.append(ProjectWindow().show())
        self.tab.children = tuple(list(self.projects) + [self.add_button])
