import sys

from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow

app = QApplication(['System Maker'])

main = MainWindow()
main.show()

sys.exit(app.exec_())
