# --- Skeleton Class for drawing a quadrant in a Gtk Window
import gi
import os
from gi.repository import Gtk
from WindowMain import QuadWindow

# setup
win = QuadWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
