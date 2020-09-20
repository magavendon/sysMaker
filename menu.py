from PySide2.QtCore import Signal
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget

from font import Font
from menubutton import Menu_Button

class Menu(QWidget):
    show = Signal(int)

    def __init__(self):
        # Parent class init
        QWidget.__init__(self)

        # Create layout
        layout = QVBoxLayout()
        layout.setMargin(0)
        layout.setSpacing(0)
        layout.addStretch()
        self.setLayout(layout)

    def add_button(self, title, screen, update_function):
        # Create the menu button.
        menu_button = Menu_Button(title, screen)
        menu_button.pressed.connect(lambda x=screen: update_function(x))

        # Add the button.
        self.layout().insertWidget(self.layout().count() - 1, menu_button)

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
