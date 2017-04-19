# --- A Class to hold all the GUI elements of the Quad app
# --- Author: Callum Warrilow

import gi
import os
from gi.repository import Gtk
from Quadrant import Quadrant
from os.path import expanduser

class QuadWindow(Gtk.Window):

    # ----- FIELDS -----
    home = expanduser("~")
    quadPath = home + "/.quad/"
    quad = []

    # ----- CONSTRUCTOR -----
    def __init__(self):
        Gtk.Window.__init__(self)
        self.quadGrid = Gtk.Grid()
        self.add(self.quadGrid)

        self.createGUI()
    # ----- END CONSTRUCTOR -----

    # --- method for making other method calls to setup the whole GUI
    def createGUI(self):
        global quad

        for quadID in range(0, 4):
            self.createQuad(self.quad, quadID)
        return
    # end createGUI()

    # --- method to specifically create an instance of Quadrant on the Window
    def createQuad(self, quad, quadID):

        # create quadrants
        newQuad = Quadrant(self.quadPath, quadID)
        quad.append(newQuad)
        quad[quadID].set_left_margin(10)
        quad[quadID].set_right_margin(10)
        quad[quadID].readFromFile()

        # set quad position in grid based on ID
        if(quadID == 0):
            self.quadGrid.add(quad[quadID])
        elif(quadID == 1):
            self.quadGrid.attach_next_to(quad[quadID], quad[0], Gtk.PositionType.RIGHT, 1, 1)
        elif(quadID == 2):
            self.quadGrid.attach_next_to(quad[quadID], quad[0], Gtk.PositionType.BOTTOM, 1, 1)
        elif(quadID == 3):
            self.quadGrid.attach_next_to(quad[quadID], quad[1], Gtk.PositionType.BOTTOM, 1, 1)
    # end createQuad()
