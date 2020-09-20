from PySide2.QtGui import QFont

class Font(QFont):
    def __init__(self, family = 'Astron', size = 20):
        # Parent class init
        QFont.__init__(self, family, size)
