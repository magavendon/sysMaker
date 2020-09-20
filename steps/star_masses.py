from PySide2.QtCore import Qt
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
        self.update_masses()
        masses_layout = QHBoxLayout()
        masses_layout.addWidget(self.masses)
        masses_layout.addStretch()

        # Description
        description = QLabel('''A star's evolution depends very strongly on its mass and age, and somewhat less strongly on its initial composition.\nA star's mass is measured in solar masses, so that a star with mass 1.0 is exactly as massive as our own sun. Objects smaller than about 0.08 solar masses can't maintain nuclear fusion in their cores, and so can't be considered stars. Some gargantuan stars seem to have about 100 solar masses, although such "hyperstars" are extrememly rare. For every massive star that burns briefly and brightly, there are many small stars that burn dimly and hoard their nuclear fuel. The vast majority of stars, including almost every star likely to appear in a space campaign, have mass of 3.0 solar masses or less. Stars larger than about 2.0 solar masses don't appear liekly to have planets at all, so this world-design system won't examine such stars in great detail. Stars with life-bearing planets are most likely to mass between 0.6 and 1.5 solar masses.''')
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignJustify)

        # Create layout
        layout = QVBoxLayout()
        layout.addLayout(masses_layout)
        layout.addWidget(description)
        layout.addStretch()
        self.setLayout(layout)

    def update_masses(self):
        if len(system.current.masses) > 0:
            update_text = ''
            for i in range(0, len(system.current.masses)):
                mass = system.current.masses[i]
                update_text += \
                    f'{chr(65 + i)}: {mass:.2f}' + \
                    f'{"   " if i < len(system.current.masses) - 1 else ""}'
            self.masses.setText(update_text)

    def update_info(self):
        self.update_masses()
