# --- A Class to hold all the GUI elements of the Quad app
# --- Author: Callum Warrilow

import gi
import os
from gi.repository import Gtk
from Quadrant import Quadrant
from os.path import expanduser

class QuadWindow(Gtk.Window):

    home = expanduser("~")
    quadPath = home + "/.quad/"
    quad[4] = None

    def __init__(self):
        Gtk.Window.__init__(self)
        self.quadGrid = Gtk.Grid()
        self.add(self.quadGrid)

        self.createGUI()

    # --- method for making other method calls to setup the whole GUI
    def createGUI(self):
        self.createQuad()
        return
    # end createGUI()

    # --- method to specifically create an instance of Quadrant on the Window
    def createQuad(self):
        # create quadrants
        quad0 = Quadrant(self.quadPath, 0)
        quad0.set_left_margin(10)
        quad0.set_right_margin(10)
        quad0.readFromFile()
        self.quadGrid.add(quad0)

        quad1 = Quadrant(self.quadPath, 1)
        quad1.set_left_margin(10)
        quad1.set_right_margin(10)
        quad1.readFromFile()
        self.quadGrid.attach_next_to(quad1, quad0, Gtk.PositionType.RIGHT, 1, 1)

        quad2 = Quadrant(self.quadPath, 2)
        quad2.set_left_margin(10)
        quad2.set_right_margin(10)
        quad2.readFromFile()
        self.quadGrid.attach_next_to(quad2, quad0, Gtk.PositionType.BOTTOM, 1, 1)

        quad3 = Quadrant(self.quadPath, 3)
        quad3.set_left_margin(10)
        quad3.set_right_margin(10)
        quad3.readFromFile()
        self.quadGrid.attach_next_to(quad3, quad1, Gtk.PositionType.BOTTOM, 1, 1)
    # end createQuad()
