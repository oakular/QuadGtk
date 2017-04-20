# --- Skeleton Class for drawing a quadrant in a Gtk Window
import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from WindowMain import QuadWindow

# setup
win = QuadWindow()
win.connect("delete-event", Gtk.main_quit)
win.connect("key-press-event", QuadWindow.keyHandling)
win.show_all()
Gtk.main()
