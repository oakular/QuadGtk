# --- A Class to represent a Quadrant in the GUI.
# --- Each Quadrant extends the GTKTextView Class
# --- Author: Callum Warrilow

from gi.repository import Gtk

class Quadrant(Gtk.TextView):

    # ----- FIELDS -----
    quadPath = ''

    # ----- CONSTRUCTOR -----
    def __init__(self):
        Gtk.TextView.__init__(self)
        self.set_wrap_mode(Gtk.WrapMode.WORD)
        self.set_default_size(200, 200)
    # ----- END CONSTRUCTOR -----

    # ----- CONSTRUCTOR (sets file path within constructor)
    def __init__(self, filePath, quadNum):
        # TODO: wrap textview in a ScrolledWindow
        Gtk.TextView.__init__(self)
        self.set_wrap_mode(Gtk.WrapMode.WORD)
        self.set_size_request(150, 150)
        self.setFilePath(filePath, quadNum)
    # ----- END CONSTRUCTOR -----

    # --- method to get the path for the file containing text for this quadrant
    def getFilePath():
        return quadPath
    # end getFilePath()

    # --- method to set the path for the file containing text for this quadrant
    def setFilePath(self, filePath, quadNum):
        self.quadPath = filePath + ("quad" + str(quadNum))
    # end setFilePath()

    # --- method to read the contents of the file for this quadrant
    def readFromFile(self):
        # open the file for the quadrant that called the method
        with open(self.quadPath, 'r') as quadFile:
            quadContent = quadFile.read()
            # add contents of file to the TextView via the textbuffer
            self.textbuffer = self.get_buffer()
            self.textbuffer.set_text(quadContent)
    # end readFromFile()

    # --- method to write the contents of the file for this quadrant from the
    # text buffer
    def writeToFile():
        # open the file for the quadrant that called the method
        with open(self.quadPath, 'w') as quadFile:
            quadContent = self.get_buffer()
            quadFile.write(quadContent)
    # end writeToFile()
