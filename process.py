from tkFileDialog import askopenfilename
import ntpath
from google import google
import tkMessageBox
from bs4 import BeautifulSoup
import urllib2

"""
    *Author: Cuauhtemoc Paez,
    *Date  : 25/08/2017,

    *Notes : 
            la funcion openFile obtiene el nombre, es invocada desde el boton, obtiene-
            la ruta, en base a la ruta extrae el nombre con extension y lo limpio.

            PROBLEMA: si hay mas de una extension solo limpia 1
"""

class Process:

    def openFile(self):

        fileRout = askopenfilename()
        fileName = ntpath.basename(fileRout)
        name = fileName.split(".")
        nameLength = len(name)
        ext = name[nameLength-1]

        if (ext == "mp4" or ext == "mvk"):
            nameClear = fileName.replace("."," ").replace(","," ").replace("-"," ")
            nameSearch = "Subtitulos " + nameClear.replace(ext, "")
            resultsGoogle = self.googleSearch(nameSearch)
            self.readDOM(resultsGoogle)

        else:
            tkMessageBox.showerror("ERROR!","Solo se permiten formatos .mp4 y mvk")


    def googleSearch(self, search):
        
        search_results = google.search(search, 3)
        return search_results


    def readDOM(self, search_results):

        for results in search_results:
            content = urllib2.urlopen(results.link)
            contentHTML = BeautifulSoup(content, "html.parser")
            for link in contentHTML.find_all("a"):
                print link
            break


        