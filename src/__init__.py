# --- Skeleton Class for drawing a quadrant in a Gtk Window
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from WindowMain import QuadWindow

# setup
quadDir = os.path.expanduser("~") + "/.quad/"
if not(os.path.exists(quadDir)):
     os.makedirs(quadDir)

win = QuadWindow()
win.connect("delete-event", Gtk.main_quit)
win.connect("key-press-event", QuadWindow.keyHandling)
win.set_size_request(325,325)
win.set_gravity(Gdk.Gravity.CENTER)
win.show_all()
Gtk.main()
