from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addToCase(object):
    def setupUi(self, addToCase):
        addToCase.setObjectName("addToCase")
        addToCase.resize(535, 272)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/new_copy_40px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addToCase.setWindowIcon(icon)
        addToCase.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"")
        self.AddToCase = QtWidgets.QFrame(addToCase)
        self.AddToCase.setGeometry(QtCore.QRect(10, 10, 511, 251))
        self.AddToCase.setStyleSheet("background-color: rgb(227, 243, 241);")
        self.AddToCase.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AddToCase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AddToCase.setObjectName("AddToCase")
        self.pushButton_4 = QtWidgets.QPushButton(self.AddToCase)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 220, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-color:gray;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.AddToCase)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 220, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style:outset;\n"
"border-color:gray;\n"
"border-width:2px;\n"
"border-radius:10px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.frame = QtWidgets.QFrame(self.AddToCase)
        self.frame.setGeometry(QtCore.QRect(30, 30, 461, 171))
        self.frame.setStyleSheet("background-color: rgb(187, 227, 227);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 10, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 50, 421, 101))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(addToCase)
        QtCore.QMetaObject.connectSlotsByName(addToCase)

    def retranslateUi(self, addToCase):
        _translate = QtCore.QCoreApplication.translate
        addToCase.setWindowTitle(_translate("addToCase", "Add to case"))
        self.pushButton_4.setText(_translate("addToCase", "Ok"))
        self.pushButton_5.setText(_translate("addToCase", "Cancel"))
        self.label_2.setText(_translate("addToCase", "Comments"))
import resources2


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    addToCase = QtWidgets.QWidget()
    ui = Ui_addToCase()
    ui.setupUi(addToCase)
    addToCase.show()
    sys.exit(app.exec_())
