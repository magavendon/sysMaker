from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QVBoxLayout

from window import Window

import system

class Star_Masses(Window):
    def __init__(self):
        # Parent class init
        Window.__init__(self, 'Star Masses')

        # Masses label
        self.masses = QLabel('A: None')
        self.masses.setFont(self.sys_font)
        masses_layout = QHBoxLayout()
        masses_layout.addWidget(self.masses)
        masses_layout.addStretch()

        # Create layout
        layout = QVBoxLayout()
        layout.addLayout(masses_layout)
        layout.addStretch()
        self.setLayout(layout)
