from tkFileDialog import askopenfilename
import ntpath
from google import google
import tkMessageBox
from bs4 import BeautifulSoup
import urllib2
import wget
import threading
import urllib
import rarfile
import os
import tkMessageBox
import shutil

"""
    *Author: Cuauhtemoc Paez,
    *Date  : 25/08/2017,

    *Notes : 
            la funcion openFile obtiene el nombre, es invocada desde el boton, obtiene-
            la ruta, en base a la ruta extrae el nombre con extension y lo limpio.

            PROBLEMA: Si hay mas de una extension solo limpia 1,
                      De momento solo funciona para subdix (pagina de subtitulos)
            *Update: Threading, se pueden anexar mas de un fichero para descargar el material.
            
"""

class Process:
    
    global __ThreadFile

    def __trheadDownloadSubtitles(self, nameSearch, fileRoutPure):
        
        self.__ThreadFile = threading.Thread(target=self.readDOM, args=(nameSearch,fileRoutPure,))
        self.__ThreadFile.setName(nameSearch)
        self.__ThreadFile.start()


    def openFile(self):

        fileRout = askopenfilename()
        fileName = ntpath.basename(fileRout)
        fileRoutPure = ntpath.dirname(fileRout)
        

        name = fileName.split(".")
        nameLength = len(name)
        ext = name[nameLength-1]

        if (ext == "mp4" or ext == "mvk"):
            nameClear = fileName.replace("."," ").replace(","," ").replace("-"," ").replace(ext, "")
            
            self.__trheadDownloadSubtitles(nameClear, fileRoutPure)

        else:
            tkMessageBox.showerror("ERROR!","Solo se permiten formatos .mp4 y mvk")


    def googleSearch(self, search):
        
        search_results = google.search(search, 1)
        return search_results


    def readDOM(self, nameSearch, fileRoutPure):

        print "Cargando..."
        nDownloads = 0
        ready = False

        resultsGoogle = self.googleSearch("Subtitulos " + nameSearch)
        for results in resultsGoogle:
            if (ready):
                break
            content = urllib2.urlopen(results.link)
            contentHTML = BeautifulSoup(content, "html.parser")
            for link in contentHTML.select("a[href*='bajar.php']"):
                if (nDownloads == 3):
                    ready = True
                    break
                nDownloads+=1
                href = BeautifulSoup(str(link), "html.parser")
                downloadLink = href.a['href']
                self.__downloadFile(downloadLink,str(nDownloads), fileRoutPure, nameSearch)
        
        tkMessageBox.showinfo("Terminado!", "Subtitulos para: " + nameSearch + " Terminado")
        print self.__ThreadFile.getName()
          




    def __downloadFile(self, url, name, fileRoutPure, nameDirectory):

        tmpDirectory = "./tmp/" + nameDirectory.replace(" ", "-")

        if (not os.path.exists(tmpDirectory)):
            os.mkdir(tmpDirectory)
        
        nameRar = name + ".rar"
        urllib.urlretrieve(url, filename= tmpDirectory + "/" +nameRar)
        
        Directory = fileRoutPure+"/" + nameDirectory.replace(" ", "-") + "subtitulo-" + name
        if (not os.path.exists(Directory)):
            os.mkdir(Directory)
        
        with rarfile.RarFile(tmpDirectory + "/" + nameRar) as rf:
            rf.extractall(Directory)

        shutil.rmtree(tmpDirectory)
        
            
        
        
        
