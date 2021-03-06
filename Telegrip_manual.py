
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Telegrip_manual(object):
    def setupUi(self, Telegrip_manual):
        Telegrip_manual.setObjectName("Telegrip_manual")
        Telegrip_manual.resize(644, 486)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Picture1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Telegrip_manual.setWindowIcon(icon)
        Telegrip_manual.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"")
        self.frame_2 = QtWidgets.QFrame(Telegrip_manual)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 621, 461))
        self.frame_2.setStyleSheet("background-color: rgb(227, 243, 241);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(160, 10, 331, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(227, 243, 241);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 30, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(-30, 10, 161, 111))
        self.label_2.setStyleSheet("image: url(:/newPrefix/icons/new .png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.label.raise_()
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 120, 601, 331))
        self.textBrowser.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Telegrip_manual)
        QtCore.QMetaObject.connectSlotsByName(Telegrip_manual)

    def retranslateUi(self, Telegrip_manual):
        _translate = QtCore.QCoreApplication.translate
        Telegrip_manual.setWindowTitle(_translate("Telegrip_manual", "Telegrip_manual"))
        self.label.setText(_translate("Telegrip_manual", "Telegrip Manual"))
        self.textBrowser.setHtml(_translate("Telegrip_manual", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">1- Enter case information in the first interface to start the investigation or open previously saved case.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">     -When opening the previous saved case, enter the password if the case is protected with a password.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">2- To obtain the device image, click on create device image button.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">             </span><img src=\":/newPrefix/icons/1.PNG\" /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">     - Make sure the device is connected, then click on start imaging button.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">     - The image will be created, and you can start your investigation.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">3- Click on and scroll through the evidence tree to analyze the image content.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            </span><img src=\":/newPrefix/icons/6.png\" /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">4- To add an evidence to the report, click on the check box near the evidence in interest.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">            </span><img src=\":/newPrefix/icons/5.PNG\" /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">     - Add comment if needed in the comment dialog box that appears after selecting the evidence.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">5- To generate the report, click on Generate report button.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">           </span><img src=\":/newPrefix/icons/3.PNG\" /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">     - The generated report will contain the selected evidence with their comments.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">     - Click on download button to download the report in pdf format.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">6- To save the case click on Save as button.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">         </span><img src=\":/newPrefix/icons/2.PNG\" /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">     - Enter the required information then click ok.</span><span style=\" font-size:10pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:10pt;\">     - To save the case with a protected password, select the &quot;protected &quot; check box.</span><span style=\" font-size:10pt;\"> </span></p></body></html>"))
import resources3


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Telegrip_manual = QtWidgets.QWidget()
    ui = Ui_Telegrip_manual()
    ui.setupUi(Telegrip_manual)
    Telegrip_manual.show()
    sys.exit(app.exec_())
