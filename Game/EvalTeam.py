# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Jay\Desktop\Fantasy_Cricket\Game\UI\EvalTeam.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sqlite3

cwd = os.getcwd()    # to get the location of file for any user
playerstat = sqlite3.connect(cwd + '/databases/stats.db')
statcursor = playerstat.cursor()
team = sqlite3.connect(cwd + '/databases/team.db')
teamcursor = team.cursor()
matches = sqlite3.connect(cwd + '/databases/matches.db')
matchcursor = matches.cursor()


class Ui_EvalTeam(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        cwd = os.getcwd()               # to get the location of file for any user
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(cwd + "/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.team_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.team_comboBox.setMinimumSize(QtCore.QSize(180, 30))
        self.team_comboBox.setObjectName("team_comboBox")
        self.horizontalLayout.addWidget(self.team_comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.match_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.match_comboBox.setMinimumSize(QtCore.QSize(180, 30))
        self.match_comboBox.setObjectName("match_comboBox")
        self.horizontalLayout.addWidget(self.match_comboBox)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setMinimumSize(QtCore.QSize(0, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.players = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.players.setFont(font)
        self.players.setObjectName("players")
        self.horizontalLayout_3.addWidget(self.players)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.points = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.points.setFont(font)
        self.points.setObjectName("points")
        self.horizontalLayout_3.addWidget(self.points)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem11)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.players_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.players_listWidget.setObjectName("players_listWidget")
        self.horizontalLayout_4.addWidget(self.players_listWidget)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.points_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.points_listWidget.setObjectName("points_listWidget")
        self.horizontalLayout_4.addWidget(self.points_listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.teamscore_label = QtWidgets.QLabel(self.centralwidget)
        self.teamscore_label.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        self.teamscore_label.setFont(font)
        self.teamscore_label.setObjectName("teamscore_label")
        self.horizontalLayout_5.addWidget(self.teamscore_label)
        self.teamscore = QtWidgets.QLCDNumber(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.teamscore.setFont(font)
        self.teamscore.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.teamscore.setFrameShadow(QtWidgets.QFrame.Plain)
        self.teamscore.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.teamscore.setProperty("intValue", 0)
        self.teamscore.setObjectName("teamscore")
        self.teamscore.setStyleSheet('color: blue')
        self.horizontalLayout_5.addWidget(self.teamscore)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Evaluate Team"))
        self.label.setText(_translate("MainWindow", "Evaluate the Performance of your Fantasy Team"))
        self.team_comboBox.insertItem(0,_translate('EvaluateWindow', "--SELECT TEAM--"))
        self.match_comboBox.insertItem(0,_translate('EvaluateWindow', "--SELECT MATCH--"))
        self.players.setText(_translate("MainWindow", "Players"))
        self.points.setText(_translate("MainWindow", "Points"))
        self.label_7.setText(_translate("MainWindow", "     >     "))
        self.teamscore_label.setText(_translate("MainWindow", "Your Team Points : "))
        
        
        teamcursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        team = teamcursor.fetchall()
        teamlist=[]
        for i in range(len(team)):           
            teamlist.append(team[i][0]) 
        for name in teamlist:
            self.team_comboBox.addItem(name)
            
        matchcursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        match = matchcursor.fetchall()
        matchlist=[]
        for i in range(len(match)):           
            matchlist.append(match[i][0]) 
        for name in matchlist:
            self.match_comboBox.addItem(name)
            
            
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_EvalTeam()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
