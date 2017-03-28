# --- Skeleton Class for drawing a quadrant in a Gtk Window
import gi
import os
from gi.repository import Gtk
from Quadrant import Quadrant
from os.path import expanduser

home = expanduser("~")
quadPath = home + "/.quad/"

# create window and grid
win = Gtk.Window()
grid = Gtk.Grid()
win.add(grid)

# create quadrants
quad0 = Quadrant(quadPath, 0)
quad0.readFromFile()
grid.add(quad0)

quad1 = Quadrant(quadPath, 1)
quad1.readFromFile()
grid.attach_next_to(quad1, quad0, Gtk.PositionType.RIGHT, 1, 1)

# final setup
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
