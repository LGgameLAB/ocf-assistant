import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk
from greeter import Greeter

def main():
    app = Gtk.Application(application_id='org.gtk.Example')
    greeter_window = Greeter(app)
    # app.connect('activate', greeter_window.run)
    app.run(None)
    print("Hello from ocf-greeter!")


if __name__ == "__main__":
    main()
