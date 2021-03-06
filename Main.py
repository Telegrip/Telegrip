#Built by: Norah Alkhathlan, Deema Almassary, Nourah Bin Fhaid, Sara Aldossary, and Rowida Bajuiffer
import os
import time
from pathlib import Path
from sqlite3 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QInputDialog, QMainWindow
from Creating import Ui_Creating
from Saveas import Ui_Saveas
from addToCase import Ui_addToCase
from generate_report import Ui_generate_report
from Newopen import Ui_Newopen
from Group import Group
from NormalChat import NormalChat
from channel import channel
from ParsingDoc import ParsingDoc
from ParsingImage import ParsingImage
from ParsingVideo import ParsingVideo
from Users import Users
from SecretChat import SecretChat
from GIf import GIF
from AUDIO import Audio
from ImageInfo import Imageinfo
from URL import ParsingUrl
from channelInfo import channelInfo
from GroupInfo import GroupInfo
from Telegrip_manual import Ui_Telegrip_manual
import hashlib
from userTracking import Track


class Report(object):

    def __init__(self, msgID, sendername, recivedname, timestamp, content, type, comment, filePath):
        self.msgID = msgID
        self.sendername = sendername
        self.recivedname = recivedname
        self.timestamp = timestamp
        self.content = content
        self.type = type
        self.comment = comment
        self.filePath = filePath


LastStateRole = QtCore.Qt.UserRole

global ReportList


class Ui_MainWindow(QMainWindow):
    ReportList = []
    type = ''
    casename = ''
    investigatorname = ""
    casedescription = ""
    devicename = ""
    androidversion = ""
    brand = ""
    model = ""
    country = ""
    hash = ""
    date = ""
    completed=False
    saved=False


    def __init__(self):
        super().__init__()




    def __init__(self, casename, investigatorname, casedescription, dated):
        super().__init__()
        self.casename = casename
        self.investigatorname = investigatorname
        self.casedescription = casedescription
        self.date = dated



    def cell_was_clicked(self, row, column):

        if column == 5:

            
            index = (self.tableWidgetFiles.selectionModel().currentIndex())
            value = index.sibling(index.row(), index.column()).data()

            Vid = ParsingVideo()
            list_sortedV = Vid.getData()
            for v in list_sortedV:
                if v.file == value:
                    os.startfile(v.Patth)

            Img = ParsingImage()
            list_sortedM = Img.getData()
            for i in list_sortedM:
                if i.file == value:
                    os.startfile(i.Patth)

            Doc = ParsingDoc()
            list_sortedD = Doc.getData()
            for d in list_sortedD:
                if d.file == value:
                    os.startfile(d.Patth)

            G = GIF()
            list2 = G.getData()
            for g in list2:
                if g.file == value:
                    os.startfile(g.Patth)

            Aud = Audio()
            list_sortedA = Aud.getData()
            for a in list_sortedA:
                if a.file == value:
                    os.startfile(a.Patth)

            U = ParsingUrl()
            listU = U.getData()
            for u in listU:
                if u.url == value:
                    # dont include https if found
                    if str(value).startswith("https://"):
                        os.system("start " + u.url)
                        value=''
                    else:
                      os.system("start \"\" https://" + u.url)
                      value = ''

    # open windows methods

    def openwindow(self):
        #self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Creating()
        self.ui.setupUi()
        self.ui.setWindowFlags(self.ui.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        self.ui.show()

        # open new/open interface methods

    def openwindow1(self):
        #self.window = QtWidgets.QMainWindow()

        x = Ui_Newopen()
        x.count = 0
        self.ui1 = Ui_Newopen()
        self.ui1.setupUi()
        self.ui1.setWindowFlags(self.ui1.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        self.ui1.show()
        self.close()

        # open saveas interface methods

    def openwindow2(self):
        #self.window = QtWidgets.QMainWindow()
        self.ui2 = Ui_Saveas()
        self.ui2.setupUi()
        self.ui2.setWindowFlags(self.ui2.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        self.ui2.show()
        self.saved=True



        # open addToCase interface methods

    def openwindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui3 = Ui_addToCase()
        self.ui3.setupUi(self.window)
        self.window.setWindowFlags(self.window.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        self.window.show()

        # # open addToCase interface methods
        # def openwindow5(self):
        #     self.window = QtWidgets.QMainWindow()
        #     self.ui5 = Ui_Newcase()
        #     self.ui5.setupUi(self.window)
        #     self.window.show()

        # generate report interface

    def openwindow6(self):
        if self.casename.endswith("\n"):
            self.casename=self.casename.rstrip("\n")
        f = open("dump/" + str(self.casename) + ".txt", "r")
        self.casename = f.readline()
        self.investigatorname = f.readline()
        self.casedescription = f.readline()
        self.date = f.readline()

        self.devicename = f.readline()
        self.androidversion = f.readline()
        self.brand = f.readline()
        self.model = f.readline()
        self.country = f.readline()

        f.close()

        #self.window = QtWidgets.QMainWindow()
        self.ui6 = Ui_generate_report(self.ReportList, self.casename, self.investigatorname, self.casedescription,
                                      self.devicename, self.androidversion, self.hash, self.date,
                                      self.brand, self.model, self.country)

        self.ui6.setupUi()
        self.ui6.setWindowFlags(self.ui6.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)#disable
        self.ui6.show()

    def openwindowme(self):
        self.window = QtWidgets.QMainWindow()
        self.ui3 = Ui_Telegrip_manual()
        self.ui3.setupUi(self.window)
        self.window.show()

    # srach based on button
    def search(self):
        self.fillTxt()

    # search based on the text filed
    def checkTxt(self):
        self.GetSecret_Search()
        self.GetNormal_Search()
        self.GetChannels_Search()
        self.GetGroups_Search()

    def GetSecret_Search(self):

        searchTxt = self.textEdit.toPlainText()
        if searchTxt == "" and self.type == "Secret chats":
            self.tableWidgetMessage.setRowCount(0)
            self.label_2.setText("Massages Table")
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetMessage.setHidden(False)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetMessage.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            sc = SecretChat()
            list_sorted = sc.getData()
            self.tableWidgetMessage.setColumnCount(7)
            self.tableWidgetMessage.setRowCount(len(list_sorted))
            row = 0
            for oj in list_sorted:
                if ("http" not in (oj.msg).lower()) and (oj.msg != ""):
                    item = QtWidgets.QTableWidgetItem()
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    item.setCheckState(QtCore.Qt.Unchecked)
                    item.setData(LastStateRole, item.checkState())
                    #self.tableWidgetMessage.insertRow(row)
                    self.tableWidgetMessage.setItem(row, 0, item)
                    self.tableWidgetMessage.setItem(row, 1, QTableWidgetItem(oj.msgID))
                    self.tableWidgetMessage.setItem(row, 2, QTableWidgetItem(oj.sendername))
                    self.tableWidgetMessage.setItem(row, 3, QTableWidgetItem(oj.recivedname))
                    self.tableWidgetMessage.setItem(row, 4, QTableWidgetItem(oj.timestamp))
                    self.tableWidgetMessage.setItem(row, 5, QTableWidgetItem(oj.msgsize))
                    self.tableWidgetMessage.setItem(row, 6, QTableWidgetItem(oj.msg))
                    row = row + 1
            self.tableWidgetMessage.cellChanged.connect(self.Message_Report)

        if searchTxt != "" and self.type == "Secret chats":
            self.tableWidgetMessage.setRowCount(0)
            self.label_2.setText("Massages Table")
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetMessage.setHidden(False)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetMessage.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            sc = SecretChat()
            list_sorted = sc.getData()
            self.tableWidgetMessage.setColumnCount(7)
            self.tableWidgetMessage.setRowCount(len(list_sorted))

            row = 0

            if self.radioButton_UserName.isChecked() == True:
                for oj in list_sorted:
                    if ("http" not in (oj.msg).lower()) and (oj.msg != "") and ((
                                                                                        (searchTxt).lower() in (
                                                                                        oj.sendername).lower()) or (
                                                                                        (searchTxt).lower() in (
                                                                                        oj.recivedname).lower())):
                        item = QtWidgets.QTableWidgetItem()
                        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item.setCheckState(QtCore.Qt.Unchecked)
                        item.setData(LastStateRole, item.checkState())
                        #self.tableWidgetMessage.insertRow(row)
                        self.tableWidgetMessage.setItem(row, 0, item)
                        self.tableWidgetMessage.setItem(row, 1, QTableWidgetItem(oj.msgID))
                        self.tableWidgetMessage.setItem(row, 2, QTableWidgetItem(oj.sendername))
                        self.tableWidgetMessage.setItem(row, 3, QTableWidgetItem(oj.recivedname))
                        self.tableWidgetMessage.setItem(row, 4, QTableWidgetItem(oj.timestamp))
                        self.tableWidgetMessage.setItem(row, 5, QTableWidgetItem(oj.msgsize))
                        self.tableWidgetMessage.setItem(row, 6, QTableWidgetItem(oj.msg))
                        row = row + 1
                self.tableWidgetMessage.cellChanged.connect(self.Message_Report)
            if self.radioButton_MsgContent.isChecked() == True:
                for oj in list_sorted:
                    if ("http" not in (oj.msg).lower()) and (oj.msg != "") and (searchTxt).lower() in (
                            oj.msg).lower():
                        item = QtWidgets.QTableWidgetItem()
                        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item.setCheckState(QtCore.Qt.Unchecked)
                        item.setData(LastStateRole, item.checkState())
                        self.tableWidgetMessage.setItem(row, 0, item)
                        self.tableWidgetMessage.setItem(row, 1, QTableWidgetItem(oj.msgID))
                        self.tableWidgetMessage.setItem(row, 2, QTableWidgetItem(oj.sendername))
                        self.tableWidgetMessage.setItem(row, 3, QTableWidgetItem(oj.recivedname))
                        self.tableWidgetMessage.setItem(row, 4, QTableWidgetItem(oj.timestamp))
                        self.tableWidgetMessage.setItem(row, 5, QTableWidgetItem(oj.msgsize))
                        self.tableWidgetMessage.setItem(row, 6, QTableWidgetItem(oj.msg))
                        row = row + 1
                self.tableWidgetMessage.cellChanged.connect(self.Message_Report)

    def GetGroups_Search(self):

        searchTxt = self.textEdit.toPlainText()
        if searchTxt == "" and self.type == "Groups":
            self.label_2.setText("Messages Table")
            self.tableWidgetGroups.setRowCount(0)
            self.tableWidgetMessage.setHidden(True)
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetGroups.setHidden(False)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetGChannelInfo.setHidden(True)
            self.tableWidgetGroupInfo.setHidden(True)
            self.tableWidgetUsers.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetGroups.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
            gr = Group()
            list_sorted = gr.getData()
            self.tableWidgetGroups.setColumnCount(7)
            self.tableWidgetGroups.setRowCount(len(list_sorted))
            row = 0
            for oj in list_sorted:
                if ("http" not in (oj.msg).lower()) and (oj.msg != ""  ) :
                    item = QtWidgets.QTableWidgetItem()
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    item.setCheckState(QtCore.Qt.Unchecked)
                    item.setData(LastStateRole, item.checkState())
                    #self.tableWidgetGroups.insertRow(row)
                    self.tableWidgetGroups.setItem(row, 0, item)
                    self.tableWidgetGroups.setItem(row, 1, QTableWidgetItem(oj.mid))
                    self.tableWidgetGroups.setItem(row, 2, QTableWidgetItem(oj.sender))
                    self.tableWidgetGroups.setItem(row, 3, QTableWidgetItem(oj.namef))
                    self.tableWidgetGroups.setItem(row, 4, QTableWidgetItem(oj.timestamp))
                    self.tableWidgetGroups.setItem(row, 5, QTableWidgetItem(oj.msgsize))
                    self.tableWidgetGroups.setItem(row, 6, QTableWidgetItem(oj.msg))
                    row = row + 1
            self.tableWidgetGroups.cellChanged.connect(self.Groups_Report)

        if searchTxt != "" and self.type == "Groups":
            self.label_2.setText("Messages Table")
            self.tableWidgetGroups.setRowCount(0)
            self.tableWidgetMessage.setHidden(True)
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetGroups.setHidden(False)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetGChannelInfo.setHidden(True)
            self.tableWidgetGroupInfo.setHidden(True)
            self.tableWidgetUsers.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetGroups.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
            gr = Group()
            list_sorted = gr.getData()
            self.tableWidgetGroups.setColumnCount(7)
            self.tableWidgetGroups.setRowCount(len(list_sorted))
            row = 0

            if self.radioButton_UserName.isChecked() == True:
                for oj in list_sorted:
                    if ("http" not in (oj.msg).lower()) and (oj.msg != "") and ((
                            (searchTxt).lower() in (
                            oj.sender).lower())):
                        item = QtWidgets.QTableWidgetItem()
                        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item.setCheckState(QtCore.Qt.Unchecked)
                        item.setData(LastStateRole, item.checkState())
                        #self.tableWidgetGroups.insertRow(row)
                        self.tableWidgetGroups.setItem(row, 0, item)
                        self.tableWidgetGroups.setItem(row, 1, QTableWidgetItem(oj.mid))
                        self.tableWidgetGroups.setItem(row, 2, QTableWidgetItem(oj.sender))
                        self.tableWidgetGroups.setItem(row, 3, QTableWidgetItem(oj.namef))
                        self.tableWidgetGroups.setItem(row, 4, QTableWidgetItem(oj.timestamp))
                        self.tableWidgetGroups.setItem(row, 5, QTableWidgetItem(oj.msgsize))
                        self.tableWidgetGroups.setItem(row, 6, QTableWidgetItem(oj.msg))
                        row = row + 1
                self.tableWidgetGroups.cellChanged.connect(self.Groups_Report)

            if self.radioButton_MsgContent.isChecked() == True:
                for oj in list_sorted:
                    if ("http" not in (oj.msg).lower()) and (oj.msg != "") and (searchTxt).lower() in (
                            oj.msg).lower():
                        item = QtWidgets.QTableWidgetItem()
                        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item.setCheckState(QtCore.Qt.Unchecked)
                        item.setData(LastStateRole, item.checkState())
                        self.tableWidgetGroups.setItem(row, 0, item)
                        self.tableWidgetGroups.setItem(row, 1, QTableWidgetItem(oj.mid))
                        self.tableWidgetGroups.setItem(row, 2, QTableWidgetItem(oj.sender))
                        self.tableWidgetGroups.setItem(row, 3, QTableWidgetItem(oj.namef))
                        self.tableWidgetGroups.setItem(row, 4, QTableWidgetItem(oj.timestamp))
                        self.tableWidgetGroups.setItem(row, 5, QTableWidgetItem(oj.msgsize))
                        self.tableWidgetGroups.setItem(row, 6, QTableWidgetItem(oj.msg))
                        row = row + 1
                self.tableWidgetGroups.cellChanged.connect(self.Groups_Report)

    def GetSecret_Search(self):

        searchTxt = self.textEdit.toPlainText()
        if searchTxt == "" and self.type == "Secret chats":
            self.tableWidgetMessage.setRowCount(0)
            self.label_2.setText("Massages Table")
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetMessage.setHidden(False)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetMessage.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
            sc = SecretChat()
            list_sorted = sc.getData()
            self.tableWidgetMessage.setColumnCount(7)
            self.tableWidgetMessage.setRowCount(len(list_sorted))
            row = 0
            for oj in list_sorted:
                if ("http" not in (oj.msg).lower()) and (oj.msg != ""):
                    item = QtWidgets.QTableWidgetItem()
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    item.setCheckState(QtCore.Qt.Unchecked)
                    item.setData(LastStateRole, item.checkState())
                    #self.tableWidgetMessage.insertRow(row)
                    self.tableWidgetMessage.setItem(row, 0, item)
                    self.tableWidgetMessage.setItem(row, 1, QTableWidgetItem(oj.msgID))
                    self.tableWidgetMessage.setItem(row, 2, QTableWidgetItem(oj.sendername))
                    self.tableWidgetMessage.setItem(row, 3, QTableWidgetItem(oj.recivedname))
                    self.tableWidgetMessage.setItem(row, 4, QTableWidgetItem(oj.timestamp))
                    self.tableWidgetMessage.setItem(row, 5, QTableWidgetItem(oj.msgsize))
                    self.tableWidgetMessage.setItem(row, 6, QTableWidgetItem(oj.msg))
                    row = row + 1
            self.tableWidgetMessage.cellChanged.connect(self.Message_Report)

        if searchTxt != "" and self.type == "Secret chats":
            self.tableWidgetMessage.setRowCount(0)
            self.label_2.setText("Massages Table")
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetMessage.setHidden(False)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetMessage.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
            sc = SecretChat()
            list_sorted = sc.getData()
            self.tableWidgetMessage.setColumnCount(7)
            self.tableWidgetMessage.setRowCount(len(list_sorted))

            row = 0

            if self.radioButton_UserName.isChecked() == True:
                for oj in list_sorted:
                    if ("http" not in (oj.msg).lower()) and (oj.msg != "") and ((
                                                                                        (searchTxt).lower() in (
                                                                                        oj.sendername).lower()) or (
                                                                                        (searchTxt).lower() in (
                                                                                        oj.recivedname).lower())):
                        item = QtWidgets.QTableWidgetItem()
                        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item.setCheckState(QtCore.Qt.Unchecked)
                        item.setData(LastStateRole, item.checkState())
                        #self.tableWidgetMessage.insertRow(row)
                        self.tableWidgetMessage.setItem(row, 0, item)
                        self.tableWidgetMessage.setItem(row, 1, QTableWidgetItem(oj.msgID))
                        self.tableWidgetMessage.setItem(row, 2, QTableWidgetItem(oj.sendername))
                        self.tableWidgetMessage.setItem(row, 3, QTableWidgetItem(oj.recivedname))
                        self.tableWidgetMessage.setItem(row, 4, QTableWidgetItem(oj.timestamp))
                        self.tableWidgetMessage.setItem(row, 5, QTableWidgetItem(oj.msgsize))
                        self.tableWidgetMessage.setItem(row, 6, QTableWidgetItem(oj.msg))
                        row = row + 1
                self.tableWidgetMessage.cellChanged.connect(self.Message_Report)
            if self.radioButton_MsgContent.isChecked() == True:
                for oj in list_sorted:
                    if ("http" not in (oj.msg).lower()) and (oj.msg != "") and (searchTxt).lower() in (
                            oj.msg).lower():
                        item = QtWidgets.QTableWidgetItem()
                        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item.setCheckState(QtCore.Qt.Unchecked)
                        item.setData(LastStateRole, item.checkState())
                        self.tableWidgetMessage.setItem(row, 0, item)
                        self.tableWidgetMessage.setItem(row, 1, QTableWidgetItem(oj.msgID))
                        self.tableWidgetMessage.setItem(row, 2, QTableWidgetItem(oj.sendername))
                        self.tableWidgetMessage.setItem(row, 3, QTableWidgetItem(oj.recivedname))
                        self.tableWidgetMessage.setItem(row, 4, QTableWidgetItem(oj.timestamp))
                        self.tableWidgetMessage.setItem(row, 5, QTableWidgetItem(oj.msgsize))
                        self.tableWidgetMessage.setItem(row, 6, QTableWidgetItem(oj.msg))
                        row = row + 1
                self.tableWidgetMessage.cellChanged.connect(self.Message_Report)

    def GetNormal_Search(self):

        searchTxt = self.textEdit.toPlainText()
        if searchTxt == "" and self.type == "Normal chats":
            self.tableWidgetMessage.setRowCount(0)
            self.label_2.setText("Massages Table")
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetMessage.setHidden(False)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetGChannelInfo.setHidden(True)
            self.tableWidgetGroupInfo.setHidden(True)
            self.tableWidgetUsers.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetMessage.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)

            No = NormalChat()
            list_sorted = No.getData()
            self.tableWidgetMessage.setColumnCount(7)
            self.tableWidgetMessage.setRowCount(len(list_sorted))
            row = 0

            for oj in list_sorted:
                if ("http" not in (oj.msg).lower()) and (oj.msg != ""):
                    item = QtWidgets.QTableWidgetItem()
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    item.setCheckState(QtCore.Qt.Unchecked)
                    item.setData(LastStateRole, item.checkState())
                    #self.tableWidgetMessage.insertRow(row)
                    self.tableWidgetMessage.setItem(row, 0, item)
                    self.tableWidgetMessage.setItem(row, 1, QTableWidgetItem(oj.mid))
                    self.tableWidgetMessage.setItem(row, 2, QTableWidgetItem(oj.sender))
                    self.tableWidgetMessage.setItem(row, 3, QTableWidgetItem(oj.reciver))
                    self.tableWidgetMessage.setItem(row, 4, QTableWidgetItem(oj.timestamp))
                    self.tableWidgetMessage.setItem(row, 5, QTableWidgetItem(oj.msgsize))
                    self.tableWidgetMessage.setItem(row, 6, QTableWidgetItem(oj.msg))
                    row = row + 1
            self.tableWidgetMessage.cellChanged.connect(self.Message_Report)

        if searchTxt != "" and self.type == "Normal chats":
            self.tableWidgetMessage.setRowCount(0)
            self.label_2.setText("Massages Table")
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetMessage.setHidden(False)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetGChannelInfo.setHidden(True)
            self.tableWidgetGroupInfo.setHidden(True)
            self.tableWidgetUsers.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetMessage.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
            No = NormalChat()
            list_sorted = No.getData()
            self.tableWidgetMessage.setColumnCount(7)
            self.tableWidgetMessage.setRowCount(len(list_sorted))

            row = 0

            if self.radioButton_UserName.isChecked() == True:
                for oj in list_sorted:
                    if ("http" not in (oj.msg).lower()) and (oj.msg != "") and ((
                                                                                        (searchTxt).lower() in (
                                                                                        oj.sender).lower()) or (
                                                                                        (searchTxt).lower() in (
                                                                                        oj.reciver).lower())):
                        item = QtWidgets.QTableWidgetItem()
                        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item.setCheckState(QtCore.Qt.Unchecked)
                        item.setData(LastStateRole, item.checkState())
                        #self.tableWidgetMessage.insertRow(row)
                        self.tableWidgetMessage.setItem(row, 0, item)
                        self.tableWidgetMessage.setItem(row, 1, QTableWidgetItem(oj.mid))
                        self.tableWidgetMessage.setItem(row, 2, QTableWidgetItem(oj.sender))
                        self.tableWidgetMessage.setItem(row, 3, QTableWidgetItem(oj.reciver))
                        self.tableWidgetMessage.setItem(row, 4, QTableWidgetItem(oj.timestamp))
                        self.tableWidgetMessage.setItem(row, 5, QTableWidgetItem(oj.msgsize))
                        self.tableWidgetMessage.setItem(row, 6, QTableWidgetItem(oj.msg))
                        row = row + 1
                self.tableWidgetMessage.cellChanged.connect(self.Message_Report)

            if self.radioButton_MsgContent.isChecked() == True:
                for oj in list_sorted:
                    if ("http" not in (oj.msg).lower()) and (oj.msg != "") and (searchTxt).lower() in (
                            oj.msg).lower():
                        item = QtWidgets.QTableWidgetItem()
                        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item.setCheckState(QtCore.Qt.Unchecked)
                        item.setData(LastStateRole, item.checkState())
                        self.tableWidgetMessage.setItem(row, 0, item)
                        self.tableWidgetMessage.setItem(row, 1, QTableWidgetItem(oj.mid))
                        self.tableWidgetMessage.setItem(row, 2, QTableWidgetItem(oj.sender))
                        self.tableWidgetMessage.setItem(row, 3, QTableWidgetItem(oj.reciver))
                        self.tableWidgetMessage.setItem(row, 4, QTableWidgetItem(oj.timestamp))
                        self.tableWidgetMessage.setItem(row, 5, QTableWidgetItem(oj.msgsize))
                        self.tableWidgetMessage.setItem(row, 6, QTableWidgetItem(oj.msg))
                        row = row + 1
                self.tableWidgetMessage.cellChanged.connect(self.Message_Report)

    def GetChannels_Search(self):

        searchTxt = self.textEdit.toPlainText()
        if searchTxt == "" and self.type == "Channels":
            self.label_2.setText("Messages Table")
            self.tableWidgetChannels.setRowCount(0)
            self.tableWidgetMessage.setHidden(True)
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(False)
            self.tableWidgetGChannelInfo.setHidden(True)
            self.tableWidgetGroupInfo.setHidden(True)
            self.tableWidgetUsers.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetChannels.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            ch = channel()
            list_sorted = ch.getData()
            self.tableWidgetChannels.setColumnCount(6)
            self.tableWidgetChannels.setRowCount(len(list_sorted))

            row = 0

            for oj in list_sorted:
                if ("http" not in (oj.msg).lower()) and (oj.msg != ""):
                    item = QtWidgets.QTableWidgetItem()
                    item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                    item.setCheckState(QtCore.Qt.Unchecked)
                    item.setData(LastStateRole, item.checkState())
                    #self.tableWidgetChannels.insertRow(row)
                    self.tableWidgetChannels.setItem(row, 0, item)
                    self.tableWidgetChannels.setItem(row, 1, QTableWidgetItem(oj.msgID))
                    self.tableWidgetChannels.setItem(row, 2, QTableWidgetItem(oj.namef))
                    self.tableWidgetChannels.setItem(row, 3, QTableWidgetItem(oj.timestamp))
                    self.tableWidgetChannels.setItem(row, 4, QTableWidgetItem(oj.msgsize))
                    self.tableWidgetChannels.setItem(row, 5, QTableWidgetItem(oj.msg))
                    row = row + 1
            self.tableWidgetChannels.cellChanged.connect(self.Channels_Report)

        if searchTxt != "" and self.type == "Channels":
            self.label_2.setText("Messages Table")
            self.tableWidgetChannels.setRowCount(0)
            self.tableWidgetMessage.setHidden(True)
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(False)
            self.tableWidgetGChannelInfo.setHidden(True)
            self.tableWidgetGroupInfo.setHidden(True)
            self.tableWidgetUsers.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetChannels.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
            ch = channel()
            list_sorted = ch.getData()
            self.tableWidgetChannels.setColumnCount(6)
            self.tableWidgetChannels.setRowCount(len(list_sorted))
            row = 0

            if self.radioButton_MsgContent.isChecked() == True:

                for oj in list_sorted:
                    if ("http" not in (oj.msg).lower()) and (oj.msg != "") and (searchTxt).lower() in (
                            oj.msg).lower():
                        

                        item = QtWidgets.QTableWidgetItem()
                        item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                        item.setCheckState(QtCore.Qt.Unchecked)
                        item.setData(LastStateRole, item.checkState())
                        #self.tableWidgetChannels.insertRow(row)
                        self.tableWidgetChannels.setItem(row, 0, item)
                        self.tableWidgetChannels.setItem(row, 1, QTableWidgetItem(oj.msgID))
                        self.tableWidgetChannels.setItem(row, 2, QTableWidgetItem(oj.namef))
                        self.tableWidgetChannels.setItem(row, 3, QTableWidgetItem(oj.timestamp))
                        self.tableWidgetChannels.setItem(row, 4, QTableWidgetItem(oj.msgsize))
                        self.tableWidgetChannels.setItem(row, 5, QTableWidgetItem(oj.msg))
                        row = row + 1
                self.tableWidgetChannels.cellChanged.connect(self.Channels_Report)

    def Channels_Report(self, row, column):
        item = self.tableWidgetChannels.item(row, column)
        lastState = item.data(LastStateRole)
        currentState = item.checkState()

        if currentState != lastState:  # toggle

            if currentState == QtCore.Qt.Checked:

                inputDialog = QInputDialog(None)
                inputDialog.setFixedSize(400, 300)
                inputDialog.setStyleSheet("background-color: rgb(227, 243, 241);font-size:12px;font-weight: bold;")
                inputDialog.setInputMode(QtWidgets.QInputDialog.TextInput)
                inputDialog.setOption(QtWidgets.QInputDialog.UsePlainTextEditForTextInput)
                inputDialog.setWindowTitle('Add Comment')
                inputDialog.setLabelText('Enter your Comment:')

                ok = inputDialog.exec_()
                comment = inputDialog.textValue()
                if comment == "":
                    comment = "No Comment"
                self.ReportList.append(
                    Report(self.tableWidgetChannels.item(row, 1).text(), "Broadcast",
                           "Broadcast to " + self.tableWidgetChannels.item(row, 2).text(),
                           self.tableWidgetChannels.item(row, 3).text(), self.tableWidgetChannels.item(row, 5).text(),
                           self.type, comment, ""))

            else:

                if len(self.ReportList) > 0:
                    inde = -1
                    index = 0
                    for oj in self.ReportList:
                        if self.tableWidgetChannels.item(row, 1).text() == oj.msgID:
                            inde = index
                        index += 1

                    if inde != -1:
                        self.ReportList.pop(inde)

            item.setData(LastStateRole, currentState)

    def Message_Report(self, row, column):
        item = self.tableWidgetMessage.item(row, column)
        lastState = item.data(LastStateRole)
        currentState = item.checkState()

        if currentState != lastState:  # toggle

            if currentState == QtCore.Qt.Checked:

                inputDialog = QInputDialog(None)
                inputDialog.setFixedSize(400, 300)
                inputDialog.setStyleSheet("background-color: rgb(227, 243, 241);font-size:12px;font-weight: bold;")
                inputDialog.setInputMode(QtWidgets.QInputDialog.TextInput)
                inputDialog.setOption(QtWidgets.QInputDialog.UsePlainTextEditForTextInput)
                inputDialog.setWindowTitle('Add Comment')
                inputDialog.setLabelText('Enter your Comment:')

                ok = inputDialog.exec_()
                comment = inputDialog.textValue()
                if comment == "":
                    comment = "No Comment"
                self.ReportList.append(
                    Report(self.tableWidgetMessage.item(row, 1).text(), self.tableWidgetMessage.item(row, 2).text(),
                           self.tableWidgetMessage.item(row, 3).text(),
                           self.tableWidgetMessage.item(row, 4).text(), self.tableWidgetMessage.item(row, 6).text(),
                           self.type, comment, ""))

            else:

                if len(self.ReportList) > 0:
                    inde = -1
                    index = 0
                    for oj in self.ReportList:
                        if self.tableWidgetMessage.item(row, 1).text() == oj.msgID:
                            inde = index
                        index += 1

                    if inde != -1:
                        self.ReportList.pop(inde)

            item.setData(LastStateRole, currentState)

    def Groups_Report(self, row, column):
        item = self.tableWidgetGroups.item(row, column)
        lastState = item.data(LastStateRole)
        currentState = item.checkState()

        if currentState != lastState:  # toggle

            if currentState == QtCore.Qt.Checked:

                inputDialog = QInputDialog(None)
                inputDialog.setFixedSize(400, 300)
                inputDialog.setStyleSheet("background-color: rgb(227, 243, 241);font-size:12px;font-weight: bold;")
                inputDialog.setInputMode(QtWidgets.QInputDialog.TextInput)
                inputDialog.setOption(QtWidgets.QInputDialog.UsePlainTextEditForTextInput)
                inputDialog.setWindowTitle('Add Comment')
                inputDialog.setLabelText('Enter your Comment:')

                ok = inputDialog.exec_()
                comment = inputDialog.textValue()
                if comment == "":
                    comment = "No Comment"
                self.ReportList.append(
                    Report(self.tableWidgetGroups.item(row, 1).text(), self.tableWidgetGroups.item(row, 2).text(),
                           "Broadcast to " + self.tableWidgetGroups.item(row, 3).text(),
                           self.tableWidgetGroups.item(row, 4).text(), self.tableWidgetGroups.item(row, 6).text(),
                           self.type, comment, ""))

            else:

                if len(self.ReportList) > 0:
                    inde = -1
                    index = 0
                    for oj in self.ReportList:
                        if self.tableWidgetGroups.item(row, 1).text() == oj.msgID:
                            inde = index
                        index += 1

                    if inde != -1:
                        self.ReportList.pop(inde)

            item.setData(LastStateRole, currentState)

    def Media_Report(self, row, column):
        item = self.tableWidgetFiles.item(row, column)
        lastState = item.data(LastStateRole)
        currentState = item.checkState()

        if currentState != lastState:  # toggle

            if currentState == QtCore.Qt.Checked:

                inputDialog = QInputDialog(None)
                inputDialog.setFixedSize(400, 300)
                inputDialog.setStyleSheet("background-color: rgb(227, 243, 241);font-size:12px;font-weight: bold;")
                inputDialog.setInputMode(QtWidgets.QInputDialog.TextInput)
                inputDialog.setOption(QtWidgets.QInputDialog.UsePlainTextEditForTextInput)
                inputDialog.setWindowTitle('Add Comment')
                inputDialog.setLabelText('Enter your Comment:')

                ok = inputDialog.exec_()
                comment = inputDialog.textValue()
                filePath = ""
                if comment == "":
                    comment = "No Comment"
                if (self.type == "Images"):
                    f = ParsingImage()
                    list_sortedM = f.getData()
                    for i in list_sortedM:
                        if i.msgID == self.tableWidgetFiles.item(row, 1).text():
                            filePath = i.Patth

                elif (self.type == "Documents"):
                    f = ParsingDoc()
                    list_sortedM = f.getData()
                    for i in list_sortedM:
                        if i.msgID == self.tableWidgetFiles.item(row, 1).text():
                            filePath = i.Patth

                elif (self.type == "GIF"):
                    f = GIF()
                    list_sortedM = f.getData()
                    for i in list_sortedM:
                        if i.msgID == self.tableWidgetFiles.item(row, 1).text():
                            filePath = i.Patth

                elif (self.type == "Audio"):
                    f = Audio()
                    list_sortedM = f.getData()
                    for i in list_sortedM:
                        if i.msgID == self.tableWidgetFiles.item(row, 1).text():
                            filePath = i.Patth

                elif (self.type == "Videos"):
                    f = ParsingVideo()
                    list_sortedM = f.getData()
                    for i in list_sortedM:
                        if i.msgID == self.tableWidgetFiles.item(row, 1).text():
                            filePath = (i.Patth)


                elif (self.type == "URL"):
                    f = ParsingUrl()
                    list_sortedM = f.getData()
                    for i in list_sortedM:
                        if i.msgID == self.tableWidgetFiles.item(row, 1).text():
                            filePath = i.url
                self.ReportList.append(
                    Report(self.tableWidgetFiles.item(row, 1).text(), self.tableWidgetFiles.item(row, 2).text(),
                           self.tableWidgetFiles.item(row, 3).text(),
                           self.tableWidgetFiles.item(row, 4).text(), self.tableWidgetFiles.item(row, 5).text(),
                           self.tableWidgetFiles.item(row, 6).text() + " " + self.type, comment, filePath))

            else:

                if len(self.ReportList) > 0:
                    inde = -1
                    index = 0
                    for oj in self.ReportList:
                        if self.tableWidgetFiles.item(row, 1).text() == oj.msgID:
                            inde = index
                        index += 1

                    if inde != -1:
                        self.ReportList.pop(inde)

            item.setData(LastStateRole, currentState)

    def MsgContent(self, selected):
        if selected:
            self.GetSecret_Search()
            self.GetNormal_Search()
            self.GetChannels_Search()
            self.GetGroups_Search()

    def UserName(self, selected):
        if selected:
            self.GetSecret_Search()
            self.GetNormal_Search()
            self.GetGroups_Search()

    def ItemClicked(self):
        item = self.treeWidget.currentItem()
        itemClic = item.text(0)
        self.type = item.text(0)
        if (itemClic == "Secret chats"):
            self.GetSecret_Search()

        elif (itemClic == "Normal chats"):
            self.GetNormal_Search()


        elif (itemClic == "Contacts"):

            self.label_2.setText("Contacts Table")
            self.tableWidgetMessage.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetContacts.setHidden(False)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetGChannelInfo.setHidden(True)
            self.tableWidgetGroupInfo.setHidden(True)
            self.tableWidgetUsers.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            u = Users()
            size = u.LoadUsers()
            self.tableWidgetContacts.setColumnCount(5)
            self.tableWidgetContacts.setRowCount(len(size))
            header = self.tableWidgetContacts.horizontalHeader()
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            row = 0
            for i in size:
                self.tableWidgetContacts.setItem(row, 0, QTableWidgetItem(i.UserID))
                self.tableWidgetContacts.setItem(row, 1, QTableWidgetItem(i.Name))
                self.tableWidgetContacts.setItem(row, 2, QTableWidgetItem(i.Username))
                self.tableWidgetContacts.setItem(row, 3, QTableWidgetItem(i.Status))
                self.tableWidgetContacts.setItem(row, 4, QTableWidgetItem(i.Phone))
                row = row + 1




        elif (itemClic == "Images"):

            if (self.tableWidgetFiles.cellClicked.connect(self.cell_was_clicked)):
                self.tableWidgetFiles.cellClicked.disconnect()

            self.tableWidgetFiles.setRowCount(0)

            self.label_2.setText("Media Table")

            self.tableWidgetMessage.setHidden(True)

            self.tableWidgetContacts.setHidden(True)

            self.tableWidgetFiles.setHidden(False)

            self.tableWidgetGroups.setHidden(True)

            self.tableWidgetChannels.setHidden(True)

            self.tableWidgetInfo.setHidden(True)

            header = self.tableWidgetFiles.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

            self.Img = ParsingImage()

            self.list_sortedM = self.Img.getData()

            self.tableWidgetFiles.setColumnCount(7)

            self.tableWidgetFiles.setRowCount(len(self.list_sortedM))

            row = 0

            for oj in self.list_sortedM:
                item = QtWidgets.QTableWidgetItem()

                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)

                item.setCheckState(QtCore.Qt.Unchecked)

                item.setData(LastStateRole, item.checkState())

                self.tableWidgetFiles.setItem(row, 0, item)

                self.tableWidgetFiles.setItem(row, 1, QTableWidgetItem(oj.msgID))

                self.tableWidgetFiles.setItem(row, 2, QTableWidgetItem(oj.sendername))

                self.tableWidgetFiles.setItem(row, 3, QTableWidgetItem(oj.recivedname))

                self.tableWidgetFiles.setItem(row, 4, QTableWidgetItem(oj.timestamp))

                self.tableWidgetFiles.setItem(row, 5, QTableWidgetItem(oj.file))

                self.tableWidgetFiles.setItem(row, 6, QTableWidgetItem(oj.type))

                row = row + 1

            self.tableWidgetFiles.cellClicked.connect(self.cell_was_clicked)

            self.tableWidgetFiles.cellChanged.connect(self.Media_Report)


        elif (itemClic == "Videos"):

            if (self.tableWidgetFiles.cellClicked.connect(self.cell_was_clicked)):
                self.tableWidgetFiles.cellClicked.disconnect()

            self.tableWidgetFiles.setRowCount(0)

            self.label_2.setText("Media Table")

            self.tableWidgetMessage.setHidden(True)

            self.tableWidgetContacts.setHidden(True)

            self.tableWidgetFiles.setHidden(False)

            self.tableWidgetGroups.setHidden(True)

            self.tableWidgetChannels.setHidden(True)

            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetFiles.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

            Vid = ParsingVideo()

            list_sorted3 = Vid.getData()

            self.tableWidgetFiles.setColumnCount(7)

            self.tableWidgetFiles.setRowCount(len(list_sorted3))

            row = 0

            for oj in list_sorted3:
                item = QtWidgets.QTableWidgetItem()

                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)

                item.setCheckState(QtCore.Qt.Unchecked)

                item.setData(LastStateRole, item.checkState())

                self.tableWidgetFiles.setItem(row, 0, item)

                self.tableWidgetFiles.setItem(row, 1, QTableWidgetItem(oj.msgID))

                self.tableWidgetFiles.setItem(row, 2, QTableWidgetItem(oj.sendername))

                self.tableWidgetFiles.setItem(row, 3, QTableWidgetItem(oj.recivedname))

                self.tableWidgetFiles.setItem(row, 4, QTableWidgetItem(oj.timestamp))

                self.tableWidgetFiles.setItem(row, 5, QTableWidgetItem(oj.file))

                self.tableWidgetFiles.setItem(row, 6, QTableWidgetItem(oj.type))

                row = row + 1

            self.tableWidgetFiles.cellClicked.connect(self.cell_was_clicked)

            self.tableWidgetFiles.cellChanged.connect(self.Media_Report)


        elif (itemClic == "Audio"):

            if (self.tableWidgetFiles.cellClicked.connect(self.cell_was_clicked)):
                self.tableWidgetFiles.cellClicked.disconnect()

            self.tableWidgetFiles.setRowCount(0)

            self.label_2.setText("Media Table")

            self.tableWidgetMessage.setHidden(True)

            self.tableWidgetContacts.setHidden(True)

            self.tableWidgetFiles.setHidden(False)

            self.tableWidgetGroups.setHidden(True)

            self.tableWidgetChannels.setHidden(True)

            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetFiles.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

            Aud = Audio()

            list_sorted4 = Aud.getData()

            self.tableWidgetFiles.setColumnCount(7)

            self.tableWidgetFiles.setRowCount(len(list_sorted4))

            row = 0

            for oj in list_sorted4:
                item = QtWidgets.QTableWidgetItem()

                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)

                item.setCheckState(QtCore.Qt.Unchecked)

                item.setData(LastStateRole, item.checkState())

                self.tableWidgetFiles.setItem(row, 0, item)

                self.tableWidgetFiles.setItem(row, 1, QTableWidgetItem(oj.msgID))

                self.tableWidgetFiles.setItem(row, 2, QTableWidgetItem(oj.sendername))

                self.tableWidgetFiles.setItem(row, 3, QTableWidgetItem(oj.recivedname))

                self.tableWidgetFiles.setItem(row, 4, QTableWidgetItem(oj.timestamp))

                self.tableWidgetFiles.setItem(row, 5, QTableWidgetItem(oj.file))

                self.tableWidgetFiles.setItem(row, 6, QTableWidgetItem(oj.type))

                row = row + 1

            self.tableWidgetFiles.cellClicked.connect(self.cell_was_clicked)

            self.tableWidgetFiles.cellChanged.connect(self.Media_Report)


        elif (itemClic == "Documents"):

            if (self.tableWidgetFiles.cellClicked.connect(self.cell_was_clicked)):
                self.tableWidgetFiles.cellClicked.disconnect()

            self.tableWidgetFiles.setRowCount(0)

            self.label_2.setText("Media Table")

            self.tableWidgetMessage.setHidden(True)

            self.tableWidgetContacts.setHidden(True)

            self.tableWidgetFiles.setHidden(False)

            self.tableWidgetGroups.setHidden(True)

            self.tableWidgetChannels.setHidden(True)

            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetFiles.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

            Doc = ParsingDoc()

            list_sorted5 = Doc.getData()

            self.tableWidgetFiles.setColumnCount(7)

            self.tableWidgetFiles.setRowCount(len(list_sorted5))

            row = 0

            for oj in list_sorted5:
                item = QtWidgets.QTableWidgetItem()

                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)

                item.setCheckState(QtCore.Qt.Unchecked)

                item.setData(LastStateRole, item.checkState())

                self.tableWidgetFiles.setItem(row, 0, item)

                self.tableWidgetFiles.setItem(row, 1, QTableWidgetItem(oj.msgID))

                self.tableWidgetFiles.setItem(row, 2, QTableWidgetItem(oj.sendername))

                self.tableWidgetFiles.setItem(row, 3, QTableWidgetItem(oj.recivedname))

                self.tableWidgetFiles.setItem(row, 4, QTableWidgetItem(oj.timestamp))

                self.tableWidgetFiles.setItem(row, 5, QTableWidgetItem(oj.file))

                self.tableWidgetFiles.setItem(row, 6, QTableWidgetItem(oj.type))

                row = row + 1

            self.tableWidgetFiles.cellClicked.connect(self.cell_was_clicked)

            self.tableWidgetFiles.cellChanged.connect(self.Media_Report)


        elif (itemClic == "GIF"):

            if (self.tableWidgetFiles.cellClicked.connect(self.cell_was_clicked)):
                self.tableWidgetFiles.cellClicked.disconnect()

            self.tableWidgetFiles.setRowCount(0)

            self.label_2.setText("Media Table")

            self.tableWidgetMessage.setHidden(True)

            self.tableWidgetContacts.setHidden(True)

            self.tableWidgetFiles.setHidden(False)

            self.tableWidgetGroups.setHidden(True)

            self.tableWidgetChannels.setHidden(True)

            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetFiles.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

            c = GIF()

            list_sorted6 = c.getData()

            self.tableWidgetFiles.setColumnCount(7)

            self.tableWidgetFiles.setRowCount(len(list_sorted6))

            row = 0

            for oj in list_sorted6:
                item = QtWidgets.QTableWidgetItem()

                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)

                item.setCheckState(QtCore.Qt.Unchecked)

                item.setData(LastStateRole, item.checkState())

                self.tableWidgetFiles.setItem(row, 0, item)

                self.tableWidgetFiles.setItem(row, 1, QTableWidgetItem(oj.msgID))

                self.tableWidgetFiles.setItem(row, 2, QTableWidgetItem(oj.sendername))

                self.tableWidgetFiles.setItem(row, 3, QTableWidgetItem(oj.recivedname))

                self.tableWidgetFiles.setItem(row, 4, QTableWidgetItem(oj.timestamp))

                self.tableWidgetFiles.setItem(row, 5, QTableWidgetItem(oj.file))

                self.tableWidgetFiles.setItem(row, 6, QTableWidgetItem(oj.type))

                row = row + 1

            self.tableWidgetFiles.cellClicked.connect(self.cell_was_clicked)

            self.tableWidgetFiles.cellChanged.connect(self.Media_Report)


        elif (itemClic == "URL"):

            if (self.tableWidgetFiles.cellClicked.connect(self.cell_was_clicked)):
                self.tableWidgetFiles.cellClicked.disconnect()

            self.tableWidgetFiles.setRowCount(0)

            self.label_2.setText("Media Table")

            self.tableWidgetMessage.setHidden(True)

            self.tableWidgetContacts.setHidden(True)

            self.tableWidgetFiles.setHidden(False)

            self.tableWidgetGroups.setHidden(True)

            self.tableWidgetChannels.setHidden(True)

            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetFiles.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

            U = ParsingUrl()

            list_sorted7 = U.getData()

            self.tableWidgetFiles.setColumnCount(7)

            self.tableWidgetFiles.setRowCount(len(list_sorted7))

            row = 0

            for oj in list_sorted7:
                item = QtWidgets.QTableWidgetItem()

                item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)

                item.setCheckState(QtCore.Qt.Unchecked)

                item.setData(LastStateRole, item.checkState())

                self.tableWidgetFiles.setItem(row, 0, item)

                self.tableWidgetFiles.setItem(row, 1, QTableWidgetItem(oj.msgID))

                self.tableWidgetFiles.setItem(row, 2, QTableWidgetItem(oj.sendername))

                self.tableWidgetFiles.setItem(row, 3, QTableWidgetItem(oj.recivedname))

                self.tableWidgetFiles.setItem(row, 4, QTableWidgetItem(oj.timestamp))

                self.tableWidgetFiles.setItem(row, 5, QTableWidgetItem(oj.url))

                self.tableWidgetFiles.setItem(row, 6, QTableWidgetItem(oj.type))

                row = row + 1

            self.tableWidgetFiles.cellClicked.connect(self.cell_was_clicked)

            self.tableWidgetFiles.cellChanged.connect(self.Media_Report)

        elif (itemClic == "Device information"):
            self.label_2.setText("Device Information")
            self.tableWidgetMessage.setHidden(True)
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetInfo.setHidden(False)
            header = self.tableWidgetInfo.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            i = Imageinfo()
            list_sorted8 = i.DeviceData()
            self.tableWidgetInfo.setColumnCount(5)
            self.tableWidgetInfo.setRowCount(len(list_sorted8))
            row = 0
            for oj in list_sorted8:
                self.tableWidgetInfo.setItem(row, 0, QTableWidgetItem(oj.version))
                self.tableWidgetInfo.setItem(row, 1, QTableWidgetItem(oj.name))
                self.tableWidgetInfo.setItem(row, 2, QTableWidgetItem(oj.brand))
                self.tableWidgetInfo.setItem(row, 3, QTableWidgetItem(oj.model))
                self.tableWidgetInfo.setItem(row, 4, QTableWidgetItem(oj.country))


            if (oj.version != "No device attached"):
                self.androidversion = oj.version
                self.devicename = oj.name
                self.brand = oj.brand
                self.model = oj.model
                self.country = oj.country
                self.completed=True

                if self.completed == True:
                    if self.investigatorname != "" and self.casedescription != "" and self.date != "":
                        f = open("dump/" + str(self.casename) + ".txt", "w")
                        f.write(self.casename)
                        f.write("\n")
                        f.write(self.investigatorname)
                        f.write("\n")
                        f.write(self.casedescription)
                        f.write("\n")
                        f.write(self.date)
                        f.write("\n")
                        f.write(self.devicename)
                        f.write(self.androidversion)
                        f.write(self.brand)
                        f.write(self.model)
                        f.write(self.country)
                        f.close()

                






        elif (itemClic == "Channels"):
            self.GetChannels_Search()

        elif (itemClic == "Groups"):
            self.GetGroups_Search()

        elif (itemClic == "Users"):
            self.label_2.setText("Users Table")
            self.tableWidgetMessage.setRowCount(0)
            self.tableWidgetMessage.setHidden(True)
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetGChannelInfo.setHidden(True)
            self.tableWidgetGroupInfo.setHidden(True)
            self.tableWidgetUsers.setHidden(False)
            self.tableWidgetInfo.setHidden(True)
            u = Track()
            size = u.usr()
            self.tableWidgetUsers.setColumnCount(5)
            self.tableWidgetUsers.setRowCount(len(size))
            header = self.tableWidgetUsers.horizontalHeader()
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
            row = 0
            for i in size:
                self.tableWidgetUsers.setItem(row, 0, QTableWidgetItem(i.UserID))
                self.tableWidgetUsers.setItem(row, 1, QTableWidgetItem(i.Name))
                self.tableWidgetUsers.setItem(row, 2, QTableWidgetItem(i.Username))
                self.tableWidgetUsers.setItem(row, 3, QTableWidgetItem(i.Status))
                self.tableWidgetUsers.setItem(row, 4, QTableWidgetItem(i.Phone))
                row = row + 1

        elif (itemClic == "Group information"):
            self.label_2.setText("Groups Information Table")
            self.tableWidgetGroupInfo.setRowCount(0)
            self.tableWidgetMessage.setHidden(True)
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetGChannelInfo.setHidden(True)
            self.tableWidgetGroupInfo.setHidden(False)
            self.tableWidgetUsers.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetGroupInfo.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            grI = GroupInfo()
            list_sorted = grI.getData()
            self.tableWidgetGroupInfo.setColumnCount(3)
            row = 0
            name = ""
            list_sorted.reverse()
            for oj in list_sorted:
                if oj.namef == name:
                    break
                else:
                    self.tableWidgetGroupInfo.insertRow(row)
                    self.tableWidgetGroupInfo.setItem(row, 0, QTableWidgetItem(oj.namef))
                    self.tableWidgetGroupInfo.setItem(row, 1, QTableWidgetItem(oj.timestamp))
                    self.tableWidgetGroupInfo.setItem(row, 2, QTableWidgetItem(oj.creator))
                    row = row + 1
                    name = oj.namef




        elif (itemClic == "Channel information"):
            self.label_2.setText("Channel Information Table")
            self.tableWidgetGChannelInfo.setRowCount(0)
            self.tableWidgetMessage.setHidden(True)
            self.tableWidgetContacts.setHidden(True)
            self.tableWidgetFiles.setHidden(True)
            self.tableWidgetGroups.setHidden(True)
            self.tableWidgetChannels.setHidden(True)
            self.tableWidgetGChannelInfo.setHidden(False)
            self.tableWidgetGroupInfo.setHidden(True)
            self.tableWidgetUsers.setHidden(True)
            self.tableWidgetInfo.setHidden(True)
            header = self.tableWidgetGChannelInfo.horizontalHeader()
            header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
            header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
            chI = channelInfo()
            list_sorted = chI.getData()
            self.tableWidgetGChannelInfo.setColumnCount(3)
            self.tableWidgetGChannelInfo.setRowCount(len(list_sorted))
            row = 0

            for oj in list_sorted:
                self.tableWidgetGChannelInfo.setItem(row, 0, QTableWidgetItem(oj.namef))
                self.tableWidgetGChannelInfo.setItem(row, 1, QTableWidgetItem(oj.timestamp))
                self.tableWidgetGChannelInfo.setItem(row, 2, QTableWidgetItem(oj.adminrrec))
                row = row + 1



    def setupUi(self):
        self.setObjectName("self")
        self.resize(1310, 670)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/icons/Picture1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setStyleSheet("background-color: rgb(250, 250, 250);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(20, 90, 231, 511))
        self.treeWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.treeWidget.setObjectName("treeWidget")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/icons/copy_48px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.treeWidget.headerItem().setIcon(0, icon1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/image/icons/bulleted_list_30px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item_0.setIcon(0, icon2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/image/icons/contact_40px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item_0.setIcon(0, icon3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/image/icons/user_account_26px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item_0.setIcon(0, icon4)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/image/icons/chat_40px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item_0.setIcon(0, icon5)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/image/icons/user_groups_40px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon6)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/image/icons/view_details_80px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item_2.setIcon(0, icon7)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/image/icons/group_task_40px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon8)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2.setIcon(0, icon7)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/image/icons/add_to_chat_64px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon9)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/image/icons/search_chat_100px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon10)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/image/icons/media_24px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item_0.setIcon(0, icon11)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/image/icons/documents_40px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item_1.setIcon(0, icon12)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/image/icons/image_100px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item_1.setIcon(0, icon13)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/image/icons/video_64px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item_1.setIcon(0, icon14)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/image/icons/audio_48px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item_1.setIcon(0, icon15)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/image/icons/link_30px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item_1.setIcon(0, icon16)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/image/icons/gif_16px.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item_1.setIcon(0, icon17)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 170, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("QPushButton::hover"
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
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/image/icons/upload_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon18)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")

        # action for push button Create
        self.pushButton.clicked.connect(self.openwindow)

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 60, 1291, 561))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color:  rgb(227, 243, 241);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(280, 0, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:  rgb(227, 243, 241);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:  rgb(227, 243, 241);")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(280, 30, 991, 511))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")
        self.tableWidgetGChannelInfo = QtWidgets.QTableWidget(self.widget)
        self.tableWidgetGChannelInfo.setGeometry(QtCore.QRect(0, 0, 991, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableWidgetGChannelInfo.sizePolicy().hasHeightForWidth())
        self.tableWidgetGChannelInfo.setSizePolicy(sizePolicy)
        self.tableWidgetGChannelInfo.setMinimumSize(QtCore.QSize(791, 0))
        self.tableWidgetGChannelInfo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetGChannelInfo.setObjectName("tableWidgetGChannelInfo")
        self.tableWidgetGChannelInfo.setColumnCount(3)
        self.tableWidgetGChannelInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGChannelInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGChannelInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGChannelInfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGroupInfo = QtWidgets.QTableWidget(self.widget)
        self.tableWidgetGroupInfo.setGeometry(QtCore.QRect(0, 0, 991, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableWidgetGroupInfo.sizePolicy().hasHeightForWidth())
        self.tableWidgetGroupInfo.setSizePolicy(sizePolicy)
        self.tableWidgetGroupInfo.setMinimumSize(QtCore.QSize(791, 0))
        self.tableWidgetGroupInfo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetGroupInfo.setObjectName("tableWidgetGroupInfo")
        self.tableWidgetGroupInfo.setColumnCount(3)
        self.tableWidgetGroupInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGroupInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGroupInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGroupInfo.setHorizontalHeaderItem(2, item)
        self.tableWidgetUsers = QtWidgets.QTableWidget(self.widget)
        self.tableWidgetUsers.setGeometry(QtCore.QRect(0, 0, 991, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableWidgetUsers.sizePolicy().hasHeightForWidth())
        self.tableWidgetUsers.setSizePolicy(sizePolicy)
        self.tableWidgetUsers.setMinimumSize(QtCore.QSize(791, 0))
        self.tableWidgetUsers.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetUsers.setObjectName("tableWidgetUsers")
        self.tableWidgetUsers.setColumnCount(5)
        self.tableWidgetUsers.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetUsers.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetUsers.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetUsers.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetUsers.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetUsers.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetUsers.setHorizontalHeaderItem(5, item)
        self.tableWidgetChannels = QtWidgets.QTableWidget(self.widget)
        self.tableWidgetChannels.setGeometry(QtCore.QRect(0, 0, 991, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableWidgetChannels.sizePolicy().hasHeightForWidth())
        self.tableWidgetChannels.setSizePolicy(sizePolicy)
        self.tableWidgetChannels.setMinimumSize(QtCore.QSize(791, 0))
        self.tableWidgetChannels.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetChannels.setObjectName("tableWidgetChannels")
        self.tableWidgetChannels.setColumnCount(6)
        self.tableWidgetChannels.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetChannels.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetChannels.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetChannels.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetChannels.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetChannels.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetChannels.setHorizontalHeaderItem(5, item)
        self.tableWidgetGroups = QtWidgets.QTableWidget(self.widget)
        self.tableWidgetGroups.setGeometry(QtCore.QRect(0, 0, 991, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableWidgetGroups.sizePolicy().hasHeightForWidth())
        self.tableWidgetGroups.setSizePolicy(sizePolicy)
        self.tableWidgetGroups.setMinimumSize(QtCore.QSize(791, 0))
        self.tableWidgetGroups.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetGroups.setObjectName("tableWidgetGroups")
        self.tableWidgetGroups.setColumnCount(7)
        self.tableWidgetGroups.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGroups.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGroups.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGroups.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGroups.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGroups.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGroups.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGroups.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetGroups.setHorizontalHeaderItem(7, item)
        self.tableWidgetFiles = QtWidgets.QTableWidget(self.widget)
        self.tableWidgetFiles.setGeometry(QtCore.QRect(0, 0, 991, 511))
        self.tableWidgetFiles.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetFiles.setObjectName("tableWidgetFiles")
        self.tableWidgetFiles.setColumnCount(7)
        self.tableWidgetFiles.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetFiles.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetFiles.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        item.setFont(font)
        self.tableWidgetFiles.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetFiles.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetFiles.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetFiles.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetFiles.setHorizontalHeaderItem(6, item)
        self.tableWidgetContacts = QtWidgets.QTableWidget(self.widget)
        self.tableWidgetContacts.setGeometry(QtCore.QRect(0, 0, 991, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableWidgetContacts.sizePolicy().hasHeightForWidth())
        self.tableWidgetContacts.setSizePolicy(sizePolicy)
        self.tableWidgetContacts.setMinimumSize(QtCore.QSize(791, 0))
        self.tableWidgetContacts.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetContacts.setObjectName("tableWidgetContacts")
        self.tableWidgetContacts.setColumnCount(5)
        self.tableWidgetContacts.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetContacts.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetContacts.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetContacts.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetContacts.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetContacts.setHorizontalHeaderItem(4, item)
        self.tableWidgetMessage = QtWidgets.QTableWidget(self.widget)
        self.tableWidgetMessage.setGeometry(QtCore.QRect(0, 0, 991, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableWidgetMessage.sizePolicy().hasHeightForWidth())
        self.tableWidgetMessage.setSizePolicy(sizePolicy)
        self.tableWidgetMessage.setMinimumSize(QtCore.QSize(791, 0))
        self.tableWidgetMessage.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetMessage.setObjectName("tableWidgetMessage")
        self.tableWidgetMessage.setColumnCount(7)
        self.tableWidgetMessage.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetMessage.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetMessage.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetMessage.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetMessage.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetMessage.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetMessage.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetMessage.setHorizontalHeaderItem(6, item)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 0, 1291, 61))

        "-------------------------------"
        self.tableWidgetInfo = QtWidgets.QTableWidget(self.widget)
        self.tableWidgetInfo.setGeometry(QtCore.QRect(0, 0, 991, 511))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.tableWidgetInfo.sizePolicy().hasHeightForWidth())
        self.tableWidgetInfo.setSizePolicy(sizePolicy)
        self.tableWidgetInfo.setMinimumSize(QtCore.QSize(791, 0))
        self.tableWidgetInfo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidgetInfo.setObjectName("tableWidgetContacts")
        self.tableWidgetInfo.setColumnCount(5)
        self.tableWidgetInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetInfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetInfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetInfo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        item.setFont(font)
        self.tableWidgetInfo.setHorizontalHeaderItem(4, item)

        # getting the item that is clicked
        self.treeWidget.itemClicked.connect(self.ItemClicked)

        self.frame_2.setStyleSheet("background-color: rgb(200, 232, 232);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.textChanged.connect(self.checkTxt)
        # serach label
        self.textEdit.setPlaceholderText("Search..")
        self.textEdit.setGeometry(QtCore.QRect(850, 10, 161, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(0, 40, 1291, 16))
        self.line.setStyleSheet("background-color: rgb(200, 232, 232);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 10, 170, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton::hover"
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
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(":/image/icons/save_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon19)
        self.pushButton_3.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        # action for push button Save as
        self.pushButton_3.clicked.connect(self.openwindow2)

        # self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        # self.pushButton_4.setGeometry(QtCore.QRect(390, 10, 170, 31))
        # font = QtGui.QFont()
        # font.setFamily("Lucida Sans Unicode")
        # font.setPointSize(9)
        # self.pushButton_4.setFont(font)
        # self.pushButton_4.setStyleSheet("QPushButton::hover"
        #                      "{"
        #                      "background-color : rgb(232, 232, 232);"
        #                      "}"
        #
        #                      "QPushButton"
        #                      "{"
        #                      "border-style:outset;\n"
        #                      "border-color:white;\n"
        #                      "border-width:2px;\n"
        #                      "border-radius:10px;\n"
        #                      "background-color: rgb(248, 248, 248);\n"
        #                     "}"
        #
        #                     "QPushButton::pressed"
        #                     "{"
        #                     "background-color : gray;"
        #                     "}")
        # icon20 = QtGui.QIcon()
        # icon20.addPixmap(QtGui.QPixmap(":/image/icons/plus_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        # self.pushButton_4.setIcon(icon20)
        # self.pushButton_4.setIconSize(QtCore.QSize(25, 25))
        # self.pushButton_4.setObjectName("pushButton_4")
        #
        # # action for push button add to case
        # self.pushButton_4.clicked.connect(self.openwindow3)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 10, 170, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.pushButton_5.setFont(font)
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
        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap(":/image/icons/edit_graph_report_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon21)
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")

        # action for push button genertae reoprt
        self.pushButton_5.clicked.connect(self.openwindow6)

        # self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        # self.pushButton_2.setGeometry(QtCore.QRect(1240, 10, 41, 31))
        # self.pushButton_2.setStyleSheet("image: url(:/image/icons/search_48px.png);\n"
        #                                 "")
        # self.pushButton_2.setText("")
        # self.pushButton_2.setObjectName("pushButton_2")
        #
        # # action for push button Search
        # self.pushButton_2.clicked.connect(self.search)
        # Radio button for MsgContent
        self.radioButton_MsgContent = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_MsgContent.setGeometry(QtCore.QRect(1030, 10, 150, 31))

        # adding signal and slot
        # self.radioButton_MsgContent.toggled.connect(self.MsgContent)

        # Radio button for UserName
        self.radioButton_UserName = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_UserName.setGeometry(QtCore.QRect(1170, 10, 100, 31))
        # adding signal and slot
        self.radioButton_UserName.toggled.connect(self.UserName)
        # adding signal and slot
        self.radioButton_MsgContent.toggled.connect(self.MsgContent)
        self.radioButton_MsgContent.setChecked(True)

        # adding signal and slot
        # self.radioButton_UserName.toggled.connect(self.UserName)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(290, 90, 991, 511))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.treeWidget.raise_()
        self.pushButton.raise_()
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1310, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.setMenuBar(self.menubar)
        #self.actionTelegrip_Manual = QtWidgets.QAction(MainWindow)
        #self.actionTelegrip_Manual.setObjectName("actionTelegrip_Manual")
        self.actionTelegrip_Manual_2 = QtWidgets.QAction(self)
        self.actionTelegrip_Manual_2.setObjectName("actionTelegrip_Manual_2")
        self.actionNew_case = QtWidgets.QAction(self)
        self.actionNew_case.setObjectName("actionNew_case")

        self.actionTelegrip_Manual_2.triggered.connect(self.openwindowme)
        self.actionNew_case.triggered.connect(self.openwindow1)

        #self.actionOpen_case = QtWidgets.QAction(MainWindow)
        #self.actionOpen_case.setObjectName("actionOpen_case")
        #self.actionSave = QtWidgets.QAction(MainWindow)
        #self.actionSave.setObjectName("actionSave")
        #self.actionSave_as = QtWidgets.QAction(MainWindow)
        #self.actionSave_as.setObjectName("actionSave_as")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew_case)
        #self.menuFile.addAction(self.actionOpen_case)
        #self.menuFile.addAction(self.actionSave)
        #self.menuFile.addAction(self.actionSave_as)
        self.menuView.addAction(self.actionTelegrip_Manual_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        # hide the tables
        self.tableWidgetContacts.setHidden(True)
        self.tableWidgetFiles.setHidden(True)
        self.tableWidgetGroups.setHidden(True)
        self.tableWidgetChannels.setHidden(True)
        self.tableWidgetMessage.setHidden(True)
        self.tableWidgetGChannelInfo.setHidden(True)
        self.tableWidgetGroupInfo.setHidden(True)
        self.tableWidgetUsers.setHidden(True)
        self.tableWidgetInfo.setHidden(True)


    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Telegrip"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Image"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Device information"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Contacts"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Users"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "Messages"))
        self.treeWidget.topLevelItem(3).child(0).setText(0, _translate("MainWindow", "Channels"))
        self.treeWidget.topLevelItem(3).child(0).child(0).setText(0, _translate("MainWindow", "Channel information"))
        self.treeWidget.topLevelItem(3).child(1).setText(0, _translate("MainWindow", "Groups"))
        self.treeWidget.topLevelItem(3).child(1).child(0).setText(0, _translate("MainWindow", "Group information"))
        self.treeWidget.topLevelItem(3).child(2).setText(0, _translate("MainWindow", "Normal chats"))
        self.treeWidget.topLevelItem(3).child(3).setText(0, _translate("MainWindow", "Secret chats"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "Media"))
        self.treeWidget.topLevelItem(4).child(0).setText(0, _translate("MainWindow", "Documents"))
        self.treeWidget.topLevelItem(4).child(1).setText(0, _translate("MainWindow", "Images"))
        self.treeWidget.topLevelItem(4).child(2).setText(0, _translate("MainWindow", "Videos"))
        self.treeWidget.topLevelItem(4).child(3).setText(0, _translate("MainWindow", "Audio"))
        self.treeWidget.topLevelItem(4).child(4).setText(0, _translate("MainWindow", "URL"))
        self.treeWidget.topLevelItem(4).child(5).setText(0, _translate("MainWindow", "GIF"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setText(_translate("MainWindow", "Create Device Image"))
        self.label_2.setText(_translate("MainWindow", "Evidence Table"))
        self.label.setText(_translate("MainWindow", "Evidence Tree"))
        item = self.tableWidgetGChannelInfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetGChannelInfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time of creation"))
        item = self.tableWidgetGChannelInfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Admins"))
        item = self.tableWidgetGroupInfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetGroupInfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time of creation"))
        item = self.tableWidgetGroupInfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Created by"))
        item = self.tableWidgetUsers.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User ID"))
        item = self.tableWidgetUsers.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetUsers.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidgetUsers.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status"))
        item = self.tableWidgetUsers.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Phone"))
        item = self.tableWidgetChannels.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Message ID"))
        item = self.tableWidgetChannels.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Channel name"))
        item = self.tableWidgetChannels.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Timestamp"))
        item = self.tableWidgetChannels.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Message Size"))
        item = self.tableWidgetChannels.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Message Content"))
        item = self.tableWidgetGroups.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Message ID"))
        item = self.tableWidgetGroups.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sender Name"))
        item = self.tableWidgetGroups.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Group Name"))
        item = self.tableWidgetGroups.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Timestamp"))
        item = self.tableWidgetGroups.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Message Size"))
        item = self.tableWidgetGroups.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Message Content"))
        item = self.tableWidgetFiles.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Message ID"))
        item = self.tableWidgetFiles.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sender name"))
        item = self.tableWidgetFiles.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Receiver name"))
        item = self.tableWidgetFiles.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Timestamp"))
        item = self.tableWidgetFiles.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "File name"))
        item = self.tableWidgetFiles.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Type"))
        item = self.tableWidgetContacts.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "User ID"))
        item = self.tableWidgetContacts.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidgetContacts.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Username"))
        item = self.tableWidgetContacts.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status (Last seen)"))
        item = self.tableWidgetContacts.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Phone number"))
        item = self.tableWidgetInfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Android version"))
        item = self.tableWidgetInfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Device name"))
        item = self.tableWidgetInfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Device brand"))
        item = self.tableWidgetInfo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Device model"))
        item = self.tableWidgetInfo.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Country"))

        item = self.tableWidgetMessage.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Message ID"))
        item = self.tableWidgetMessage.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sender name"))
        item = self.tableWidgetMessage.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Receiver name"))
        item = self.tableWidgetMessage.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Timestamp"))
        item = self.tableWidgetMessage.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Message size"))
        item = self.tableWidgetMessage.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Message content"))
        self.pushButton_3.setText(_translate("MainWindow", "Save as"))
        #self.pushButton_4.setText(_translate("MainWindow", "Add to case"))
        self.pushButton_5.setText(_translate("MainWindow", "Generate report"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuView.setTitle(_translate("MainWindow", "Info"))
        #self.actionTelegrip_Manual.setText(_translate("MainWindow", "Telegrip Manual"))
        self.actionTelegrip_Manual_2.setText(_translate("MainWindow", "Telegrip Manual"))
        self.actionNew_case.setText(_translate("MainWindow", "New/open case"))
        #self.actionOpen_case.setText(_translate("MainWindow", "Open case"))
        #self.actionSave.setText(_translate("MainWindow", "Save"))
        #self.actionSave_as.setText(_translate("MainWindow", "Save as"))
        self.radioButton_MsgContent.setText(_translate("MainWindow", "Message content"))
        self.radioButton_UserName.setText(_translate("MainWindow", "User name"))

    def closeEvent(self,event):
        if self.saved == False:
            self.openwindow2()





import Resources




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    # MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow('','','','')
    ui.setupUi()
    app.aboutToQuit.connect(ui.closeEvent())
    ui.setWindowFlags(ui.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)#disable
    ui.show()
    sys.exit(app.exec_())
