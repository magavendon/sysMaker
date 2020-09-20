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

        # Update masses label
        if len(system.current.masses) > 0:
            update_text = ''
            for i in range(0, len(system.current.masses)):
                mass = system.current.masses[i]
                update_text += \
                    f'{chr(65 + i)}: {mass:.2f}' + \
                    f'{"   " if i < len(system.current.masses) - 1 else ""}'
            self.masses.setText(update_text)

        # Create layout
        layout = QVBoxLayout()
        layout.addLayout(masses_layout)
        layout.addStretch()
        self.setLayout(layout)
