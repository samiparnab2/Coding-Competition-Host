
import os,sys
from typing import Set
from PyQt5 import QtCore, QtGui, QtWidgets
from CompetitionWindow import CompetitionWindow
class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.SetupUi()

    def SetupUi(self):
        self.setWindowTitle("Coding-Host(Log In)")
        self.resize(949, 451)
        self.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_13.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 12pt \"Droid Sans Fallback\";\n"
"")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.layoutWidget_6 = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget_6.setGeometry(QtCore.QRect(20, 32, 421, 251))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_14.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 12pt \"Droid Sans Fallback\";\n"
"")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_10.addWidget(self.label_14)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.adminid_text = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.adminid_text.setStyleSheet("QLineEdit{\n"
"    border:none;\n"
"border-bottom: 2px solid rgb(187, 205, 255);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.adminid_text.setObjectName("adminid_text")
        self.horizontalLayout_10.addWidget(self.adminid_text)
        self.verticalLayout_12.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_15.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 12pt \"Droid Sans Fallback\";\n"
"")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_11.addWidget(self.label_15)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.admin_password_text = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.admin_password_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.admin_password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.admin_password_text.setStyleSheet("QLineEdit{\n"
"    border:none;\n"
"border-bottom: 2px solid rgb(187, 205, 255);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.admin_password_text.setObjectName("admin_password_text")
        self.horizontalLayout_11.addWidget(self.admin_password_text)
        self.verticalLayout_12.addLayout(self.horizontalLayout_11)
        self.verticalLayout_11.addLayout(self.verticalLayout_12)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_16.setMinimumSize(QtCore.QSize(211, 31))
        self.label_16.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 12pt \"Droid Sans Fallback\";\n"
"")
        self.label_16.setText("")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_12.addWidget(self.label_16)
        self.admin_login_button = QtWidgets.QPushButton(self.layoutWidget_6)
        self.admin_login_button.setMinimumSize(QtCore.QSize(100, 40))
        self.admin_login_button.setMaximumSize(QtCore.QSize(100, 40))
        self.admin_login_button.clicked.connect(self.AdminLogin)
        self.admin_login_button.setStyleSheet("QPushButton {\n"
"font: 14pt \"Droid Sans Fallback\";\n"
"background-position: center;\n"
"background-repeat: no-reperat;\n"
"border: 2px solid rgb(64, 71, 88);\n"
"border-radius:7px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 85, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 67, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 32, 97);\n"
"}")
        self.admin_login_button.setObjectName("admin_login_button")
        self.horizontalLayout_12.addWidget(self.admin_login_button)
        self.verticalLayout_11.addLayout(self.horizontalLayout_12)
        self.verticalLayout_10.addWidget(self.frame_4)
        self.horizontalLayout.addLayout(self.verticalLayout_10)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_9.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 12pt \"Droid Sans Fallback\";\n"
"")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.layoutWidget_4 = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget_4.setGeometry(QtCore.QRect(20, 32, 421, 251))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_10.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 12pt \"Droid Sans Fallback\";\n"
"")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.userid_text = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.userid_text.setStyleSheet("QLineEdit{\n"
"    border:none;\n"
"border-bottom: 2px solid rgb(187, 205, 255);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.userid_text.setObjectName("userid_text")
        self.horizontalLayout_7.addWidget(self.userid_text)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_17.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 12pt \"Droid Sans Fallback\";\n"
"")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_13.addWidget(self.label_17)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.examname_text = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.examname_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.examname_text.setStyleSheet("QLineEdit{\n"
"    border:none;\n"
"border-bottom: 2px solid rgb(187, 205, 255);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.examname_text.setObjectName("examname_text")
        self.horizontalLayout_13.addWidget(self.examname_text)
        self.verticalLayout_9.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_11.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 12pt \"Droid Sans Fallback\";\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        spacerItem4 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.user_password_text = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.user_password_text.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.user_password_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.user_password_text.setStyleSheet("QLineEdit{\n"
"    border:none;\n"
"border-bottom: 2px solid rgb(187, 205, 255);\n"
"color:rgb(255, 255, 255);\n"
"}")
        self.user_password_text.setObjectName("user_password_text")
        self.horizontalLayout_8.addWidget(self.user_password_text)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout_8.addLayout(self.verticalLayout_9)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_12.setMinimumSize(QtCore.QSize(211, 31))
        self.label_12.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 12pt \"Droid Sans Fallback\";\n"
"")
        self.label_12.setText("")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.user_login_button = QtWidgets.QPushButton(self.layoutWidget_4)
        self.user_login_button.setMinimumSize(QtCore.QSize(100, 40))
        self.user_login_button.setMaximumSize(QtCore.QSize(100, 40))
        self.user_login_button.clicked.connect(self.UserLogin)
        self.user_login_button.setStyleSheet("QPushButton {\n"
"font: 14pt \"Droid Sans Fallback\";\n"
"background-position: center;\n"
"background-repeat: no-reperat;\n"
"border: 2px solid rgb(64, 71, 88);\n"
"border-radius:7px;\n"
"color:rgb(255, 255, 255);\n"
"background-color:rgb(0, 85, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 67, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(0, 32, 97);\n"
"}")
        self.user_login_button.setObjectName("user_login_button")
        self.horizontalLayout_9.addWidget(self.user_login_button)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.horizontalLayout.addLayout(self.verticalLayout_7)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_13.setText(_translate("MainWindow", "Admin Login"))
        self.label_14.setText(_translate("MainWindow", "Admin ID"))
        self.adminid_text.setPlaceholderText(_translate("MainWindow", "Enter Admin ID"))
        self.label_15.setText(_translate("MainWindow", "Password"))
        self.admin_password_text.setPlaceholderText(_translate("MainWindow", "Enter Admin Password"))
        self.admin_login_button.setText(_translate("MainWindow", "Login"))
        self.label_9.setText(_translate("MainWindow", "User Login"))
        self.label_10.setText(_translate("MainWindow", "User ID          "))
        self.userid_text.setPlaceholderText(_translate("MainWindow", "Enter User ID"))
        self.label_17.setText(_translate("MainWindow", "Exam Name "))
        self.examname_text.setPlaceholderText(_translate("MainWindow", "Enter Exam Name"))
        self.label_11.setText(_translate("MainWindow", "Password      "))
        self.user_password_text.setPlaceholderText(_translate("MainWindow", "Enter User Password"))
        self.user_login_button.setText(_translate("MainWindow", "Login"))
    def AdminLogin(self):
        pass
    def UserLogin(self):
        self.competitionUI=CompetitionWindow(os.popen('pwd').read().strip(),'NewExam','user@123')
        self.close()
        
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    loginUI=LoginWindow()
    sys.exit(app.exec_())