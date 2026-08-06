from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import sql
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtCore import Qt


username = ""

class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(236, 107)
        self.denglu = QtWidgets.QPushButton(Dialog)
        self.denglu.setGeometry(QtCore.QRect(20, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.denglu.setFont(font)
        self.denglu.setObjectName("denglu")
        self.zhuce = QtWidgets.QPushButton(Dialog)
        self.zhuce.setGeometry(QtCore.QRect(130, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.zhuce.setFont(font)
        self.zhuce.setObjectName("zhuce")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.denglu.clicked.connect(self.open_window_denglu)
        self.zhuce.clicked.connect(self.open_window_zhuce)
        self.denglu_window = None
        self.zhuce_window = None

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "运动会管理系统"))
        self.denglu.setText(_translate("Dialog", "登录"))
        self.zhuce.setText(_translate("Dialog", "注册"))

    def open_window_denglu(self):
        self.denglu_window = QtWidgets.QDialog()
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self.denglu_window)
        self.denglu_window.show()

    def open_window_zhuce(self):
        self.zhuce_window = QtWidgets.QDialog()
        self.ui = Ui_Dialog3()
        self.ui.setupUi(self.zhuce_window)
        self.zhuce_window.show()

class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        self.truea = True
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 171)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 30, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 70, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 120, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.conect)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "用户登录"))
        self.label.setText(_translate("Dialog", "用户名："))
        self.label_2.setText(_translate("Dialog", "密码："))
        self.pushButton.setText(_translate("Dialog", "登录"))

    def show_main_window(self):
        if self.truea:
            self.main_window = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self.main_window)
            self.main_window.show()
            if self.user_info[2] == '总控':
                self.dialog = QtWidgets.QDialog()
                self.ui5 = Ui_Dialog5()
                self.ui5.setupUi(self.dialog)
                self.dialog.show()
            elif self.user_info[2] == '班主任':
                self.dialog = QtWidgets.QDialog()
                self.ui6 = Ui_Dialog6()
                self.ui6.setupUi(self.dialog)
                self.dialog.show()
            elif self.user_info[2] == '裁判':
                self.dialog = QtWidgets.QDialog()
                self.ui7 = Ui_Dialog7()
                self.ui7.setupUi(self.dialog)
                self.dialog.show()
        else:
            self.dialog = QtWidgets.QDialog()
            self.ui4 = Ui_Dialog4()
            self.ui4.setupUi(self.dialog)
            self.dialog.show()

    def conect(self):
        global username
        self.username = self.lineEdit.text().strip()
        username = self.username
        self.password = self.lineEdit_2.text().strip()
        self.user_info = sql.add_denglu(self.username, self.password)
        if self.user_info is not None:
            self.truea = True
            self.show_main_window()
        else:
            self.truea = False
            self.show_main_window()

class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 299)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 90, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.job = ['班主任','裁判']
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(120, 150, 241, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(self.job)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 50, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 220, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 200, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 250, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.intomain)
        self.pushButton.clicked.connect(self.show_main_window)
        self.pushButton.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "用户注册"))
        self.label_3.setText(_translate("Dialog", "职业"))
        self.label_2.setText(_translate("Dialog", "密码："))
        self.label.setText(_translate("Dialog", "用户名："))
        self.label_4.setText(_translate("Dialog", "班级："))
        self.label_5.setText(_translate("Dialog", "没有班级不填"))
        self.pushButton.setText(_translate("Dialog", "注册"))

    def intomain(self):
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        self.class_ = self.lineEdit_3.text()
        self.job = self.comboBox.currentText()
        sql.add_zhuce(self.username,self.password,self.job,self.class_)
        try:
            if self.class_[0] == 'A':
                sql.add_7(self.class_)
            elif self.class_[0] == 'B':
                sql.add_8(self.class_)
            elif self.class_[0] == 'C':
                sql.add_9(self.class_)
        except:
            pass

    def show_main_window(self):
        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_window.show()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 632)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 761, 551))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_5 = QtWidgets.QLabel(parent=self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 741, 501))
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(parent=self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 91, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(510, 10, 151, 16))
        self.label_3.setObjectName("label_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(parent=self.tab_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 30, 231, 481))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(sql.find_ranking_7()[1])
        self.tableWidget_3 = QtWidgets.QTableWidget(parent=self.tab_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(510, 30, 241, 481))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        self.tableWidget_3.setRowCount(sql.find_ranking_8()[1])
        self.tableWidget_4 = QtWidgets.QTableWidget(parent=self.tab_2)
        self.tableWidget_4.setGeometry(QtCore.QRect(250, 30, 241, 481))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(3)
        self.tableWidget_4.setRowCount(sql.find_ranking_9()[1])
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.comboBox = QtWidgets.QComboBox(parent=self.tab)
        self.comboBox.setGeometry(QtCore.QRect(580, 0, 171, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems([str(item[0]) for item in sql.find_sports()])
        self.label_4 = QtWidgets.QLabel(parent=self.tab)
        self.label_4.setGeometry(QtCore.QRect(480, 10, 81, 16))
        self.label_4.setObjectName("label_4")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 751, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tabWidget.addTab(self.tab, "")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 570, 101, 31))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.tableWidget_2.setHorizontalHeaderLabels(['班级','分数','排名'])
        self.tableWidget_3.setHorizontalHeaderLabels(['班级','分数','排名'])
        self.tableWidget_4.setHorizontalHeaderLabels(['班级','分数','排名'])
        self.tableWidget.setHorizontalHeaderLabels(['运动员','班级','总分'])
        try:
            for i in range(self.tableWidget_2.rowCount()):
                for j in range(self.tableWidget_2.columnCount()):
                    item = QtWidgets.QTableWidgetItem(sql.find_ranking_7()[0][i][j])
                    self.tableWidget_2.setItem(i, j, item)
            for a in range(self.tableWidget_4.rowCount()):
                for b in range(self.tableWidget_4.columnCount()):
                    item = QtWidgets.QTableWidgetItem(sql.find_ranking_8()[0][a][b])
                    self.tableWidget_4.setItem(a, b, item)
            for c in range(self.tableWidget_3.rowCount()):
                for d in range(self.tableWidget_3.columnCount()):
                    item = QtWidgets.QTableWidgetItem(sql.find_ranking_9()[0][c][d])
                    self.tableWidget_3.setItem(c, d, item)
        except:
            pass
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_4.horizontalHeader().setVisible(False)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.refresh_all)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p>主页</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate('MainWindow', "主页"))
        self.pixmap = QtGui.QPixmap("images\ground.jpg")
        self.label_5.setPixmap(self.pixmap)
        self.label_5.setScaledContents(True)
        self.label.setText(_translate("MainWindow", "七年级"))
        self.label_2.setText(_translate("MainWindow", "八年级"))
        self.label_3.setText(_translate("MainWindow", "九年级"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "班级排名"))
        self.label_4.setText(_translate("MainWindow", "运动项目"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "运动项目"))
        self.pushButton.setText(_translate("MainWindow", "刷新"))

    def refresh_all(self):
        data_7, count_7 = sql.find_ranking_7()
        self.tableWidget_2.setRowCount(count_7)
        for i in range(count_7):
            for j in range(3):
                item = QtWidgets.QTableWidgetItem(str(data_7[i][j]))
                self.tableWidget_2.setItem(i, j, item)
        
        data_8, count_8 = sql.find_ranking_8()
        self.tableWidget_4.setRowCount(count_8)
        for a in range(count_8):
            for b in range(3):
                item = QtWidgets.QTableWidgetItem(str(data_8[a][b]))
                self.tableWidget_4.setItem(a, b, item)
        
        data_9, count_9 = sql.find_ranking_9()
        self.tableWidget_3.setRowCount(count_9)
        for c in range(count_9):
            for d in range(3):
                item = QtWidgets.QTableWidgetItem(str(data_9[c][d]))
                self.tableWidget_3.setItem(c, d, item)

        current_sport = self.comboBox.currentText()
        if current_sport:
            data, count = sql.find_ranking_sporters(current_sport)
            self.tableWidget.setRowCount(count)
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setHorizontalHeaderLabels(['运动员', '班级', '总分'])
        
        for i in range(count):
            for j in range(6):
                item = QtWidgets.QTableWidgetItem(str(data[i][j]))
                self.tableWidget.setItem(i, j, item)
        self.statusbar.showMessage("所有数据已刷新", 2000)

class Ui_Dialog4(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(347, 230)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 50, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(120, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "提示"))
        self.label.setText(_translate("Dialog", "用户或密码错误"))
        self.pushButton.setText(_translate("Dialog", "OK"))

class Ui_Dialog5(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 443)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        Dialog.setFont(font)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 370, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 120, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(280, 220, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(390, 130, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton.clicked.connect(self.clean)
        self.pushButton_2.clicked.connect(self.addsports)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "管理员功能"))
        self.pushButton.setText(_translate("Dialog", "结束运动会清空数据"))
        self.label.setText(_translate("Dialog", "新增运动项目"))
        self.pushButton_2.setText(_translate("Dialog", "确认添加"))

    def clean(self):
        sql.clean_all()

    def addsports(self):
        text = self.lineEdit.text().strip()
        if text:
            sql.add_sports(text)
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog8()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

class Ui_Dialog6(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(769, 504)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 160, 54, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(352, 110, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 200, 54, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(180, 240, 54, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(348, 160, 161, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(350, 200, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(350, 250, 161, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(340, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        try:
            self.comboBox.addItems([str(item[0]) for item in sql.find_sports()])
            self.comboBox_2.addItems([str(item[0]) for item in sql.find_sports()])
            self.comboBox_3.addItems([str(item[0]) for item in sql.find_sports()])
        except:
            pass
        self.pushButton.clicked.connect(self.addsporter)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "运动员录入（班主任）"))
        self.label.setText(_translate("Dialog", "运动员名称："))
        self.label_2.setText(_translate("Dialog", "项目1："))
        self.label_3.setText(_translate("Dialog", "项目2："))
        self.label_4.setText(_translate("Dialog", "项目3："))
        self.pushButton.setText(_translate("Dialog", "保存"))

    def addsporter(self):
        global username
        name = self.lineEdit.text().strip()
        s1 = self.comboBox.currentText()
        s2 = self.comboBox_2.currentText()
        s3 = self.comboBox_3.currentText()
        class_ = sql.find_class(username)
        sql.add_sporter(name, class_, s1, s2, s3, 0)
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog8()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

class Ui_Dialog7(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(784, 511)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(510, 10, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(610, 20, 151, 31))
        self.comboBox.setObjectName("comboBox")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 80, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(370, 90, 181, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 150, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(372, 150, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(550, 150, 71, 16))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 310, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(260, 240, 54, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(370, 240, 121, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(260, 200, 54, 12))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.spinBox_2 = QtWidgets.QSpinBox(Dialog)
        self.spinBox_2.setGeometry(QtCore.QRect(370, 190, 121, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        try:
            self.comboBox.addItems([str(item[0]) for item in sql.find_sports()])
        except:
            pass
        self.comboBox.currentTextChanged.connect(self.update_sporter)
        self.pushButton.clicked.connect(self.addgrade)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def update_sporter(self):
        sport = self.comboBox.currentText()
        self.comboBox_2.clear()
        for name in sql.find_sporter(sport):
            self.comboBox_2.addItem(name)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "裁判成绩录入"))
        self.label.setText(_translate("Dialog", "项目："))
        self.label_2.setText(_translate("Dialog", "运动员："))
        self.label_3.setText(_translate("Dialog", "成绩："))
        self.checkBox.setText(_translate("Dialog", "破纪录"))
        self.pushButton.setText(_translate("Dialog", "保存"))
        self.label_4.setText(_translate("Dialog", "积分"))
        self.label_5.setText(_translate("Dialog", "排名："))

    def addgrade(self):
        name = self.comboBox_2.currentText()
        class_ = sql.find_class_(name)
        ranking = self.spinBox_2.value()
        sport = self.comboBox.currentText()
        score = self.spinBox.value()
        sql.add_grade(name,0,class_,ranking,sport,score)
        if class_[0] == 'A':
            self.start_scroe = int(sql.find_scroe_7(class_))
            self.start_scroe += score
            sql.update_7(class_, self.start_scroe, ranking)
        elif class_[0] == 'B':
            self.start_scroe = int(sql.find_scroe_8(class_))
            self.start_scroe += score
            sql.update_8(class_, self.start_scroe, ranking)
        elif class_[0] == 'C':
            self.start_scroe = int(sql.find_scroe_9(class_))
            self.start_scroe += score
            sql.update_9(class_, self.start_scroe, ranking)
        self.dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog8()
        self.ui.setupUi(self.dialog)
        self.dialog.show()

class Ui_Dialog8(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 50, 211, 101))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(72)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(130, 200, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "操作成功"))
        self.label.setText(_translate("Dialog", "成功"))
        self.pushButton.setText(_translate("Dialog", "OK"))