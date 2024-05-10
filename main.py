import sys
import os
import time
import threading
import PIL.Image
import pytesseract
from components.TextEditor import TextEditor
from components.FileList import FileList
from components.FileListItem import FileItem
from PyQt6 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg
from PyQt6.QtWidgets import QGroupBox as qgb, QHBoxLayout as qhl, QVBoxLayout as qvl
from PyQt6.QtCore import pyqtSignal as Signal
from PyQt6.QtGui import QAction

class MyApp(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(959, 667)
        #SET STYLE
        with open('styles/style.css', 'r') as fh:
            self.setStyleSheet(fh.read())

        #VARIABLES
        self.imageExtensions = ['.jpg', '.png', '.jpeg', '.bmp']
        self.saveExtension = '.txt'
        self.path = ''
        self.filePathList = []
        #============================================================
        #ACTIONS & MENUS

        #FILE MENU ACTIONS
        self.fileMenu = qtw.QMenu('File')

        self.fileActionNew = QAction('New')
        self.fileActionOpen = QAction('Open')
        self.fileActionImport = QAction('Import')
        self.fileActionImportFolder = QAction('Import Folder')
        self.fileActionSave = QAction('Save')
        self.fileActionSaveAs = QAction('Save As...')
        self.fileActionClose = QAction('Close')
        self.fileActionExit = QAction('Exit')

        self.fileMenu.addAction(self.fileActionNew)
        self.fileMenu.addAction(self.fileActionOpen)
        self.fileMenu.addAction(self.fileActionImport)
        self.fileMenu.addAction(self.fileActionImportFolder)
        self.fileMenu.addAction(self.fileActionSave)
        self.fileMenu.addAction(self.fileActionSaveAs)
        self.fileMenu.addAction(self.fileActionClose)
        self.fileMenu.addAction(self.fileActionExit)

        # self.fileActionImportFolder.triggered.connect(self.openImageFiles)
        #============================================================
        #EDIT MENU ACTIONS

        #============================================================
        #HELP MENU ACTIONS

        #============================================================
        #============================================================
        self.mainMenuBar = qtw.QMenuBar()
        self.mainMenuBar.addMenu(self.fileMenu)
        self.mainMenuBar.addMenu('Edit')
        self.mainMenuBar.addMenu('Help')
        self.setMenuBar(self.mainMenuBar)
        
        #============================================================
        #GROUPS & LAYOUTS
        self.mainGroup = qgb('')
        self.mainGroup.setLayout(qvl())
        self.mainContentGroup = qgb('')
        self.mainContentGroup.setLayout(qhl())
        #============================================================
        
        self.mcgl = self.mainContentGroup.layout()
        self.mgl = self.mainGroup.layout()
        self.setLayoutSettings(self.mcgl)
        self.setLayoutSettings(self.mgl)

        self.mainProgressBar = qtw.QProgressBar(parent=self.mainGroup)

        self.mgl.addWidget(self.mainContentGroup)
        self.mgl.addWidget(self.mainProgressBar)

        self.textEditor = TextEditor(self)
        self.fileList = FileList(self)

        self.mcgl.addWidget(self.fileList)
        self.mcgl.addWidget(self.textEditor)
        self.setCentralWidget(self.mainGroup)
        #SIGNALS
        self.fileList.sendItemData.connect(self.itemInListChanged)
        self.fileList.addImages.connect(self.openImageFiles)
        # self.fileList.removeImages.connect()
        #============================================================
        

    def openImageFiles(self):
        self.mainProgressBar.setValue(self.mainProgressBar.minimum())
        self.path = qtw.QFileDialog.getExistingDirectory(self, 'Select Folder')
        self.filePathList = [os.path.join(self.path, file) for file in os.listdir(self.path) if any(file.endswith(ext) for ext in self.imageExtensions)]
        self.mainProgressBar.setMaximum(len(self.filePathList))
        self.mainProgressBar.setFormat("Processing Images %v/%m")
        for item in self.filePathList:
            MPB_Value = self.mainProgressBar.value()
            fileData = self.createFileData(item)
            self.fileList.addItem(fileData)
            self.updateProgressBarValue(MPB_Value + 1)

    def createFileData(self, item:str):
        fileData = {
            'path': item,
            'filename': self.getBasenameWithExtension(item),
            'text' : self.convertToText(item),
            'savePath' : os.path.splitext(item)[0] + self.saveExtension
        }
        return fileData
        

    def addFileDataToList(self, fileData:dict):
        self.fileList.addItem(fileData)
        # self.saveFilePathList = [os.path.splitext(os.path.join(self.path, file))[0] + '.txt' for file in os.listdir(self.path) if any(file.endswith(ext) for ext in self.imageExtensions)]
        # print(self.saveFilePathList)

    def updateProgressBarValue(self, value:int):
        self.mainProgressBar.setValue(value)
        
    def getBasenameWithExtension(self, pathToFile):
        return os.path.basename(pathToFile)

    def convertToText(self, filePath):
        conf = r'--psm 6 --oem 3'
        langIndex = 1
        language = 'eng' if langIndex == 0 else 'slv' if langIndex == 1 else 'mkd' if langIndex == 2 else 'eng'
        # self.mainProgressBar.setValue(self.mainProgressBar.minimum())
        text = pytesseract.image_to_string(PIL.Image.open(filePath), lang=language, config=conf)
        return text


    def itemInListChanged(self, item:FileItem):
        self.textEditor.changeText(item.text)  
    
    def saveToFile(self, filePath, fileType):
        text = pytesseract.image_to_string(PIL.Image.open(self.filePathList[i]), lang=language, config=conf)
        with open(filePath, 'w+') as fh:
            fh.write(text)
            fh.close()
    
    def setLayoutSettings(self, layout:qtw.QLayout):
        layout.setContentsMargins(0,1,0,1)
        layout.setSpacing(0)




app = qtw.QApplication(sys.argv)

window = MyApp()
window.show()



app.exec()

