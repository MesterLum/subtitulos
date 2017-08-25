from Tkinter import Button
import process

class Frame:

    global __app
    global __openfile
    global __process

    def __init__(self, app):

        self.__app = app
        self.__process = process.Process()
        self.__initialize()   
        
    def __initialize(self):
        self.__openfile = Button(self.__app, text="Abrir", command = lambda : self.__process.openFile())
        self.__openfile.grid(row=0,column=0)