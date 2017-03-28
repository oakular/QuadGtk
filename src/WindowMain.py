# --- A Class to hold all the GUI elements of the Quad app
# --- Author: Callum Warrilow

import gi
import os
from gi.repository import Gtk
from Quadrant import Quadrant
from os.path import expanduser

class QuadWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self)
        quadGrid = Gtk.Grid()
        self.add(quadGrid)

        self.createGUI()

    # --- method for making other method calls to setup the whole GUI
    def createGUI(self):
        self.createQuad()
        return
    # end createGUI()

    # --- method to specifically create an instance of Quadrant on the Window
    def createQuad(self):
        # create quadrants
        quad0 = Quadrant(quadPath, 0)
        quad0.readFromFile()
        grid.add(quad0)

        quad1 = Quadrant(quadPath, 1)
        quad1.readFromFile()
        grid.attach_next_to(quad1, quad0, Gtk.PositionType.RIGHT, 1, 1)

        quad2 = Quadrant(quadPath, 2)
        quad2.readFromFile()
        grid.attach_next_to(quad2, quad0, Gtk.PositionType.BOTTOM, 1, 1)

        quad3 = Quadrant(quadPath, 3)
        quad3.readFromFile()
        grid.attach_next_to(quad3, quad1, Gtk.PositionType.BOTTOM, 1, 1)
    # end createQuad()
