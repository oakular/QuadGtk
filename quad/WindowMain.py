# --- A Class to hold all the GUI elements of the Quad app
# --- Author: Callum Warrilow

import gi
import os
from gi.repository import Gtk
from gi.repository import Gdk

from src.Quadrant import Quadrant
from os.path import expanduser

class QuadWindow(Gtk.Window):

    # ----- FIELDS -----
    home = expanduser("~")
    quadPath = home + "/.quad/"
    quad = []
    quadScroll = []

    # ----- CONSTRUCTOR -----
    def __init__(self):
        Gtk.Window.__init__(self)
        self.quadGrid = Gtk.Grid()
        self.quadGrid.set_row_spacing(5)
        self.quadGrid.set_column_spacing(5)
        self.add(self.quadGrid)

        self.createGUI()
    # ----- END CONSTRUCTOR -----

    # --- method for making other method calls to setup the whole GUI
    def createGUI(self):
        global quad, quadScroll

        for quadID in range(0, 4):
            self.createQuad(self.quad, quadID)
            self.createScrollWin(self.quad, self.quadScroll, quadID)
        return
    # end createGUI()

    # --- method to specifically create an instance of Quadrant on the Window
    def createQuad(self, quad, quadID):

        # init quadrant
        newQuad = Quadrant(self.quadPath, quadID)
        quad.append(newQuad)

        # set margins
        quad[quadID].set_left_margin(10)
        quad[quadID].set_top_margin(10)
        quad[quadID].set_bottom_margin(10)
        quad[quadID].set_right_margin(10)

        # draw border
        quad[quadID].props.border_width = 4

        # add text from file
        quad[quadID].readFromFile()

    # end createQuad()

    # --- method to wrap the Quadrant passed as param around a scroll window.
    # Method then adds scroll window to GUI
    def createScrollWin(self, quad, quadScroll, quadID):

        scrollWin = Gtk.ScrolledWindow(hadjustment=None, vadjustment=None)
        scrollWin.set_size_request(150, 150)
        scrollWin.set_shadow_type(Gtk.ShadowType.OUT)
        self.quadScroll.append(scrollWin)

        self.quadScroll[quadID].add(quad[quadID])

        # set quad position in grid based on ID
        if(quadID == 0):
            self.quadGrid.add(self.quadScroll[quadID])
        elif(quadID == 1):
            self.quadGrid.attach_next_to(self.quadScroll[quadID],
                    self.quadScroll[0], Gtk.PositionType.RIGHT, 1, 1)
        elif(quadID == 2):
            self.quadGrid.attach_next_to(self.quadScroll[quadID],
                    self.quadScroll[0], Gtk.PositionType.BOTTOM, 1, 1)
        elif(quadID == 3):
            self.quadGrid.attach_next_to(self.quadScroll[quadID],
                    self.quadScroll[1], Gtk.PositionType.BOTTOM, 1, 1)
    # end createScrollWin

    # --- method to handle key presses
    def keyHandling(self, event):
        global quad

        keyname = Gdk.keyval_name(event.keyval)

        # save file when ctrl+s is pressed
        if keyname == 's':
            if event.get_state() == Gdk.ModifierType.CONTROL_MASK:
                print("- saved to file")
                for quadID in range (0, 4):
                    self.quad[quadID].writeToFile()
    # end keyHandling()
