# Form implementation generated from reading ui file 'text_editor.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGroupBox as qgb


class TextEditor(qgb):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.changingFormating:bool = False
        self.setObjectName("TextEditor")
        self.verticalLayout = qtw.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(2, 0, 2, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = qtw.QGroupBox(parent=self)
        sizePolicy = qtw.QSizePolicy(qtw.QSizePolicy.Policy.Fixed, qtw.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = qtw.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = qtw.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fontSelectionMenu = qtw.QFontComboBox(parent=self.groupBox)
        self.fontSelectionMenu.setObjectName("fontSelectionMenu")
        self.fontSelectionMenu.setFocusPolicy(qtc.Qt.FocusPolicy.ClickFocus)
        self.horizontalLayout_3.addWidget(self.fontSelectionMenu)
        self.fontSize = qtw.QSpinBox(parent=self.groupBox)
        self.fontSize.setMinimum(6)
        self.fontSize.setMaximum(128)
        self.fontSize.setSingleStep(2)
        self.fontSize.setProperty("value", 10)
        self.fontSize.setObjectName("fontSize")
        self.horizontalLayout_3.addWidget(self.fontSize)
        self.textLayout_0 = qtw.QHBoxLayout()
        self.textLayout_0.setSpacing(6)
        self.textLayout_0.setObjectName("textLayout_0")
        self.textBoldBtn = qtw.QPushButton(parent=self.groupBox)
        self.textBoldBtn.setMaximumSize(qtc.QSize(24, 16777215))
        self.textBoldBtn.setText("")
        icon = qtg.QIcon.fromTheme("format-text-bold")
        self.textBoldBtn.setIcon(icon)
        self.textBoldBtn.setCheckable(True)
        self.textBoldBtn.setObjectName("textBoldBtn")
        self.textLayout_0.addWidget(self.textBoldBtn)
        self.textItalicBtn = qtw.QPushButton(parent=self.groupBox)
        self.textItalicBtn.setMaximumSize(qtc.QSize(24, 16777215))
        self.textItalicBtn.setText("")
        icon = qtg.QIcon.fromTheme("format-text-italic")
        self.textItalicBtn.setIcon(icon)
        self.textItalicBtn.setCheckable(True)
        self.textItalicBtn.setObjectName("textItalicBtn")
        self.textLayout_0.addWidget(self.textItalicBtn)
        self.textUnderlineBtn = qtw.QPushButton(parent=self.groupBox)
        self.textUnderlineBtn.setMaximumSize(qtc.QSize(24, 16777215))
        self.textUnderlineBtn.setText("")
        icon = qtg.QIcon.fromTheme("format-text-underline")
        self.textUnderlineBtn.setIcon(icon)
        self.textUnderlineBtn.setCheckable(True)
        self.textUnderlineBtn.setObjectName("textUnderlineBtn")
        self.textLayout_0.addWidget(self.textUnderlineBtn)
        self.textStrikeBtn = qtw.QPushButton(parent=self.groupBox)
        self.textStrikeBtn.setMaximumSize(qtc.QSize(24, 16777215))
        self.textStrikeBtn.setText("")
        icon = qtg.QIcon.fromTheme("format-text-strikethrough")
        self.textStrikeBtn.setIcon(icon)
        self.textStrikeBtn.setCheckable(True)
        self.textStrikeBtn.setObjectName("textStrikeBtn")
        self.textLayout_0.addWidget(self.textStrikeBtn)
        # self.textColorLayout = qtw.QHBoxLayout()
        # self.textColorLayout.setSpacing(0)
        # self.textColorLayout.setObjectName("textColorLayout")
        # self.colorBtn = qtw.QPushButton(parent=self.groupBox)
        # self.colorBtn.setText("")
        # self.colorBtn.setObjectName("colorBtn")
        # self.textColorLayout.addWidget(self.colorBtn)
        # self.selectColorBtn = qtw.QComboBox(parent=self.groupBox)
        # self.selectColorBtn.setMaximumSize(qtc.QSize(16, 16777215))
        # self.selectColorBtn.setEditable(False)
        # self.selectColorBtn.setFrame(False)
        # self.selectColorBtn.setObjectName("selectColorBtn")
        # self.textColorLayout.addWidget(self.selectColorBtn)
        # self.textLayout_0.addLayout(self.textColorLayout)
        # self.textColorBgLayout = qtw.QHBoxLayout()
        # self.textColorBgLayout.setContentsMargins(0, -1, 0, -1)
        # self.textColorBgLayout.setSpacing(0)
        # self.textColorBgLayout.setObjectName("textColorBgLayout")
        # self.textColorBgBtn = qtw.QPushButton(parent=self.groupBox)
        # self.textColorBgBtn.setText("")
        # self.textColorBgBtn.setObjectName("textColorBgBtn")
        # self.textColorBgLayout.addWidget(self.textColorBgBtn)
        # self.comboBox = qtw.QComboBox(parent=self.groupBox)
        # self.comboBox.setMaximumSize(qtc.QSize(16, 16777215))
        # self.comboBox.setFrame(False)
        # self.comboBox.setObjectName("comboBox")
        # self.textColorBgLayout.addWidget(self.comboBox)
        # self.textLayout_0.addLayout(self.textColorBgLayout)
        self.horizontalLayout_3.addLayout(self.textLayout_0)
        self.textLayout_1 = qtw.QHBoxLayout()
        self.textLayout_1.setSpacing(6)
        self.textLayout_1.setObjectName("textLayout_1")
        # self.textAlignLeftBtn = qtw.QPushButton(parent=self.groupBox)
        # self.textAlignLeftBtn.setMaximumSize(qtc.QSize(24, 16777215))
        # self.textAlignLeftBtn.setText("")
        # icon = qtg.QIcon.fromTheme("format-justify-left")
        # self.textAlignLeftBtn.setIcon(icon)
        # self.textAlignLeftBtn.setCheckable(True)
        # self.textAlignLeftBtn.setObjectName("textAlignLeftBtn")
        # self.textLayout_1.addWidget(self.textAlignLeftBtn)
        # self.textAlignCenterBtn = qtw.QPushButton(parent=self.groupBox)
        # self.textAlignCenterBtn.setMaximumSize(qtc.QSize(24, 16777215))
        # self.textAlignCenterBtn.setText("")
        # icon = qtg.QIcon.fromTheme("format-justify-center")
        # self.textAlignCenterBtn.setIcon(icon)
        # self.textAlignCenterBtn.setCheckable(True)
        # self.textAlignCenterBtn.setObjectName("textAlignCenterBtn")
        # self.textLayout_1.addWidget(self.textAlignCenterBtn)
        # self.textAlignRightBtn = qtw.QPushButton(parent=self.groupBox)
        # self.textAlignRightBtn.setMaximumSize(qtc.QSize(24, 16777215))
        # self.textAlignRightBtn.setText("")
        # icon = qtg.QIcon.fromTheme("format-justify-right")
        # self.textAlignRightBtn.setIcon(icon)
        # self.textAlignRightBtn.setCheckable(True)
        # self.textAlignRightBtn.setObjectName("textAlignRightBtn")
        # self.textLayout_1.addWidget(self.textAlignRightBtn)
        # self.textAlignFillBtn = qtw.QPushButton(parent=self.groupBox)
        # self.textAlignFillBtn.setMaximumSize(qtc.QSize(24, 16777215))
        # self.textAlignFillBtn.setText("")
        # icon = qtg.QIcon.fromTheme("format-justify-fill")
        # self.textAlignFillBtn.setIcon(icon)
        # self.textAlignFillBtn.setCheckable(True)
        # self.textAlignFillBtn.setChecked(True)
        # self.textAlignFillBtn.setObjectName("textAlignFillBtn")
        # self.textLayout_1.addWidget(self.textAlignFillBtn)
        self.horizontalLayout_3.addLayout(self.textLayout_1)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.groupBox)
        self.textEdit = qtw.QTextEdit(parent=self)
        self.textEdit.setOverwriteMode(False)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)

        # self.textAlignLeftBtn.toggled.connect(lambda : self.changeTextOrientation(mode='l'))
        # self.textAlignCenterBtn.toggled.connect(lambda : self.changeTextOrientation(mode='c'))
        # self.textAlignRightBtn.toggled.connect(lambda : self.changeTextOrientation(mode='r'))
        # self.textAlignFillBtn.toggled.connect(self.changeTextOrientation)

        self.retranslateUi()
        qtc.QMetaObject.connectSlotsByName(self)

        self.fontSize.valueChanged.connect(self.changeFontSize)
        self.fontSelectionMenu.currentFontChanged.connect(self.changeFontStyle)

    def changeFontStyle(self):
        newFont = self.textEdit.font()
        newFont.setFamily(self.fontSelectionMenu.currentFont().family())
        self.textEdit.setFont(newFont)
        
    def changeFontSize(self):
        textFont = self.textEdit.font()
        textFont.setPointSize(self.fontSize.value())
        self.textEdit.setFont(textFont)

 

    def clearSelection(self):
        newTextCursor = self.textEdit.textCursor()
        newTextCursor.clearSelection()
        self.textEdit.setTextCursor(newTextCursor)

    def changeText(self, text:str):
        self.textEdit.setText(text)

    def setTextOrientation(self, mode='f'):
        fontNew = qtg.QFont()

    def retranslateUi(self):
        _translate = qtc.QCoreApplication.translate
        self.setWindowTitle(_translate("GroupBox", "GroupBox"))
        self.fontSize.setSuffix(_translate("GroupBox", "px"))

    # def changeTextOrientation(self, mode):
    #     leftState = self.textAlignLeftBtn.isChecked()
    #     centerState = self.textAlignCenterBtn.isChecked()
    #     rightState = self.textAlignRightBtn.isChecked()
    #     fillState = self.textAlignFillBtn.isChecked()

    #     if(not self.changingFormating):

    #         self.changingFormating = True
    #         aF = Qt.AlignmentFlag.AlignAbsolute
    #         if (mode == 'l' and leftState):
    #             self.textAlignCenterBtn.setChecked(False)
    #             self.textAlignRightBtn.setChecked(False)
    #             self.textAlignFillBtn.setChecked(False)
    #             aF = Qt.AlignmentFlag.AlignLeft
    #         elif (mode == 'c' and centerState):
    #             self.textAlignLeftBtn.setChecked(False)
    #             self.textAlignRightBtn.setChecked(False)
    #             self.textAlignFillBtn.setChecked(False)
    #             aF = Qt.AlignmentFlag.AlignCenter
    #         elif (mode == 'r' and rightState):
    #             self.textAlignLeftBtn.setChecked(False)
    #             self.textAlignCenterBtn.setChecked(False)
    #             self.textAlignFillBtn.setChecked(False)
    #             aF = Qt.AlignmentFlag.AlignRight
    #         else:
    #             self.textAlignLeftBtn.setChecked(False)
    #             self.textAlignCenterBtn.setChecked(False)
    #             self.textAlignRightBtn.setChecked(False)
    #             self.textAlignFillBtn.setChecked(True)

    #         self.textEdit.selectAll()
    #         self.textEdit.setAlignment(aF)
    #         self.changingFormating = False
    #         self.clearSelection()
