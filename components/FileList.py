
from PyQt6 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg
from PyQt6.QtWidgets import QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtCore import pyqtSignal as Signal
from components.FileListItem import FileItem

fakeData = {
    'path': 'fake/path',
    'filename': 'testName',
    'text': 'text text',
    'savePath': 'fake/save/path'
}


class FileList(qtw.QWidget):
    sendItemData = Signal(FileItem)
    addImages = Signal()
    removeImages = Signal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.itemList = []
        self.selectedItem = None
        self.setObjectName('FileList')
        self.selectedItem = None
        self.setSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        self.setMaximumWidth(320)

        self.mainLayout = qtw.QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.mainScrollArea = qtw.QScrollArea(self)
        self.mainScrollArea.setHorizontalScrollBarPolicy(qtc.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.mainScrollAreaLayout = qtw.QVBoxLayout()

        self.controlsWidget = qtw.QWidget(self)
        self.controlsWidget.setObjectName('ControlsWidget')
        self.controlsWidget.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.controlsLayout = qtw.QHBoxLayout()
        self.controlsWidget.setLayout(self.controlsLayout)
        self.mainLayout.addWidget(self.controlsWidget)
        self.mainLayout.addWidget(self.mainScrollArea)
        
        self.controlsAddImagesBtn = qtw.QPushButton(icon=qtg.QIcon("icons/icons_controls_white_0.png"))
        self.controlsRemoveImagesBtn = qtw.QPushButton(icon=qtg.QIcon("icons/icons_controls_white_1.png"))
        self.controlsSortFilesBtn = qtw.QPushButton()
        self.controlsAddImagesBtn.setMaximumWidth(24)
        self.controlsRemoveImagesBtn.setMaximumWidth(24)
        self.controlsSortFilesBtn.setMaximumWidth(24)
        self.controlsAddImagesBtn.setMaximumHeight(24)
        self.controlsRemoveImagesBtn.setMaximumHeight(24)
        self.controlsSortFilesBtn.setMaximumHeight(24)
        self.controlsLayout.addWidget(self.controlsAddImagesBtn)
        self.controlsLayout.addWidget(self.controlsRemoveImagesBtn)
        self.controlsLayout.addWidget(self.controlsSortFilesBtn)

        self.mainScrollArea.setLayout(self.mainScrollAreaLayout)
        self.mainScrollArea.setSizePolicy(qtw.QSizePolicy.Policy.MinimumExpanding, qtw.QSizePolicy.Policy.MinimumExpanding)
        self.mainScrollAreaItemListWidget = qtw.QWidget(self)
        self.mainScrollAreaItemListLayout = qtw.QVBoxLayout()
        self.mainScrollAreaItemListWidget.setLayout(self.mainScrollAreaItemListLayout)
        self.mainScrollAreaLayout.addWidget(self.mainScrollAreaItemListWidget)

        self.mainScrollAreaItemListWidget.setSizePolicy(qtw.QSizePolicy.Policy.MinimumExpanding, qtw.QSizePolicy.Policy.Fixed)
        self.mainScrollAreaLayout.setAlignment(qtc.Qt.AlignmentFlag.AlignTop)

        self.setLayoutSettings(self.mainScrollAreaLayout)
        self.mainScrollAreaItemListLayout.setContentsMargins(qtc.QMargins(1,2,1,2))
        self.setLayoutSettings(self.mainLayout)

        self.controlsAddImagesBtn.clicked.connect(lambda: self.addImages.emit())
        self.controlsRemoveImagesBtn.clicked.connect(lambda: self.removeImages.emit())
        self.addItem(data=fakeData)

    def addItem(self, data:dict={}):
        if not data:
            print(f"Data is empty! {data}")
            return
        for i in range(0, self.mainScrollAreaItemListLayout.count()):
            currentItem = self.mainScrollAreaItemListLayout.itemAt(i).widget()
            
            if currentItem.path == data['path']:
                return
            else:
                print(f"CurrentItem: {currentItem.filename}/data: {data['filename']}")
        itemIndex = self.mainScrollAreaItemListLayout.count()
        index = itemIndex if itemIndex >= 1 else 0
        data['index'] = index
        print(f"index:{index}/itemIndex:{itemIndex}")
        # print(data)
        item = FileItem()
        item.setData(data)
        item.checked.connect(self.itemSelected)
        self.mainScrollAreaItemListLayout.addWidget(item)

    def setLayoutSettings(self, layout:qtw.QLayout):
        layout.setContentsMargins(0,1,0,1)
        layout.setSpacing(0)

    def itemSelected(self, item):
        self.selectedItem = item
        for i in range(0, self.mainScrollAreaItemListLayout.count()):
            currItem = self.mainScrollAreaItemListLayout.itemAt(i).widget()
            if not item.index == currItem.index:
                currItem.filenameBtn.setChecked(False)
        self.sendItemData.emit(item)

    def updateItemName(self, itemName:str):
        if itemName:
            if self.selectedItem:
                self.selectedItem.filename = itemName

        return

        


