from gi.repository import Gtk

class ExampleWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="PyGrunn Demo")

        # Create the label
        label = Gtk.Label()
        label.set_markup("This is an <b>example label</b>.\nClick on the button below to show a dialog.")

        # Create the button
        button = Gtk.Button(label="Click me!")
        button.connect("clicked", self.click_handler)

        # Create a box
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20, margin=20)
        vbox.set_homogeneous(False)
        vbox.pack_start(label, True, True, 0)
        vbox.pack_start(button, True, True, 0)
        self.add(vbox)

    def click_handler(self, sender):
        # Initialize a dialog window
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "You clicked the button.")
        dialog.format_secondary_text("Now go grab yourself a cold one, beause you've earned it!")

        # Show the dialog window, blocks until the window is dismissed
        dialog.run()

        # Clean up
        dialog.destroy()

window = ExampleWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
