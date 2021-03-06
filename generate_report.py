import os
import re
from aifc import Error

from fpdf import FPDF
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QScrollBar, QScrollArea, QMainWindow

now = datetime.now()

dt_string = now.strftime("%m/%d/%Y %H:%M:%S")  # footer date
dtf_string = now.strftime("%m%d%Y%H%M%S")  # format for pdf name


class PDF(FPDF):

    def header(self):

        self.image('logo.jpg', 125, 8, 35, 35)  # logo
        self.set_font('Arial', 'B', 12)  # font setting
        self.ln(50)  # Line break

    def footer(self):

        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')  # Page number
        self.cell(0, 10, dt_string, 0, 0, 'R')  # date/time


class Ui_generate_report(QMainWindow):

    def __init__(self):
        super().__init__()

    def __init__(self, list, casename, investigatorname, casedescription, devicename, androidversion, hashed, dated,
                 brand, model, country):
        super().__init__()
        self.list = list
        self.casename = casename
        self.investigatorname = investigatorname
        self.casedescription = casedescription
        self.devicename = devicename
        self.androidversion = androidversion
        self.hashed = hashed
        self.dated = dated
        self.brand = brand
        self.model = model
        self.country = country

    def setupUi(self):

        self.setObjectName("self")
        self.resize(850, 572)
        self.setStyleSheet("background-color: rgb(227, 243, 241)")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 800, 500))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.report_table = QtWidgets.QTableWidget(self.frame)
        self.report_table.setGeometry(QtCore.QRect(0, 320, 780, 180))
        self.report_table.setObjectName("report_table")
        self.report_table.setColumnCount(6)
        self.report_table.setRowCount(len(self.list))
        header = self.report_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)

        row = 0
        for oj in self.list:
            self.report_table.setItem(row, 0, QTableWidgetItem(oj.comment))
            self.report_table.setItem(row, 1, QTableWidgetItem(oj.type))
            self.report_table.setItem(row, 2, QTableWidgetItem(oj.content))
            self.report_table.setItem(row, 3, QTableWidgetItem(oj.sendername))
            self.report_table.setItem(row, 4, QTableWidgetItem(oj.recivedname))
            self.report_table.setItem(row, 5, QTableWidgetItem(oj.timestamp))
            row = row + 1



        self.report_table.setColumnCount(6)
        self.report_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.report_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.report_table.setHorizontalHeaderItem(5, item)
        self.photo = QtWidgets.QLabel(self.frame)
        self.photo.setGeometry(QtCore.QRect(290, 5, 100, 100))
        self.photo.setText("")

        self.photo.setPixmap(QtGui.QPixmap("logo.jpg"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.case_name = QtWidgets.QLabel(self.frame)
        self.case_name.setGeometry(QtCore.QRect(10, 110, 300, 16))
        self.case_name.setObjectName("case_name")
        self.Investigator_name = QtWidgets.QLabel(self.frame)
        self.Investigator_name.setGeometry(QtCore.QRect(10, 130, 300, 16))
        self.Investigator_name.setObjectName("Investigator_name")
        self.case_descrition = QtWidgets.QLabel(self.frame)
        self.case_descrition.setGeometry(QtCore.QRect(10, 150, 300, 16))
        self.case_descrition.setObjectName("case_descrition")
        self.date = QtWidgets.QLabel(self.frame)
        self.date.setGeometry(QtCore.QRect(10, 170, 300, 16))
        self.date.setObjectName("date")
        self.device_name = QtWidgets.QLabel(self.frame)
        self.device_name.setGeometry(QtCore.QRect(10, 190, 300, 16))
        self.device_name.setObjectName("device_name")
        self.android_version = QtWidgets.QLabel(self.frame)
        self.android_version.setGeometry(QtCore.QRect(10, 210, 300, 16))
        self.android_version.setObjectName("android_version")
        self.text_case = QtWidgets.QLabel(self.frame)
        self.text_case.setGeometry(QtCore.QRect(10, 230, 300, 16))
        self.text_case.setText("")
        self.text_case.setObjectName("text_case")
        self.text_invest = QtWidgets.QLabel(self.frame)
        self.text_invest.setGeometry(QtCore.QRect(10, 250, 300, 16))
        self.text_invest.setText("")
        self.text_invest.setObjectName("text_invest")
        self.text_desc = QtWidgets.QLabel(self.frame)
        self.text_desc.setGeometry(QtCore.QRect(10, 270, 300, 16))
        self.text_desc.setText("")
        self.text_desc.setObjectName("text_desc")
        self.text_date = QtWidgets.QLabel(self.frame)
        self.text_date.setGeometry(QtCore.QRect(10, 290, 300, 16))
        self.text_date.setText("")
        self.text_date.setObjectName("text_date")
        self.text_device = QtWidgets.QLabel(self.frame)
        self.text_device.setGeometry(QtCore.QRect(10, 310, 300, 16))
        self.text_device.setText("")
        self.text_device.setObjectName("text_device")
        self.text_version = QtWidgets.QLabel(self.frame)
        self.text_version.setGeometry(QtCore.QRect(10, 330, 300, 16))
        self.text_version.setText("")
        self.text_version.setObjectName("text_version")
        self.case_hash = QtWidgets.QLabel(self.frame)
        self.case_hash.setGeometry(QtCore.QRect(10, 230, 300, 16))
        self.case_hash.setText("")
        self.case_hash.setObjectName("case_hash")
        self.Bbrand = QtWidgets.QLabel(self.frame)
        self.Bbrand.setGeometry(QtCore.QRect(10, 250, 300, 16))
        self.Bbrand.setObjectName("Device_Brand")
        self.Mmodel = QtWidgets.QLabel(self.frame)
        self.Mmodel.setGeometry(QtCore.QRect(10, 270, 300, 16))
        self.Mmodel.setObjectName("Device_Model")
        self.Ccountry = QtWidgets.QLabel(self.frame)
        self.Ccountry.setGeometry(QtCore.QRect(10, 290, 300, 16))
        self.Ccountry.setObjectName("Country")

        self.case_name.raise_()
        self.Investigator_name.raise_()
        self.case_descrition.raise_()
        self.date.raise_()
        self.device_name.raise_()
        self.android_version.raise_()
        self.text_case.raise_()
        self.text_invest.raise_()
        self.text_desc.raise_()
        self.text_date.raise_()
        self.text_device.raise_()
        self.text_version.raise_()
        self.case_hash.raise_()
        self.Bbrand.raise_()
        self.Mmodel.raise_()
        self.Ccountry.raise_()

        self.photo.raise_()
        self.report_table.raise_()
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setGeometry(QtCore.QRect(190, 530, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.download_button.setFont(font)
        self.download_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.download_button.setStyleSheet("QPushButton::hover"
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
        self.download_button.setObjectName("download_button")

        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setGeometry(QtCore.QRect(510, 530, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.cancel_button.setFont(font)
        self.cancel_button.setStyleSheet("QPushButton::hover"
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
        self.cancel_button.setObjectName("cancel_button")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 787, 21))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, generate_report):

        _translate = QtCore.QCoreApplication.translate
        generate_report.setWindowTitle(_translate("generate_report", "MainWindow"))
        item = self.report_table.verticalHeaderItem(0)
        item.setText(_translate("generate_report", "1"))
        item = self.report_table.horizontalHeaderItem(0)
        item.setText(_translate("generate_report", "Investigator comments"))
        item = self.report_table.horizontalHeaderItem(1)
        item.setText(_translate("generate_report", "Evidence source"))
        item = self.report_table.horizontalHeaderItem(2)
        item.setText(_translate("generate_report", "Evidence"))
        item = self.report_table.horizontalHeaderItem(3)
        item.setText(_translate("generate_report", "Sender name"))
        item = self.report_table.horizontalHeaderItem(4)
        item.setText(_translate("generate_report", "Receiver/Channel/Group name"))
        item = self.report_table.horizontalHeaderItem(5)
        item.setText(_translate("generate_report", "Timestamp"))
        self.case_name.setText(_translate("generate_report", "Case Name: "))
        self.Investigator_name.setText(_translate("generate_report", "Investigator Name:"))
        self.case_descrition.setText(_translate("generate_report", "Case Description:"))
        self.date.setText(_translate("generate_report", "Date:"))
        self.device_name.setText(_translate("generate_report", "Device Name:"))
        self.android_version.setText(_translate("generate_report", "Android Version:"))
        self.case_hash.setText(_translate("generate_report", "Hash:"))
        self.Bbrand.setText(_translate("generate_report", "Device Brand"))
        self.Mmodel.setText(_translate("generate_report", "Device Model"))
        self.Ccountry.setText(_translate("generate_report", "Device Model"))
        self.download_button.setText(_translate("generate_report", "Download"))
        self.cancel_button.setText(_translate("generate_report", "Cancel"))
        self.download_button.clicked.connect(self.generatePDF)
        self.cancel_button.clicked.connect(self.closewindo)
        self.case_name.setText('Case Name: ' + self.casename)
        self.Investigator_name.setText('Investigator Name: ' + self.investigatorname)
        self.case_descrition.setText('Case Description: ' + self.casedescription)
        self.device_name.setText('Device Name: ' + self.devicename)
        self.android_version.setText('Android Version: ' + self.androidversion)
        self.case_hash.setText('Hash: ' + self.hashed)
        self.date.setText('Date: ' + self.dated)
        self.Bbrand.setText('Device Brand: ' + self.brand)
        self.Mmodel.setText('Device Model: ' + self.model)
        self.Ccountry.setText('Country: ' + self.country)
        self.case_name.adjustSize()
        self.Investigator_name.adjustSize()
        self.case_descrition.adjustSize()
        self.device_name.adjustSize()
        self.android_version.adjustSize()
        self.date.adjustSize()
        self.Bbrand.adjustSize()
        self.Mmodel.adjustSize()
        self.Ccountry.adjustSize()

        self.report_table.setColumnCount(6)
        self.report_table.setRowCount(len(self.list))

        row = 0
        for oj in self.list:
            self.report_table.setItem(row, 0, QTableWidgetItem(oj.comment))
            self.report_table.setItem(row, 1, QTableWidgetItem(oj.type))
            self.report_table.setItem(row, 2, QTableWidgetItem(oj.content))
            self.report_table.setItem(row, 3, QTableWidgetItem(oj.sendername))
            self.report_table.setItem(row, 4, QTableWidgetItem(oj.recivedname))
            self.report_table.setItem(row, 5, QTableWidgetItem(oj.timestamp))
            row = row + 1


    def closewindo(self):
        self.close()

    def generatePDF(self):

        if len(self.list) > 0:
            import hashlib
            conversion = tuple(self.list)

            sha256 = hashlib.sha256()
            for x in conversion:
                sha256 .update(x.msgID.encode()+x.sendername.encode()+x.recivedname.encode()+x.timestamp.encode()+x.content.encode()+x.type.encode())
            digested_hash = sha256 .hexdigest()
            self.hashed = digested_hash
            self.case_hash.setText('Hash: ' + self.hashed)
            self.case_hash.adjustSize()

            pdf = PDF('P', 'mm', (300, 500))
            pdf.alias_nb_pages()

            pdf.add_page()

            pdf.cell(40, 10, 'Case Name: ' + self.casename, 0, 0, 'L')
            pdf.ln(10)
            pdf.cell(40, 10, 'Investigator Name: ' + self.investigatorname, 0, 0, 'L')
            pdf.ln(10)
            pdf.cell(40, 10, 'Case Description: ' + self.casedescription, 0, 0, 'L')
            pdf.ln(10)
            pdf.cell(40, 10, 'Device Name: ' + self.devicename, 0, 0, 'L')
            pdf.ln(10)
            pdf.cell(40, 10, 'Device Brand: ' + self.brand, 0, 0, 'L')
            pdf.ln(10)
            pdf.cell(40, 10, 'Device Model: ' + self.model, 0, 0, 'L')
            pdf.ln(10)
            pdf.cell(40, 10, 'Android Version: ' + self.androidversion, 0, 0, 'L')
            pdf.ln(10)
            pdf.cell(40, 10, 'Country: ' + self.country, 0, 0, 'L')
            pdf.ln(10)
            pdf.cell(40, 10, 'Date: ' + self.dated, 0, 0, 'L')
            pdf.ln(10)

            pdf.cell(40, 10, 'Hash Value: ' + self.hashed, 0, 0, 'L')
            pdf.ln(10) #linebreak

            lineNumber = 0 #EvidenceCounter
            for oj in self.list:
                pdf.set_text_color(253, 7, 7)
                pdf.multi_cell(250, 10, txt='Evidence#: ' + str(lineNumber + 1), border=1)
                pdf.set_text_color(0, 0, 255)
                pdf.multi_cell(250, 10, txt='Investigator comments', border=1)
                pdf.set_text_color(0, 0, 0)
                pdf.multi_cell(250, 10, txt=oj.comment, border=1)
                pdf.set_text_color(0, 0, 255)
                pdf.multi_cell(250, 10, txt='Evidence Source', border=1)
                pdf.set_text_color(0, 0, 0)
                pdf.multi_cell(250, 10, txt=oj.type, border=1)
                pdf.set_text_color(0, 0, 255)
                pdf.multi_cell(250, 10, txt='Evidence', border=1)

                if oj.filePath != "":
                    pdf.cell(15, 10, 'view', border=1, ln=0, link=os.path.abspath(os.getcwd())+"//"+oj.filePath) #media

                    pdf.set_text_color(0, 0, 0)
                    regrex_pattern = re.compile(pattern="["
                                                        u"\U0001F600-\U0001F64F"  # emoticons
                                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                                        "]+", flags=re.UNICODE)  # remove any symbols in the username
                    pdf.multi_cell(250, 10, txt=regrex_pattern.sub(r'', oj.content), border=1)



                else:
                    pdf.set_text_color(0, 0, 0)
                    regrex_pattern = re.compile(pattern="["
                                                        u"\U0001F600-\U0001F64F"  # emoticons
                                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                                        "]+", flags=re.UNICODE)  # remove any symbols in the username
                    pdf.multi_cell(250, 10, txt=regrex_pattern.sub(r'', oj.content), border=1)

                pdf.set_text_color(0, 0, 255)
                pdf.multi_cell(250, 10, txt='Sender name', border=1)
                pdf.set_text_color(0, 0, 0)
                regrex_pattern = re.compile(pattern="["
                                                    u"\U0001F600-\U0001F64F"  # emoticons
                                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                                    "]+", flags=re.UNICODE)  # remove any symbols in the username
                pdf.multi_cell(250, 10, txt=regrex_pattern.sub(r'', oj.sendername), border=1)
                pdf.set_text_color(0, 0, 255)
                if oj.type == "Channels":
                    pdf.multi_cell(250, 10, txt='Channel name', border=1) #header
                elif oj.type == "Groups":
                    pdf.multi_cell(250, 10, txt='Group name', border=1)
                else:
                    pdf.multi_cell(250, 10, txt='Receiver name', border=1)
                pdf.set_text_color(0, 0, 0)
                regrex_pattern = re.compile(pattern="["
                                                    u"\U0001F600-\U0001F64F"  # emoticons
                                                    u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                                    u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                                    u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                                    "]+", flags=re.UNICODE) #remove any symbols in the username
                pdf.multi_cell(250, 10, txt=regrex_pattern.sub(r'', oj.recivedname), border=1)
                pdf.set_text_color(0, 0, 255)
                pdf.multi_cell(250, 10, txt='Timestamp', border=1)
                pdf.set_text_color(0, 0, 0)
                pdf.multi_cell(250, 10, txt=oj.timestamp, border=1)

                pdf.ln(15)

                lineNumber += 1

            pdf.set_text_color(0, 0, 0)

            pdf.cell(50, 10, txt='Number of Evidence: ' + str(lineNumber), border=0, ln=0)

            pdf.ln(15)

            pdf.output("Report_" + str(dtf_string) + ".pdf", 'F')  # output pdf
            os.startfile("Report_" + str(dtf_string) + ".pdf")  # to open it
            self.list.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_generate_report('', '', '', '', '', '', '', '', '', '', '')
    ui.setupUi()
    ui.setWindowFlags(ui.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint) 
    ui.show()
    sys.exit(app.exec_())
