# --- A Class to represent a Quadrant in the GUI.
# --- Each Quadrant extends the GTKTextView Class
# --- Author: Callum Warrilow

from gi.repository import Gtk

class Quadrant(Gtk.TextView):

    FILE_PATH = ""

    # --- CONSTRUCTOR
    def __init__(self):
        Gtk.TextView.__init__(self)
        self.set_wrap_mode(Gtk.WrapMode.WORD)
    # end CONSTRUCTOR

    # --- CONSTRUCTOR (sets file path within constructor)
    def __init__(self, filePath, quadNum):
        Gtk.TextView.__init__(self)
        self.set_wrap_mode(Gtk.WrapMode.WORD)
        self.setFilePath(filePath, quadNum)
    # end CONSTRUCTOR

    # --- method to get the path for the file containing text for this quadrant
    def getFilePath():
        return FILE_PATH
    # end getFilePath()

    # --- method to set the path for the file containing text for this quadrant
    def setFilePath(self, filePath, quadNum):
        FILE_PATH = filePath + ("quad" + quadNum)
    # end setFilePath()

    # --- method to read the contents of the file for this quadrant
    def readFromFile():
        # open the file for the quadrant that called the method
        with open(FILE_PATH) as quadFile:
            quadContent = quadFile.read()
            # add contents of file to the TextView
            self.set_text(quadContent)
        return
    # end readFromFile()

    # --- method to write the contents of the file for this quadrant from the
    # text buffer
    def writeToFile():
        return
    # end writeToFile()
