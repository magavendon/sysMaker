from PySide2.QtCore import Signal
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget

from font import Font

class Menu(QWidget):
    show = Signal(int)

    def __init__(self):
        # Parent class init
        QWidget.__init__(self)

    def set_menu(self, widgets):
        # Get font instance
        sys_font = Font()
        sys_font.setPointSize(14)

        # Create layout
        layout = QVBoxLayout()
        layout.setMargin(0)
        layout.setSpacing(0)

        # Add each widget to layout.
        for widget in widgets:
            layout.addWidget(widget)
        layout.addStretch()

        # Set layout
        self.setLayout(layout)

        # # Add screen 1 button
        # screen_one = QPushButton('First')
        # screen_one.setFont(sys_font)
        # screen_one.setFlat(True)
        # screen_one.setStyleSheet(
        #     'QPushButton::hover{'
        #     'background-color : blue;'
        #     'border           : none}')
        # screen_one.pressed.connect(lambda x=0: self.show.emit(x))

        # # Add screen 2 button
        # screen_two = QPushButton('Second')
        # screen_two.setFont(sys_font)
        # screen_two.setFlat(True)
        # screen_two.setStyleSheet(
        #     'QPushButton::hover{'
        #     'background-color : blue;'
        #     'border           : none}')
        # screen_two.pressed.connect(lambda x=1: self.show.emit(x))
