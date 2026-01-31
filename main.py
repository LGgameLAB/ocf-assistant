import gi, sys
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from assistant import Assistant



def main(app):
    assistant_window = Assistant(application=app)
    assistant_window.present()


if __name__ == "__main__":
    app = Gtk.Application(application_id='org.gtk.Example')
    app.connect('activate', main)
    app.run(sys.argv)
