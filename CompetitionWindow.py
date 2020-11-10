
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from FileHandle import FileEncrytion
from datetime import datetime
class CompetitionWindow(object):
    def __init__(self,path,compName,userId):
        self.compName=compName
        self.userId=userId
        self.path=path

    def SetupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 589)
        MainWindow.setStyleSheet("background-color: rgb(39, 44, 54);\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setStyleSheet("background-color: rgb(27, 29, 35);\n")
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comp_name_text = QtWidgets.QLabel(self.widget)
        self.comp_name_text.setStyleSheet("font: 12pt \"Droid Sans Fallback\";\ncolor:rgb(255, 255, 255);")
        self.comp_name_text.setObjectName("exam_name_text")
        self.horizontalLayout_3.addWidget(self.comp_name_text)
        self.time_text = QtWidgets.QLabel(self.widget)
        self.time_text.setStyleSheet("font: 12pt \"Droid Sans Fallback\";\n""color:rgb(255, 255, 255);")
        self.time_text.setAlignment(QtCore.Qt.AlignCenter)
        self.time_text.setObjectName("time_text")
        self.horizontalLayout_3.addWidget(self.time_text)
        self.userid_text = QtWidgets.QLabel(self.widget)
        self.userid_text.setStyleSheet("font: 12pt \"Droid Sans Fallback\";\n""color:rgb(255, 255, 255);")
        self.userid_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userid_text.setObjectName("userid_text")
        self.horizontalLayout_3.addWidget(self.userid_text)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.widget)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("border:none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.language_choose = QtWidgets.QComboBox(self.frame)
        self.language_choose.setMaximumSize(QtCore.QSize(100, 16777215))
        self.language_choose.setToolTip("")
        self.language_choose.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.language_choose.setStyleSheet("QComboBox{\nbackground-color: rgb(27, 29, 35);\nborder-radius: 7px;\nborder: 2px solid rgb(27, 29, 35);\npadding: 5px;\npadding-left: 10px;\ntext-color: rgb(255,255,255);\ncolor: rgb(255,255,255);\n}\nQComboBox:hover{\nborder: 2px solid rgb(64, 71, 88);\n}")
        self.language_choose.setEditable(False)
        self.language_choose.setObjectName("language_choose")
        self.verticalLayout.addWidget(self.language_choose)
        self.language_choose.currentIndexChanged.connect(self.changeLanguage)
        self.program_text = QtWidgets.QTextEdit(self.frame)
        self.program_text.setStyleSheet("QTextEdit{\ncolor:rgb(255, 255, 255);\nfont: 12pt \"Droid Sans Fallback\";\nborder: 2px solid rgb(64, 71, 88);\n}")
        self.program_text.setObjectName("program_text")
        self.verticalLayout.addWidget(self.program_text)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.run_button = QtWidgets.QPushButton(self.frame)
        self.run_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.run_button.setStyleSheet("QPushButton {\nfont: 14pt \"Droid Sans Fallback\";\nbackground-position: center;\nbackground-repeat: no-reperat;\nborder: 2px solid rgb(64, 71, 88);\nborder-radius:7px;\ncolor:rgb(255, 255, 255);\nbackground-color:rgb(0, 85, 255);\n}QPushButton:hover {\nbackground-color: rgb(0, 67, 200);\n}\nQPushButton:pressed {\nbackground-color: rgb(0, 32, 97);\n}")
        self.run_button.setObjectName("run_button")
        self.horizontalLayout.addWidget(self.run_button)
        self.submit_button = QtWidgets.QPushButton(self.frame)
        self.submit_button.setMaximumSize(QtCore.QSize(150, 16777215))
        self.submit_button.setStyleSheet("QPushButton {\nfont: 14pt \"Droid Sans Fallback\";\nbackground-position: center;\nbackground-repeat: no-reperat;\nborder: 2px solid rgb(64, 71, 88);\nborder-radius:7px;\ncolor:rgb(255, 255, 255);\nbackground-color:rgb(0, 85, 255);\n}\nQPushButton:hover{\nbackground-color: rgb(0, 67, 200);\n\n}\nQPushButton:pressed {\nbackground-color: rgb(0, 32, 97);\n}")
        self.submit_button.setObjectName("submit_button")
        self.horizontalLayout.addWidget(self.submit_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.question_tab = QtWidgets.QTabWidget(self.frame)
        self.question_tab.setStyleSheet("color:rgb(255, 255, 255);\nfont: 9pt \"Droid Sans Fallback\";\nborder: none;")
        self.question_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.question_tab.setDocumentMode(False)
        self.question_tab.setTabsClosable(False)
        self.question_tab.setMovable(True)
        self.question_tab.setTabBarAutoHide(False)
        self.question_tab.setObjectName("question_tab")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.text_browser = QtWidgets.QTextBrowser(self.tab)
        self.text_browser.setStyleSheet("QTextBrowser{\ncolor:rgb(255, 255, 255);\nfont: 12pt \"Droid Sans Fallback\";\n}")
        self.text_browser.setObjectName("text_browser")
        self.gridLayout.addWidget(self.text_browser, 0, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/cil-check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.question_tab.addTab(self.tab, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.question_tab.addTab(self.tab_2, icon, "")
        self.verticalLayout_3.addWidget(self.question_tab)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.question_tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.program_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans Fallback\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">xvxvxvx546475  uksgakjhj  jkjfgahfg kgafg</p></body></html>"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.submit_button.setText(_translate("MainWindow", "Submit"))
        self.text_browser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Droid Sans Fallback\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" background-color:transparent;\">You are given a tree with N nodes (numbered 1 through N). A tree is a connected undirected graph without cycles.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">You have to assign an integer to each node; for each valid i, let\'s denote the integer assigned to node i by Ai. This assignment must satisfy the following conditions:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">For each valid i, 1≤Ai≤105.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">For each simple path in the tree which contains at least two nodes, let\'s denote the set of nodes in this path by S. Then, ∑v∈SAv is not divisible by |S|.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">Input</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">The first line of each test case contains a single integer N.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">Each of the next N−1 lines contains two space-separated integers u and v denoting that nodes u and v are connected by an edge.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">Output</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">For each test case, print a single line containing N space-separated integers A1,A2,…,AN.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">If there are multiple solutions, you may find any one of them. It can be proved that a solution always exists under the given constraints.</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">Constraints</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">1≤T≤200</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">2≤N≤100</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">1≤u,v≤N</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">Example Input</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">2</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">7</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">1 2</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">4 6</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">3 5</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">1 4</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">7 5</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">5 1</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">3</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">1 2xxx1212dd have </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">2 3</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">Example Output</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">4 9 12 1 9 8 4</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:100%; background-color:transparent;\"><span style=\" background-color:transparent;\">4 3 6</span></p></body></html>"))
        self.question_tab.setTabText(self.question_tab.indexOf(self.tab), _translate("MainWindow", "q1"))
        self.question_tab.setTabText(self.question_tab.indexOf(self.tab_2), _translate("MainWindow", "Question 1"))


    def LoadSettings(self):
        self.file=FileEncrytion()
        self.file.LoadKey('competitions/'+self.compName+'/settings')
        self.key=self.file.key
        self.settings=self.file.LoadSettings('competitions/'+self.compName+'/settings')

    def StartCompetition(self,mainWindow):
        self.LoadSettings()
        self.parentMainWindow=mainWindow
        if self.settings['starting-time']!=None:##testing korte hbe
            while datetime.now().time() < datetime.strptime(self.settings['starting-time'],'%H:%M:%S').time():
                pass
        self.SetupUi(self.parentMainWindow)
        self.comp_name_text.setText(self.compName)
        self.time_text.setText(str(self.settings['duration']))###########need to be modified
        self.userid_text.setText(self.userId)
        self.language_choose.addItems(self.settings['languages'])

    def changeLanguage(self):
        self.program_text.setText(self.language_choose.currentText())
