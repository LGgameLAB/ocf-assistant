import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


class Greeter(Gtk.Window):
    '''
        The greeter/welcome page application
    '''
    title = "Welcome"

    def __init__(self, app):
        super().__init__(self.title, application=app)

        self.load_components()

    def load_components(self):
        btn = Gtk.Button(label="Hello, World!")
        btn.connect('clicked', lambda x: self.win.close())
        self.set_child(btn)

    def run(self):
        self.win.present()
