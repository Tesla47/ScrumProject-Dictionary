# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import json
from difflib import get_close_matches
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
data=json.load(open("dictionary (1).json"))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1317, 750)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1351, 761))
        self.frame.setStyleSheet("background:#FFFFFF;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-10, 0, 141, 751))
        self.frame_2.setStyleSheet("QFrame {\n"
"background:#223363;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Btn_Toggle = QtWidgets.QPushButton(self.frame_2)
        self.Btn_Toggle.setGeometry(QtCore.QRect(10, 10, 131, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Btn_Toggle.sizePolicy().hasHeightForWidth())
        self.Btn_Toggle.setSizePolicy(sizePolicy)
        self.Btn_Toggle.setStyleSheet("border: 0px solid;\n"
"color: white;\n"
"font-family: times new roman;\n"
"font-style: italic;\n"
"background:#223363;\n"
"font-size:25px;")
        self.Btn_Toggle.setObjectName("Btn_Toggle")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(10, 170, 131, 41))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"background:#223363;\n"
"border-radius:10px;\n"
"font-size: 22px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:15px;\n"
"background:#007BFF;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 250, 131, 41))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"background:#223363;\n"
"border-radius:10px;\n"
"font-size: 22px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:15px;\n"
"background:#007BFF;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 330, 131, 41))
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"background:#223363;\n"
"border-radius:10px;\n"
"font-size: 22px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:15px;\n"
"background:#007BFF;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(170, 30, 1121, 691))
        self.stackedWidget.setStyleSheet("border-radius:30px;\n"
"background:#F3F6FF;\n"
"background-color:rgba(243,246,255);\n"
"backdrop-filter: blur(6px);\n"
"font-size: 30px;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label_1 = QtWidgets.QLabel(self.page)
        self.label_1.setGeometry(QtCore.QRect(40, 160, 361, 61))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("color: black;\n"
"font-size: 30px;")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.textEdit = QtWidgets.QLineEdit(self.page)
        self.textEdit.setGeometry(QtCore.QRect(30, 280, 391, 61))
        self.textEdit.setStyleSheet("border-radius:15px;\n"
"border: 1px solid grey;\n"
"text-align: center;\n"
"font-family: times new roman;\n"
"font-size: 20px;\n"
"color: black;\n"
"background-color: white;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.pushButton_4 = QtWidgets.QPushButton(self.page)
        self.pushButton_4.setGeometry(QtCore.QRect(140, 390, 161, 61))
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"background:#0068FF;\n"
"color:white;\n"
"font-size:22px;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"color:#333;\n"
"border-radius:15px;\n"
"background:#007BFF;\n"
"\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_3 = QtWidgets.QTextEdit(self.page)
        self.label_3.setGeometry(QtCore.QRect(540, 140, 561, 511))
        self.label_3.setStyleSheet("color: black;\n"
"font-family: times new roman;\n"
"font-size: 18px;\n"
"border: 1px solid gray;\n"
"background-color: white;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_15 = QtWidgets.QLabel(self.page_2)
        self.label_15.setGeometry(QtCore.QRect(20, 60, 981, 51))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: black;\n"
"font-family: times new roman;\n"
"font-size: 30px;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_21 = QtWidgets.QLabel(self.page_2)
        self.label_21.setGeometry(QtCore.QRect(20, 180, 731, 31))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: black;\n"
"font-family: times new roman;\n"
"font-size: 30px;")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_17 = QtWidgets.QLabel(self.page_2)
        self.label_17.setGeometry(QtCore.QRect(20, 340, 531, 31))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: black;\n"
"font-family: times new roman;\n"
"font-size: 30px;")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.page_2)
        self.label_19.setGeometry(QtCore.QRect(20, 400, 591, 31))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: black;\n"
"font-family: times new roman;\n"
"font-size: 30px;")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_16 = QtWidgets.QLabel(self.page_2)
        self.label_16.setGeometry(QtCore.QRect(10, 290, 631, 21))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: black;\n"
"font-family: times new roman;\n"
"font-size: 30px;")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.page_2)
        self.label_18.setGeometry(QtCore.QRect(0, 230, 571, 31))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: black;\n"
"font-family: times new roman;\n"
"font-size: 30px;")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.page_2)
        self.label_20.setGeometry(QtCore.QRect(30, 460, 561, 31))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: black;\n"
"font-family: times new roman;\n"
"font-size: 30px;")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_22 = QtWidgets.QLabel(self.page_2)
        self.label_22.setGeometry(QtCore.QRect(580, 600, 541, 61))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: black;\n"
"font-size: 30px;")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_23 = QtWidgets.QLabel(self.page_5)
        self.label_23.setGeometry(QtCore.QRect(20, 150, 991, 131))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color: black;\n"
"font-family: times new roman;\n"
"font-size: 30px;")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.page_5)
        self.label_24.setGeometry(QtCore.QRect(20, 280, 991, 111))
        font = QtGui.QFont()
        font.setFamily("times new roman")
        font.setPointSize(-1)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: black;\n"
"font-family: times new roman;\n"
"font-size: 30px;")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.stackedWidget.addWidget(self.page_5)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.setpage1)
        self.pushButton_2.clicked.connect(self.setpag2)
        self.pushButton_3.clicked.connect(self.setpag3)
        self.pushButton_4.clicked.connect(self.get_info)


    def setpage1(self):
        self.stackedWidget.setCurrentIndex(0)

    def setpag2(self):
        self.stackedWidget.setCurrentIndex(1)
    def setpag3(self):
        self.stackedWidget.setCurrentIndex(2)
    def get_info(self, word):
        word=self.textEdit.text()
        word.lower()
        if word in data:
            return self.label_3.setText(data[word])
        elif len(get_close_matches(word, data.keys())) > 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setText("Did you mean % s instead?" % get_close_matches(word, data.keys())[0])
            msg.setWindowTitle("MessageBox demo")
            msg.addButton(QMessageBox.Yes)
            msg.addButton(QMessageBox.No)
            reply=msg.exec()
            if reply ==QMessageBox.Yes:
                return self.label_3.setText(data[get_close_matches(word, data.keys())[0]])
            elif reply == QMessageBox.No:
                return self.label_3.setText("The word does not exist. Please double check it")
            else:
                return self.label_3.setText("We did not understand your entry")
        else:
            return self.label_3.setText("The dose not exist. Please double check it")
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dictionary"))
        self.Btn_Toggle.setText(_translate("Dialog", "Dictionary"))
        self.pushButton.setText(_translate("Dialog", "Home"))
        self.pushButton_2.setText(_translate("Dialog", "About"))
        self.pushButton_3.setText(_translate("Dialog", "Help"))
        self.label_1.setText(_translate("Dialog", "Insert the Word "))
        self.pushButton_4.setText(_translate("Dialog", "Search"))
        self.label_15.setText(_translate("Dialog", "This Dictionary is a project in software engineering class which is developed by:"))
        self.label_21.setText(_translate("Dialog", "- Sayed Shabeer Hashimi (Shabeer.hashimi@auaf.edu.af)"))
        self.label_17.setText(_translate("Dialog", "- Elyas Fekrat (elyas.fekrat@auaf.edu.af)"))
        self.label_19.setText(_translate("Dialog", "- Rayhana Amiri (rayhana.amiri@auaf.edu.af)"))
        self.label_16.setText(_translate("Dialog", "- Zahra Stanikzai (zahra.stanikzai@auaf.edu.af)"))
        self.label_18.setText(_translate("Dialog", "- Emal Ismail (emal.ismail@auaf.edu.af)"))
        self.label_20.setText(_translate("Dialog", "- Yousaf Sultani (yousaf.sultani@auaf.edu.af)"))
        self.label_22.setText(_translate("Dialog", "Supervised by: Ali Rahman Shinwari"))
        self.label_23.setText(_translate("Dialog", "Please insert the word you need to know the meaning and hit the search button."))
        self.label_24.setText(_translate("Dialog", "If you faced any kind of issue, please contact us through the emails provide in "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
