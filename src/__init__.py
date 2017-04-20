# --- Skeleton Class for drawing a quadrant in a Gtk Window
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
from WindowMain import QuadWindow

# setup
win = QuadWindow()
win.connect("delete-event", QuadWindow.main_quit)
win.connect("key-press-event", QuadWindow.keyHandling)
win.set_size_request(325,325)
win.set_gravity(Gdk.Gravity.CENTER)
win.show_all()
Gtk.main()
