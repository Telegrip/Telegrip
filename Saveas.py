from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import sqlite3

from PyQt5.QtWidgets import QMainWindow, QMessageBox
from passlib.hash import pbkdf2_sha256
from passlib.hash import sha256_crypt
import re
import os
import shutil
import zipfile
import pyzipper

class nameCase(object):

    def __init__(self,nameFlag,protected):
        self.nameFlag=nameFlag
        self.protected=protected

class Ui_Saveas(QMainWindow):



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
        self.pushButton_4.clicked.connect(self.SaveCase)
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

        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(30, 200, 461, 171))
        self.frame.setStyleSheet("background-color: rgb(187, 227, 227);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 90, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(190, 20, 251, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textPass = QtWidgets.QLineEdit(self.frame)
        self.textPass.setGeometry(190, 80, 251, 31)
        self.textPass.setPlaceholderText("Password")
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)

        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(30, 60, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(7)

        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")


        self.textEdit_4 = QtWidgets.QTextEdit(self.frame)
        self.textEdit_4.setGeometry(QtCore.QRect(190, 125, 251, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(227, 243, 241);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.verticalScrollBar().setSliderPosition(0)
        self.textEdit_4.setReadOnly(True)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def closewindo(self):
        self.close()

    def retranslateUi(self, Saveas):
        _translate = QtCore.QCoreApplication.translate
        Saveas.setWindowTitle(_translate("Saveas", "Save as"))
        self.pushButton_4.setText(_translate("Saveas", "OK"))
        self.pushButton_5.setText(_translate("Saveas", "Cancel"))
        self.label_2.setText(_translate("Saveas", "File name"))
        self.label_4.setText(_translate("Saveas", "Password"))
        self.checkBox.setText(_translate("Saveas", "Protected"))
        self.label_5.setText(_translate("Saveas", "Path"))




    import resources2
    def createConnection(self):

        connection = mysql.connector.connect(
            host="localhost",
            database="telegrip",
            user="root",
            passwd="123456",
            auth_plugin='mysql_native_password'


        )

        return connection

    def SaveCase(self):

        found2=False
        completed=False
        Datalist=[]
        connection = self.createConnection()
        cursor = connection.cursor()
        Query1 = "SELECT casename FROM auth;"
        cursor.execute(Query1)
        names = cursor.fetchall()

        CaseName = self.textEdit.toPlainText()
        CaseName= CaseName.lower()
        CasePass = self.textPass.text()
        repeated = True
        QueryTy = 0
        regexp = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if (regexp.search(CaseName) or (regexp.search(CasePass))):
            self.SpecialCaseMessage()




        else:

            Repeated = False
            Query1 = "SELECT casename FROM auth;"
            cursor.execute(Query1)
            names = cursor.fetchall()

            for n in names:

                print(n[0])

                if (n[0] == CaseName):

                    Repeated = True

                    break
                    

                else:
                    continue

            if Repeated == False:

                     if(self.checkBox.isChecked() and len(CaseName)!=0): #protected flow
                        if (len(CasePass) != 0 and len(CasePass)>=8) :
                             dir = os.getcwd()
                             work_dir = os.path.join(dir, 'dump')
                             work_dir2 = os.path.join(dir, CaseName)

                             print(work_dir)

                             found = False
                             for x in os.walk(dir):
                                 print(x[0])
                                 if x[0] == work_dir:

                                     found = True
                                     break


                                 else:
                                     continue



                             if found == True:
                                  protected = "True"
                                  CasePass = sha256_crypt.hash(CasePass)
                                  query3 = "INSERT INTO auth (casename,password) VALUES(%s,%s)"
                                  entr=(CaseName,CasePass)
                                  cursor.execute(query3,entr)
                                  connection.commit()
                                  dirt=os.getcwd()
                                  name=CaseName
                                  nameFlag=name


                                  Current_dir=os.path.join(dirt,name)
                                  print(Current_dir)

                                  folder_path = os.path.join(dirt, 'dump')
                                  output_path = os.getcwd() + '\\'+name+'.zip'
                                  print(folder_path)

                                  self.checkBox=self.zip_folderPyzipper(folder_path,output_path,name )

                                  delt= name+'.zip'
                                  print(delt)
                                  shutil.copystat('dump', name+'.zip', follow_symlinks=True)
                                  shutil.rmtree('dump') 

                                  self.textEdit_4 = self.textEdit_4.setText(Current_dir)
                                  completed = True
                             elif found == False:

                                  print(work_dir2)

                                  for x in os.walk(dir):
                                      print(x[0])
                                      if x[0] == work_dir2:

                                          found2 = True
                                          if found2 == True:
                                              self.PathnotExists()
                                              break
                                      else:
                                          continue
                                  if found2 == False:

                                    self.DumpnotExists()
                             

                        else:
                             self.PassPolicy()
                            



                     elif (self.checkBox.isChecked()==True and len(CasePass) == 0):  
                              self.EnterPass()

                     elif (self.checkBox.isChecked()==False and len(CasePass) == 0):
                         dir = os.getcwd()
                         work_dir = os.path.join(dir, 'dump')
                         work_dir2 = os.path.join(dir, CaseName)



                         print(work_dir)

                         found = False
                         for x in os.walk(dir):
                             print(x[0])
                             if x[0] == work_dir:

                                 found = True
                                 break


                             else:
                                 continue



                         if found == True:

                             query3 = "INSERT INTO auth (casename,password) VALUES(%s,%s)"
                             entr = (CaseName,"null")
                             cursor.execute(query3, entr)
                             connection.commit()

                             dirt = os.getcwd()
                             case=os.rename('dump',CaseName)
                             Current_dir = os.path.join(dirt, CaseName)

                             self.textEdit_4 = self.textEdit_4.setText(Current_dir)
                             completed = True
                            
                         elif found==False:



                             for x in os.walk(dir):

                                 if x[0] == work_dir2:

                                     found2 = True
                                     if found2==True:
                                      self.PathnotExists()
                                      break
                                 else:
                                     continue
                             if found2==False:

                                  self.DumpnotExists()
                             

                     else:
                           self.Unchecked()
                          
            else:
             self.Repeated()

        if completed ==True:
            msg = QMessageBox()
            msg.setWindowTitle("Save as")
            msg.setText("Case has been saved successfully")
            msg.exec_()
            self.closewindo()















    def PassPolicy(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(" Password policy")
        msg.setText("Please, Make sure password length grater than or equal 8 character")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    def Unchecked(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Unprotected Case")
        msg.setText("Sorry, you must check the checkbox to enter the password ")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    def FieldsEmpty(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Empty Fields")
        msg.setText("Sorry, you must enter Case name")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    def CaseandPassEmpty(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Empty Fields")
        msg.setText("Sorry, you must enter Case name and Password")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()


    def Repeated(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Case name already exists")
        msg.setText("Please, change the case name")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    def EnterPass(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Enter Password")
        msg.setText("Please, enter the file password")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()


    def SpecialCaseMessage(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("No special charachters are allowed")
        msg.setText("Please, no special charachters")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()

    def FieldsEmpty(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Empty Fields")
        msg.setText("Sorry, you must set the Case name and Case password values")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()



    def zip_folderPyzipper(self,folder_path, output_path,name):  # add the cache4.db

       dir=os.getcwd()
       work_dir=os.path.join(dir,'dump')

       print(work_dir)

       found=False
       for x in os.walk(dir):
        print(x[0])
        if x[0]== work_dir:

           found=True
           break


        else:
            continue
       print("fter loop")
       print(found)

       if found==True:

            parent_folder = os.path.dirname(folder_path)
            contents = os.walk(folder_path)
            try:

                zip_file = pyzipper.AESZipFile(name+'.zip', 'w', compression=pyzipper.ZIP_DEFLATED,
                                               encryption=pyzipper.WZ_AES)
                zip_file.pwd = b'PASSWORD'
                for root, folders, files in contents:

                    for folder_name in folders:
                        absolute_path = os.path.join(root, folder_name)
                        relative_path = absolute_path.replace(parent_folder + '\\',
                                                              '')
                        print("Adding '%s' to archive." % absolute_path)
                        zip_file.write(absolute_path, relative_path)
                    for file_name in files:
                        absolute_path = os.path.join(root, file_name)
                        relative_path = absolute_path.replace(parent_folder + '\\',
                                                              '')
                        print("Adding '%s' to archive." % absolute_path)
                        zip_file.write(absolute_path, relative_path)

                print("'%s' created successfully." % output_path)


            except OSError as message:
                print(message)
                sys.exit(1)
            except zipfile.BadZipfile as message:
                print(message)

            finally:
                zip_file.close()

       else:
           self.PathnotExists()




    def PathnotExists(self):
              msg = QtWidgets.QMessageBox()
              msg.setWindowTitle("Path does not exist ")
              msg.setText("Sorry, The case is already saved")
              msg.setIcon(QtWidgets.QMessageBox.Information)
              x = msg.exec_()

    def DumpnotExists(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Dump does not exist ")
        msg.setText("Please create device image")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Saveas()
    ui.setupUi()
    ui.setWindowFlags(ui.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)  
    ui.show()
    sys.exit(app.exec_())
