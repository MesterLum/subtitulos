from tkFileDialog import askopenfilename

class Process:

    def openFile(self):
        filename = askopenfilename()
        print filename
        