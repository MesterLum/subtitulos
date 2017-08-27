from tkFileDialog import askopenfilename
import ntpath
from google import google
import tkMessageBox
from bs4 import BeautifulSoup
import urllib2
import threading

"""
    *Author: Cuauhtemoc Paez,
    *Date  : 25/08/2017,

    *Notes : 
            la funcion openFile obtiene el nombre, es invocada desde el boton, obtiene-
            la ruta, en base a la ruta extrae el nombre con extension y lo limpio.

            PROBLEMA: si hay mas de una extension solo limpia 1,
            *Update: Threading, se pueden anexar mas de un fichero para descargar el material.
            
"""

class Process:

    global __ThreadFile

    def __trheadDownloadSubtitles(self, nameSearch):
        
        self.__ThreadFile = threading.Thread(target=self.readDOM, args=(nameSearch,))
        self.__ThreadFile.start()


    def openFile(self):

        fileRout = askopenfilename()
        fileName = ntpath.basename(fileRout)
        name = fileName.split(".")
        nameLength = len(name)
        ext = name[nameLength-1]

        if (ext == "mp4" or ext == "mvk"):
            nameClear = fileName.replace("."," ").replace(","," ").replace("-"," ").replace(ext, "")
            nameSearch = "Subtitulos " + nameClear
            self.__trheadDownloadSubtitles(nameSearch)

        else:
            tkMessageBox.showerror("ERROR!","Solo se permiten formatos .mp4 y mvk")


    def googleSearch(self, search):
        
        search_results = google.search(search, 3)
        return search_results


    def readDOM(self, nameSearch):

        print "Cargando..."
        resultsGoogle = self.googleSearch(nameSearch)
        for results in resultsGoogle:
            content = urllib2.urlopen(results.link)
            contentHTML = BeautifulSoup(content, "html.parser")
            for link in contentHTML.a["href"]:
                print link
            break
        print "Termine"      