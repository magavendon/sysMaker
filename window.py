from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget

from font import Font

class Window(QWidget):
    show = Signal(int)

    def __init__(self, title):
        # Parent class init
        QWidget.__init__(self)

        # Set title
        self.title = title

        # Set fonts
        self.sys_font = Font()
        self.box_title_font = Font()
        self.box_title_font.setPointSize(14)

    def update_info(self):
        pass
