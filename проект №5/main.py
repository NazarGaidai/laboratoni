import sys
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from config import Ui_Dialog
from config_T import Ui_Dialog_Tables
from configOW import Ui_OtherWindow
from configOW_1 import Ui_OtherWindow_1
from configOW_2 import Ui_OtherWindow_2
from config_0 import Ui_Dialog_0

app = QtWidgets.QApplication(sys.argv)


Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

def open_T():
    global Dialog_Tables
    Dialog_Tables = QtWidgets.QDialog()
    ui = Ui_Dialog_Tables()
    ui.setupUi(Dialog_Tables)
    Dialog.close()
    Dialog_Tables.show()

    def open_0():
        global OtherWindow
        OtherWindow = QtWidgets.QDialog()
        ui = Ui_OtherWindow()
        ui.setupUi(OtherWindow)
        OtherWindow.show()


    ui.pushButton.clicked.connect(open_0)

    def open_1():
        global OtherWindow_1
        OtherWindow_1 = QtWidgets.QDialog()
        ui = Ui_OtherWindow_1()
        ui.setupUi(OtherWindow_1)
        OtherWindow_1.show()


    ui.pushButton_2.clicked.connect(open_1)

    def open_2():
        global OtherWindow_2
        OtherWindow_2 = QtWidgets.QDialog()
        ui = Ui_OtherWindow_2()
        ui.setupUi(OtherWindow_2)
        OtherWindow_2.show()


    ui.pushButton_3.clicked.connect(open_2)


    def exit():
        Dialog_Tables.close()
        Dialog.show()

    ui.pushButton_4.clicked.connect(exit)

ui.pushButton.clicked.connect(open_T)

def open_x():
    global Dialog_0
    Dialog_0 = QtWidgets.QDialog()
    ui = Ui_Dialog_0()
    ui.setupUi(Dialog_0)
    Dialog_0.show()


ui.pushButton_5.clicked.connect(open_x)

def open_g():
    img = Image.open('Figure_1.png')
    img.show()



ui.pushButton_2.clicked.connect(open_g)

def exit_q():
    Dialog.close()

ui.pushButton_4.clicked.connect(exit_q)


sys.exit(app.exec_())
