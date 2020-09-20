from PySide2.QtCore import Qt
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QLineEdit
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QVBoxLayout
from PySide2.QtWidgets import QWidget

from window import Window

import system

class Star_Masses(Window):
    def __init__(self):
        # Parent class init
        Window.__init__(self, 'Star Masses')

        # Masses label
        self.masses = QLabel('A: None')
        self.masses.setFont(self.sys_font)
        self.update_masses_label()
        masses_layout = QHBoxLayout()
        masses_layout.addWidget(self.masses)
        masses_layout.addStretch()

        # Description
        description = QLabel('''A star's evolution depends very strongly on its mass and age, and somewhat less strongly on its initial composition.\nA star's mass is measured in solar masses, so that a star with mass 1.0 is exactly as massive as our own sun. Objects smaller than about 0.08 solar masses can't maintain nuclear fusion in their cores, and so can't be considered stars. Some gargantuan stars seem to have about 100 solar masses, although such "hyperstars" are extrememly rare. For every massive star that burns briefly and brightly, there are many small stars that burn dimly and hoard their nuclear fuel. The vast majority of stars, including almost every star likely to appear in a space campaign, have mass of 3.0 solar masses or less. Stars larger than about 2.0 solar masses don't appear liekly to have planets at all, so this world-design system won't examine such stars in great detail. Stars with life-bearing planets are most likely to mass between 0.6 and 1.5 solar masses.''')
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignJustify)

        # Mass selection box
        mass_selection = QGroupBox('Choose the star mass(es)')
        mass_selection.setFont(self.box_title_font)
        selection_layout = QHBoxLayout()
        selection_layout.addWidget(mass_selection)
        selection_layout.addStretch()

        # First mass selection
        first_widget    = QWidget()
        first_label     = QLabel('Star A:')
        self.first_mass = QLineEdit()
        first_set       = QPushButton('Set Mass')
        first_label.setFont(self.sys_font)
        self.first_mass.setFont(self.sys_font)
        first_set.setFont(self.sys_font)
        self.first_mass.returnPressed.connect(self.update_masses)
        first_set.pressed.connect(self.update_masses)
        first_layout = QHBoxLayout()
        first_layout.addWidget(first_label)
        first_layout.addWidget(self.first_mass)
        first_layout.addWidget(first_set)
        first_layout.addStretch()
        first_widget.setLayout(first_layout)

        # Second mass selection
        self.second_widget = QWidget()
        second_label       = QLabel('Star B:')
        self.second_mass   = QLineEdit()
        second_set         = QPushButton('Set Mass')
        second_label.setFont(self.sys_font)
        self.second_mass.setFont(self.sys_font)
        second_set.setFont(self.sys_font)
        self.second_mass.returnPressed.connect(self.update_masses)
        second_set.pressed.connect(self.update_masses)
        second_layout = QHBoxLayout()
        second_layout.addWidget(second_label)
        second_layout.addWidget(self.second_mass)
        second_layout.addWidget(second_set)
        second_layout.addStretch()
        self.second_widget.setLayout(second_layout)

        # Third mass selection
        self.third_widget = QWidget()
        third_label       = QLabel('Star C:')
        self.third_mass   = QLineEdit()
        third_set         = QPushButton('Set Mass')
        third_label.setFont(self.sys_font)
        self.third_mass.setFont(self.sys_font)
        third_set.setFont(self.sys_font)
        self.third_mass.returnPressed.connect(self.update_masses)
        third_set.pressed.connect(self.update_masses)
        third_layout = QHBoxLayout()
        third_layout.addWidget(third_label)
        third_layout.addWidget(self.third_mass)
        third_layout.addWidget(third_set)
        third_layout.addStretch()
        self.third_widget.setLayout(third_layout)

        # Set mass selection box layout
        mass_selection_layout = QVBoxLayout()
        mass_selection_layout.addWidget(first_widget)
        mass_selection_layout.addWidget(self.second_widget)
        mass_selection_layout.addWidget(self.third_widget)
        mass_selection.setLayout(mass_selection_layout)

        # Create layout
        layout = QVBoxLayout()
        layout.addLayout(masses_layout)
        layout.addWidget(description)
        layout.addSpacing(10)
        layout.addLayout(selection_layout)
        layout.addStretch()
        self.setLayout(layout)

    def update_masses(self):
        vals = []
        if system.current.num_of_stars >= 1:
            vals.append(self.first_mass.text())
        if system.current.num_of_stars >= 2:
            vals.append(self.second_mass.text())
        if system.current.num_of_stars == 3:
            vals.append(self.third_mass.text())

        for i in range(0, len(vals)):
            system.current.update_mass(i, float(vals[i]))

        self.update_info()

    def update_masses_label(self):
        if len(system.current.masses) > 0:
            update_text = ''
            for i in range(0, len(system.current.masses)):
                mass = system.current.masses[i]
                update_text += \
                    f'{chr(65 + i)}: {mass:.2f}' + \
                    f'{"   " if i < len(system.current.masses) - 1 else ""}'
            self.masses.setText(update_text)

    def update_mass_edits(self):
        # Determine which lines are visible.
        second = True if len(system.current.masses) >= 2 else False
        third  = True if len(system.current.masses) == 3 else False
        self.second_widget.setVisible(second)
        self.third_widget.setVisible(third)

        # Update the first line edit.
        self.first_mass.setText(f'{system.current.masses[0]:.2f}')

        # Update the second line edit.
        if second:
            self.second_mass.setText(f'{system.current.masses[1]:.2f}')

        # Update the third line edit.
        if third:
            self.third_mass.setText(f'{system.current.masses[2]:.2f}')

    def update_info(self):
        self.update_masses_label()
        self.update_mass_edits()
