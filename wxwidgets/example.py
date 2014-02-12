import wx

class ExampleWindow(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="PyGrunn Demo", pos=(250, 150), size=(300, 200))

        # Set up the window
        self.Bind(wx.EVT_CLOSE, self.close_handler)
        panel = wx.Panel(self)

        # Create the label
        label = wx.StaticText(panel, -1, "This is an example label. Click on the button below to show a dialog.")
        label.SetSize(label.GetBestSize())

        # Create the button
        button = wx.Button(panel, wx.ID_CLOSE, "Click Me!")
        button.Bind(wx.EVT_BUTTON, self.click_handler)

        # Create a box
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(label, 1, wx.ALL | wx.ALIGN_CENTER, 20)
        vbox.Add(button, 1, wx.ALL | wx.ALIGN_CENTER, 20)
        panel.SetSizer(vbox)
        panel.Layout()

    def close_handler(self, event):
        self.Destroy()

    def click_handler(self, event):
        # Initialize a dialog window
        dialog = wx.MessageDialog(self, "Now go grab yourself a cold one, because you've earned it!", "You clicked the button.", wx.OK|wx.ICON_INFORMATION)

        # Show the dialog window, blocks until the window is dismissed
        dialog.ShowModal()

        # Clean up
        dialog.Destroy()

app = wx.App()
top = ExampleWindow()
top.Show()
app.MainLoop()
