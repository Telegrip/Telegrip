import os
from subprocess import check_output
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QMainWindow


class Ui_Creating(QMainWindow):

    def __init__(self):
        super().__init__()

    def Imaging(self):


        #Check prerequisites
        j = 0
        while j < 50:
         j+= 0.0001
         self.progressBar.setValue(j)

        if os.path.exists("C:\Telegrip-platform-tools") == False:
            url = 'https://dl.google.com/android/repository/platform-tools-latest-windows.zip'
            with urlopen(url) as zipresp:
                with ZipFile(BytesIO(zipresp.read())) as zfile:
                    zfile.extractall('C:\Telegrip-platform-tools')

        while j < 75:
         j+= 0.0001
         self.progressBar.setValue(j)

        #Check connectivity

        adb_output = check_output(["C:\Telegrip-platform-tools/platform-tools/adb", "devices"])
        while j < 100:
         j+= 0.0001
         self.progressBar.setValue(j)

        msg = QMessageBox()
        msg.setWindowTitle("Device status")
        if len(adb_output) > 35:
            msg.setText("Device is connected successfully")
            msg.exec_()

            i = 0
            while i < 25:
                i += 0.0001
                self.progressBar1.setValue(i)

            while i < 45:
                i += 0.0001
                self.progressBar1.setValue(i)

            # Imaging

            os.system("C:\Telegrip-platform-tools/platform-tools/adb pull /sdcard/Telegram dump")

            while i < 65:
                i += 0.0001
                self.progressBar1.setValue(i)

            os.system("C:\Telegrip-platform-tools/platform-tools/adb pull /storage/emulated/0/android/data/org.telegram.messenger/cache dump")

            while i < 75:
                i += 0.0001
                self.progressBar1.setValue(i)

            os.system("C:\Telegrip-platform-tools/platform-tools/adb shell su -c cp /data/data/org.telegram.messenger/files/cache4.db /sdcard/cache4.db")

            while i < 85:
                i += 0.0001
                self.progressBar1.setValue(i)

            os.system("C:\Telegrip-platform-tools/platform-tools/adb pull /sdcard/cache4.db dump")


            while i < 100:
                i += 0.0001
                self.progressBar1.setValue(i)

            msg.setText("Image has been created successfully")
            msg.exec_()
            self.closewindo()

        else:
            msg.setText("Device is not connected, try to reconnect it again ")
            msg.exec_()
            self.closewindo()











    def setupUi(self):
        self.setObjectName("self")
        self.resize(483, 284)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/icons/Picture1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"")
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 461, 261))
        self.frame_2.setStyleSheet("background-color: rgb(227, 243, 241);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar.setGeometry(QtCore.QRect(90, 130, 321, 21))
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setToolTip("Checking device connectivity")

        self.progressBar1 = QtWidgets.QProgressBar(self.frame_2)
        self.progressBar1.setGeometry(QtCore.QRect(90, 180, 321, 21))
        self.progressBar1.setObjectName("progressBar")
        self.progressBar1.setToolTip("Imaging")





        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(140, 50, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(self.frame_2)
        self.label2.setGeometry(QtCore.QRect(150, 110, 300, 16))
        self.label2.setObjectName("connectivity")
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label2.raise_()

        self.label3 = QtWidgets.QLabel(self.frame_2)
        self.label3.setGeometry(QtCore.QRect(190, 160, 300, 16))
        self.label3.setObjectName("Imaging")
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.label3.setFont(font)
        self.label3.setObjectName("label2")
        self.label3.raise_()



        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(160, 215, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(8)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_5.setStyleSheet("QPushButton::hover"
                             "{"
                             "background-color : rgb(232, 232, 232);"
                             "}"
                                      
                             "QPushButton"
                             "{"
                             "border-style:outset;\n"
                             "border-color:white;\n"
                             "border-width:2px;\n"
                             "border-radius:10px;\n"
                             "background-color: rgb(248, 248, 248);\n"
                            "}"
                                      
                            "QPushButton::pressed"
                            "{"
                            "background-color : gray;"
                            "}")
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_5.clicked.connect(self.Imaging)




        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def closewindo(self):
        self.close()

    def retranslateUi(self, Creating):
        _translate = QtCore.QCoreApplication.translate
        Creating.setWindowTitle(_translate("Creating", "Creating device Image"))
        self.label.setText(_translate("Creating", "Creating Device Image"))
        self.label2.setText(_translate("Creating", "Checking device connectivity:"))
        self.label3.setText(_translate("Creating", "Imaging process:"))
        self.pushButton_5.setText(_translate("Creating", "Start imaging"))
        self.label2.adjustSize()
        self.label3.adjustSize()


import resources2


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #Creating = QtWidgets.QWidget()
    ui = Ui_Creating()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())
