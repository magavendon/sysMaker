from PySide2.QtWidgets import QPushButton

from font import Font

class Menu_Button(QPushButton):
    def __init__(self, text, screen):
        # Parent class init
        QPushButton.__init__(self, text)

        # Set custom font
        sys_font = Font()
        sys_font.setPointSize(14)
        self.setFont(sys_font)

        # Add customization
        self.setFlat(True)
        self.setStyleSheet(
            'QPushButton::hover{'
            'background-color : blue;'
            'border           : none}')

        # Add assigned screen
        self.assigned_screen = screen
