import mainUI
import sql
from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import os

sql.start()

pyqt6_path = os.path.dirname(QtWidgets.__file__)
plugin_path = os.path.join(pyqt6_path, 'Qt6', 'plugins')
if not os.path.exists(plugin_path):
    plugin_path = os.path.join(pyqt6_path, 'Qt', 'plugins')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog1 = QtWidgets.QDialog()
    ui = mainUI.Ui_Dialog1()
    ui.setupUi(Dialog1)
    Dialog1.show()
    sys.exit(app.exec())