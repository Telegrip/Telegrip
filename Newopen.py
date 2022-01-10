from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QFileDialog, QMainWindow
import mysql.connector
import sqlite3
from passlib.hash import pbkdf2_sha256
from passlib.hash import sha256_crypt
from PyQt5.QtWidgets import ( QLineEdit,)
import os
import re
import shutil
from PyQt5.QtWidgets import QMainWindow, QMessageBox
import zipfile
import pyzipper
import mysql.connector



import cgitb
cgitb.enable(format = 'text')

class Ui_Newopen(QMainWindow):
    count =0
    wrongFlag = False
    maxFlag = False
    verified = False


    def __init__(self):
        super().__init__()

    def setupUi(self):

        self.setObjectName("self")
        self.resize(548, 439)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/new_copy_40px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(250, 250, 250);\n"
                           "")
        self.frame_2 = QtWidgets.QFrame(self)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 521, 411))
        self.frame_2.setStyleSheet("background-color: rgb(227, 243, 241);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(110, 10, 301, 181))
        self.label.setStyleSheet("image: url(:/image/icons/new .png);\n"
                                 "background-color: rgb(227, 243, 241);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 380, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButton_4.setStyleSheet("QPushButton::hover"
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 380, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
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
        self.pushButton_5.clicked.connect(self.closewindo)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_2)
        self.tabWidget.setGeometry(QtCore.QRect(30, 180, 471, 191))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_2.setGeometry(QtCore.QRect(180, 10, 251, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit = QtWidgets.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(180, 50, 251, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_3.setGeometry(QtCore.QRect(180, 90, 251, 31))
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.tab)
        self.dateEdit.setGeometry(QtCore.QRect(180, 130, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(30, 60, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(30, 100, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_4.setGeometry(QtCore.QRect(160, 20, 251, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textPass = QtWidgets.QLineEdit(self.tab_2)
        self.textPass.setGeometry(160, 60, 251, 31)
        self.textPass.setPlaceholderText("Password")
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(158, 105, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(227, 233, 230);")
        self.label_9.setObjectName("label_9")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_6.setGeometry(QtCore.QRect(160, 100, 251, 31))
        self.textEdit_6.setStyleSheet("background-color: rgb(227, 243, 241);")
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_6.verticalScrollBar().setSliderPosition(0)
        self.textEdit_6.setReadOnly(True)


        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def closewindo(self):
        self.close()

    def retranslateUi(self, Newopen):
        _translate = QtCore.QCoreApplication.translate
        Newopen.setWindowTitle(_translate("Newopen", "New/open case"))
        self.pushButton_4.setText(_translate("Newopen", "Ok"))
        self.pushButton_5.setText(_translate("Newopen", "Cancel"))
        self.label_5.setText(_translate("Newopen", "Date"))
        self.label_4.setText(_translate("Newopen", "Case description"))
        self.label_3.setText(_translate("Newopen", "Case name"))
        self.label_2.setText(_translate("Newopen", "Investigator name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Newopen", "New case"))
        self.label_6.setText(_translate("Newopen", "Case name"))
        self.label_7.setText(_translate("Newopen", "Password"))
        self.label_8.setText(_translate("Newopen","Case file"))
        self.pushButton_4.clicked.connect(self.OkPressed)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Newopen", "Open case"))
    import resources2

    #import resources2
    def createConnection(self):

        connection = mysql.connector.connect(
            host="localhost",
            database="telegrip",
            user="root",
            passwd="123456",
            auth_plugin='mysql_native_password'
        )
        return connection

    def OkPressed(self):

        


        if(self.tabWidget.currentIndex() == 0):

            self.NewCase()
            



        if (self.tabWidget.currentIndex() == 1):

            self.OpenCase()








    def createdcase(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("New Case")
        msg.setText("The case was created successfully ")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    def NewCase(self):

        Sflag = False
        connection = self.createConnection()
        CaseName = self.textEdit_2.toPlainText()
        InvestigatorName = self.textEdit.toPlainText()
        CaseDesc = self.textEdit_3.toPlainText()
        Date = self.dateEdit.date().toPyDate().strftime("%d, %b %Y")






        special_char = False
        regexp = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if (regexp.search(CaseName) or regexp.search(InvestigatorName) or regexp.search(CaseDesc)):
            Sflag = True
            self.SpecialCaseMessage()


        if((len(CaseName) >15 or len(CaseName) == 0) or (len(InvestigatorName) >15 or len(InvestigatorName) ==0) or  (len(CaseDesc) >140)):
            Sflag = True
            self.LenghthErrorPopUp()


        else:

            self.createdcase()

        if Sflag==False:
            from Main import Ui_MainWindow
            self.ui = Ui_MainWindow(CaseName, InvestigatorName, CaseDesc, Date)
            self.ui.setupUi()
            self.ui.setWindowFlags(self.ui.windowFlags() & QtCore.Qt.CustomizeWindowHint)
            self.ui.setWindowFlags(self.ui.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
            self.ui.show()
            self.close()

  






    def OpenCase(self):
        
        completed=False

        connection = self.createConnection()

        cursor = connection.cursor()
        CaseName = self.textEdit_4.toPlainText()

        CaseName = CaseName.lower()
        Query1 = "SELECT casename FROM auth;"
        cursor.execute(Query1)
        names = cursor.fetchall()
        print(names)
        checkName = False
        checkPass = False
        SpcialFlag=False
        print(CaseName)
        Pass=self.textPass.text()






        regexp = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        if (regexp.search(CaseName) or (regexp.search(Pass))):
            SpcialFlag=True

            self.SpecialCaseMessage() 


        if (len(CaseName) == 0 and len(Pass) == 0):
            SpcialFlag=True
            self.FieldsEmpty()


        if (len(CaseName) != 0 and len(Pass) != 0 and SpcialFlag==False):

            dir = os.getcwd()
            work_dir = os.path.join(dir, CaseName + '.zip')

            print(work_dir)

            found1 = False
            for x in os.listdir(dir):

                if x == CaseName + '.zip':

                    found1 = True

            if found1 == True:
                
                if names != None:
                    

                    for n in names:
                        print(n)
                        if CaseName == n[0]:


                            checkName = True
                            Query2 = "SELECT password FROM auth WHERE casename='" + CaseName + "'"
                            cursor.execute(Query2)
                            PasswordDB = cursor.fetchone()

                            dir = os.getcwd()
                            folder='\\'+CaseName+'.zip'
                            cur_dir = os.path.join(dir, CaseName + '.zip')
                            print(folder)

                            if (sha256_crypt.verify(Pass, PasswordDB[0])):
                                self.verified = True


                                checkPass = True
                                self.Unzip(CaseName)

                                os.remove(CaseName + '.zip')

                                print(cur_dir)
                                self.textEdit_6 = self.textEdit_6.setText(cur_dir)

                                completed=True
                            else:

                                self.wrongFlag=True


                        else:
                            continue
                            self.CaseNotexist()
                        
                else:
                    self.DBisEmpty()
            else:

                self.CaseNotexist()




            if self.wrongFlag == True:
                self.count += 1

                if self.count <= 3:
                     self.wrongPass()

                elif self.count > 3:
                     self.Maxx()
                     self.close()




        if (len(CaseName) != 0 and len(Pass) == 0 and  SpcialFlag==False): # not protected


            checkName = False
            checkp=False

            if names != None:
                for n in names:
                    if CaseName == n[0]:
                        checkName = True
                        Query4 = "SELECT password FROM auth WHERE casename='" + CaseName + "'"
                        cursor.execute(Query4)
                        PasswordDB = cursor.fetchone()

                        if PasswordDB[0]!='null':
                            checkp=True

                    else:
                        continue

                if checkName == True and checkp==False:

                    print(CaseName)
                    os.rename(CaseName, 'dump')
                    print("after rename")
                    dir = os.getcwd()
                    cur_dir = os.path.join(dir, CaseName + '.zip')
                    print(cur_dir)


                    self.textEdit_6 = self.textEdit_6.setText(cur_dir)
                    completed = True

                    
                elif checkName==True and checkp==True:
                  self.FieldsEmpty()
                else:
                    self.CaseNotexist()

            elif checkName==False:
                self.DBisEmpty()

        if completed==True:

            msg = QMessageBox()
            msg.setWindowTitle("Open")
            msg.setText("Case has been opened successfully")
            msg.exec_()
            self.closewindo()

            from Main import Ui_MainWindow
            self.ui = Ui_MainWindow(CaseName, "", "", "")
            self.ui.setupUi()
            self.ui.setWindowFlags(self.ui.windowFlags() & QtCore.Qt.CustomizeWindowHint)
            self.ui.setWindowFlags(self.ui.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
            self.ui.show()








    def Maxx(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Sorry ")
        msg.setText("You have exceeded the trial attempt")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()
    def wrongPass(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Wrong Password ")
        msg.setText("Sorry, the password entered is wrong please, try again")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    def CaseNotexist(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Case doesnt exist")
        msg.setText("Sorry, The case doesnt exist")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    def FieldsEmpty(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Empty Fields")
        msg.setText(" If the case is protected, you must set the Case name and Case password values. \n\n"
                    "Otherwise enter the Case name ")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    def Err(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Case Name or Password is not correct and make sure you are selecting the database")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    def DBisEmpty(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Empty Database")
        msg.setText("Sorry, the DataBase has no records")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()



    def SpecialCaseMessage(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("No special charachters are allowed")
        msg.setText("Please, no special characters")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()



    def PassErrorPopUp(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Please re-check the entries")
        msg.setText("Please re-check the entries ") 
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()









    def LenghthErrorPopUp(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Re-check the entries")
        msg.setText("Please ensure the length of the Case Name and Investigator Name \n are less than 15 charachters and does not equal 0\n\n The Case Description must be less than 140 charachters")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()
    




    def BrowseDb(self):
        
        filename = QFileDialog.getOpenFileName(None, 'Open Database', os.getcwd() #'c:\\'
                                               , 'SQLite DB file (*.db)')
        print(filename)
        self.textEdit_4.setText(filename[0])
        



  



    def Unzip(self,casename):
        print("inside unzip")
        pw = b'PASSWORD'
        output_path = os.getcwd() + "\\"+casename+".zip"
        print(output_path)
        x = os.getcwd()
        print(x)
        with pyzipper.AESZipFile(output_path)as zf:
            zf.setpassword(pw)
            zf.extractall(x)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Newopen()
    ui.setupUi()
    ui.setWindowFlags(ui.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)  
    ui.show()
    sys.exit(app.exec_())

