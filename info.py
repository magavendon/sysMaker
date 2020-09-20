from PySide2.QtCore import Signal
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QToolButton
from PySide2.QtWidgets import QWidget

from font import Font

class InfoPanel(QWidget):
    toggle_menu = Signal()

    def __init__(self):
        # Parent class init
        QWidget.__init__(self)

        # Get instance of font
        sys_font = Font()
        sys_font.setPointSize(24)

        # Add menu button
        menu = QToolButton()
        menu.setIcon(QIcon('assets/hamburger.svg'))
        menu.pressed.connect(lambda: self.toggle_menu.emit())

        # Add title
        self.title = QLabel('System Maker')
        self.title.setFont(sys_font)

        # Create layout
        layout = QHBoxLayout()
        layout.addWidget(menu)
        layout.addWidget(self.title)
        self.setLayout(layout)
