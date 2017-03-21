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

    # --- method for making other method calls to setup the whole GUI
    def createGUI():
        return
    # end createGUI()

    # --- method to specifically create an instance of Quadrant on the Window
    def createQuad(self):
        return
    # end createQuad()
