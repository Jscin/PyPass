from PyQt5 import QtCore, QtGui, QtWidgets
from serial_cypher import File_Manager as FM
import os
import PyPass_Update_Window as PUW
import datetime


class Ui_MainWindow(object):
    def __init__(self):
        self._crypter = FM()

    def _Update_Window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = PUW.Ui_UpdateWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.MainWindow.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 618)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "font: 11pt \"Segoe UI\";")
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        MainWindow.setWindowIcon(QtGui.QIcon(
            scriptDir + os.path.sep + 'locked.ico'))
        self.MainWindow = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.p_label = QtWidgets.QLabel(self.centralwidget)
        self.p_label.setObjectName("p_label")

        self.gridLayout.addWidget(self.p_label, 1, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)

        self.passwords = QtWidgets.QLineEdit(self.centralwidget)
        self.passwords.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "gridline-color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(80, 80, 80);\n"
                                     "border-radius: 5px;")

        self.passwords.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwords.setObjectName("passwords")

        self.gridLayout.addWidget(self.passwords, 2, 2, 1, 1)
        self.acc_label = QtWidgets.QLabel(self.centralwidget)
        self.acc_label.setObjectName("acc_label")

        self.gridLayout.addWidget(self.acc_label, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 7, 4, 1, 1)

        self.index_input = QtWidgets.QLineEdit(self.centralwidget)
        self.index_input.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "gridline-color: rgb(0, 0, 0);\n"
                                       "background-color: rgb(80, 80, 80);\n"
                                       "border-radius: 5px;")
        self.index_input.setObjectName("index_input")

        self.gridLayout.addWidget(self.index_input, 4, 3, 1, 1)
        self.index_label = QtWidgets.QLabel(self.centralwidget)
        self.index_label.setObjectName("index_label")

        self.gridLayout.addWidget(self.index_label, 3, 3, 1, 1)
        self.remove_user = QtWidgets.QPushButton(self.centralwidget)
        self.remove_user.setStyleSheet("color: rgb(255, 255, 255);\n"
                                       "background-color: rgb(79, 79, 79);")
        self.remove_user.setObjectName("remove_user")
        self.remove_user.clicked.connect(self.remove)

        self.gridLayout.addWidget(self.remove_user, 4, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 5, 3, 1, 1)

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setMovement(QtWidgets.QListView.Static)
        self.listWidget.setResizeMode(QtWidgets.QListView.Adjust)
        self.listWidget.setObjectName("listWidget")
        item = "None"
        if len(self._crypter.load_data()[0]) > 1:
            self.show_accounts()
            del item
        else:
            self.listWidget.addItem(item)

        self.gridLayout.addWidget(self.listWidget, 4, 1, 4, 2)

        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(79, 79, 79);")
        self.add_button.setObjectName("add_button")
        self.add_button.clicked.connect(self.add_user)

        self.gridLayout.addWidget(self.add_button, 2, 3, 1, 1)

        self.usernames = QtWidgets.QLineEdit(self.centralwidget)
        self.usernames.setStyleSheet("color: rgb(255, 255, 255);\n"
                                     "gridline-color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(80, 80, 80);\n"
                                     "border-radius: 5px;")
        self.usernames.setObjectName("usernames")

        self.gridLayout.addWidget(self.usernames, 2, 1, 1, 1)

        self.update_login = QtWidgets.QPushButton(self.centralwidget)
        self.update_login.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(79, 79, 79);")
        self.update_login.setObjectName("update_login")
        self.update_login.clicked.connect(self._Update_Window)

        self.gridLayout.addWidget(self.update_login, 6, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 4, 0, 3, 1)
        spacerItem11 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 6, 5, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 4, 5, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 8, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 5, 5, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem15, 2, 5, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem16, 0, 4, 1, 2)

        self.u_label = QtWidgets.QLabel(self.centralwidget)
        self.u_label.setObjectName("u_label")

        self.gridLayout.addWidget(self.u_label, 1, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem17, 3, 5, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem18, 8, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.p_label.setText(_translate("MainWindow", "Password:"))
        self.acc_label.setText(_translate("MainWindow", "Accounts:"))
        self.index_label.setText(_translate("MainWindow", "Index to Remove:"))
        self.remove_user.setText(_translate("MainWindow", "Remove User"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(True)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.add_button.setText(_translate("MainWindow", "Add User"))
        self.update_login.setText(_translate("MainWindow", "Update Login"))
        self.u_label.setText(_translate("MainWindow", "Username:"))

    def show_accounts(self):
        data = self._crypter.load_data()
        users, passes, keys, accounts = data[0], data[1], data[2], list()

        for index in range(len(keys)):
            if index == 0:
                continue
            else:
                accounts.append(
                    str(index) +
                    " Username: " +
                    self._crypter.decrypt(users[index], keys[index]) +
                    " Password: " +
                    self._crypter.decrypt(passes[index], keys[index]) +
                    " Date Added: " +
                    str(data[3][index]))

        self.listWidget.clear()
        if len(keys) == 1:
            self.listWidget.addItem("None")
        else:
            self.listWidget.addItems(accounts)

    def remove(self):
        try:
            index = int(self.index_input.text())
            if index != 0:
                data = self._crypter.load_data()
                for li in range(len(data)):
                    data[li].remove(data[li][index])
                self._crypter.dump_data(data)
            self.show_accounts()
            self.index_input.clear()
        except ValueError:
            self.index_input.clear()
        except IndexError:
            self.index_input.clear()

    def add_user(self):
        data = self._crypter.load_data()
        key = self._crypter.gen_key()
        user_names, pass_words, keys = list(
            data[0]), list(data[1]), list(data[2])
        date = datetime.datetime.now()
        data[0].append(self._crypter.encrypt(self.usernames.text(), key))
        data[1].append(self._crypter.encrypt(self.passwords.text(), key))
        data[2].append(key)
        data[3].append(date.strftime("%x"))
        self._crypter.dump_data(data)
        self.usernames.clear()
        self.passwords.clear()
        self.show_accounts()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())