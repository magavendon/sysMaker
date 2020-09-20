from PySide2.QtCore import Signal
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget

from font import Font

class Home(QWidget):
    show = Signal(int, str)

    def __init__(self):
        # Parent class init
        QWidget.__init__(self)

        # Set title
        self.title = 'System Maker'

        # Get instance of font.
        sys_font = Font()

        # Add new system button
        new_system = QPushButton('New System')
        new_system.setFont(sys_font)
        new_system.pressed.connect(lambda x=1:
                                   self.show.emit(x, 'Number of Stars'))

        # Add load system button
        load_system = QPushButton('Load System')
        load_system.setFont(sys_font)

        # Add quit button
        quit_creator = QPushButton('Quit')
        quit_creator.setFont(sys_font)

        # Create layouts
        h_layout = QHBoxLayout()
        layout   = QVBoxLayout()

        # Add children to layouts
        layout.addStretch(4)
        layout.addWidget(new_system)
        layout.addStretch(1)
        layout.addWidget(load_system)
        layout.addStretch(1)
        layout.addWidget(quit_creator)
        layout.addStretch(4)
        h_layout.addStretch(1)
        h_layout.addLayout(layout, 2)
        h_layout.addStretch(1)

        # Set the layout
        self.setLayout(h_layout)
