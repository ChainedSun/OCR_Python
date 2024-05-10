
from PyQt6 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg
from PyQt6.QtCore import pyqtSignal as Signal
from PyQt6.QtGui import QIcon




class FileItem(qtw.QWidget):
    checked = Signal(qtw.QWidget)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('FileItem')
        self.icon_Add = QIcon('icons/icons_controls_white_0.png')
        self.icon_Remove = QIcon('icons/icons_controls_white_1.png')
        self.icon_Edit = QIcon('icons/icons_controls_white_2.png')
        self.icon_Confirm = QIcon('icons/icons_controls_white_3.png')

        self.filenameBtn = qtw.QPushButton()
        self.filenameBtn.setCheckable(True)
        self.filenameBtn.clicked.connect(self.onCheck)
        self.filenameBtn.setObjectName('FileItemButton')
        self.filenameBtn.setMinimumHeight(24)

        self.mainLayout = qtw.QHBoxLayout()
        self.setLayout(self.mainLayout)
        self.filenameLineEdit = qtw.QLineEdit()
        self.editFilenameBtn = qtw.QPushButton(icon=self.icon_Edit)
        self.acceptEdit = qtw.QPushButton(icon=self.icon_Confirm)
        self.cancelEdit = qtw.QPushButton(icon=self.icon_Remove)
        self.editFilenameBtn.setMaximumSize(qtc.QSize(24, 24))
        self.acceptEdit.setMaximumSize(qtc.QSize(24, 24))
        self.cancelEdit.setMaximumSize(qtc.QSize(24, 24))
        self.mainLayout.addWidget(self.filenameBtn)
        self.mainLayout.addWidget(self.filenameLineEdit)
        self.mainLayout.addWidget(self.editFilenameBtn)
        self.mainLayout.addWidget(self.acceptEdit)
        self.mainLayout.addWidget(self.cancelEdit)
        self.filenameLineEdit.setVisible(False)
        self.acceptEdit.setVisible(False)
        self.cancelEdit.setVisible(False)

        self.mainLayout.setContentsMargins(qtc.QMargins(1,0,1,0))
        self.mainLayout.setSpacing(2)

        self.filenameLineEdit.setMinimumHeight(24)

        #SIGNALS
        self.editFilenameBtn.clicked.connect(self.editFilename)
        self.acceptEdit.clicked.connect(self.acceptEditFilename)
        self.cancelEdit.clicked.connect(self.rejectEditFilename)
        #======================================
        #EVENTS
        
        
        
    def editFilename(self):
        self.toggleEiting()
        self.filenameLineEdit.selectAll()
        self.filenameLineEdit.setFocus()
    
    def acceptEditFilename(self):
        self.toggleEiting()
        self.setFilename(self.filenameLineEdit.text())
    
    def rejectEditFilename(self):
        self.toggleEiting()
        self.filenameLineEdit.setText(self.filename)

    def toggleEiting(self):
        self.filenameBtn.setVisible(not self.filenameBtn.isVisible())
        self.editFilenameBtn.setVisible(not self.editFilenameBtn.isVisible())
        self.filenameLineEdit.setVisible(not self.filenameLineEdit.isVisible())
        self.acceptEdit.setVisible(not self.acceptEdit.isVisible())
        self.cancelEdit.setVisible(not self.cancelEdit.isVisible())

    def getData(self):
        if self.text:
            return self.text
        else:
            return f"Data doesn't exist or something went wrong!"
    
    def setData(self, data:dict={}):
        if not data:
            print(f"setData() failed, data is empty!")
            return
        self.data = data
        self.path = data['path']
        self.filename = data['filename']
        self.saveFilename = data['filename']
        self.text = data['text']
        self.index = data['index']
        self.savePath = data['savePath']
        self.filenameBtn.setText(self.filename)
        self.filenameLineEdit.setText(self.filename)
    
    def setFilename(self, nameValue:str):
        if nameValue:
            self.filename = nameValue
            self.filenameBtn.setText(nameValue)

    def changeSaveFilename(self, name:str=''):
        if name:
            self.filename, self.saveFilename = name
            self.filenameBtn.setText(name)

    def onCheck(self):
        if self.filenameBtn.isChecked():
            self.checked.emit(self)
    
        


