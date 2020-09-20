from PySide2.QtCore import Qt
from PySide2.QtCore import Signal
from PySide2.QtWidgets import QCheckBox
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QGroupBox
from PySide2.QtWidgets import QHBoxLayout
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QPushButton
from PySide2.QtWidgets import QRadioButton
from PySide2.QtWidgets import QVBoxLayout

from die_roller import dice
from window import Window
import system

class Num_Stars(Window):
    def __init__(self):
        # Parent class init
        Window.__init__(self, 'Number of Stars')

        # Stars label
        self.stars_label = QLabel('Stars: None')
        self.stars_label.setFont(self.sys_font)
        label_layout = QHBoxLayout()
        label_layout.addWidget(self.stars_label)
        label_layout.addStretch()

        # Update stars label
        if system.current.num_of_stars != 0:
            self.stars_label.setText(f'Stars: {system.current.num_of_stars}')

        # Description
        description = QLabel('''Many stars travel in pairs or larger groups, bound together gravitationally so that each orbits the center of mass of the entire system. In such star systems, the component stars are named using letters of the alphabet, with the most massive tagged A, the next most massive B, and so on. The A-component is also called the primary star of the system, and the other components are companions.\nAbout half of all star systems are composed of single stars, with most of the rest being binary pairs. Trinary (three-star) systems are uncommon but possible. Multiple star systems with more than three members are fairly rare, and shouldn't be placed at random.''')
        description.setWordWrap(True)
        description.setAlignment(Qt.AlignJustify)

        # Star selection box
        star_selection = QGroupBox('Select number of stars')
        star_selection.setFont(self.box_title_font)
        selection_layout = QHBoxLayout()
        selection_layout.addWidget(star_selection)
        selection_layout.addStretch()

        # Star selections
        one_star    = QRadioButton('1 Star'  , star_selection)
        two_stars   = QRadioButton('2 Stars' , star_selection)
        three_stars = QRadioButton('3 Stars' , star_selection)
        one_star.setFont(self.sys_font)
        two_stars.setFont(self.sys_font)
        three_stars.setFont(self.sys_font)
        one_star.pressed.connect(lambda x=1: self.update_stars(x))
        two_stars.pressed.connect(lambda x=2: self.update_stars(x))
        three_stars.pressed.connect(lambda x=3: self.update_stars(x))

        # Set star selection box layout
        star_selection_layout = QHBoxLayout()
        star_selection_layout.addWidget(one_star)
        star_selection_layout.addWidget(two_stars)
        star_selection_layout.addWidget(three_stars)
        star_selection_layout.addStretch()
        star_selection.setLayout(star_selection_layout)

        # Randomization box
        randomization = QGroupBox('Randomization')
        randomization.setFont(self.box_title_font)
        randomization_layout = QHBoxLayout()
        randomization_layout.addWidget(randomization)
        randomization_layout.addStretch()

        # Open cluster checkbox
        self.open_cluster = QCheckBox('Open Cluster')
        self.open_cluster.setFont(self.sys_font)
        self.open_cluster.stateChanged.connect(self.update_probability_table)

        # Open cluster modifier
        open_cluster_modifier = QLabel('(+3 to dice roll)')
        open_cluster_modifier.setAlignment(Qt.AlignBottom)

        # Open cluster checkbox layout
        open_cluster_checkbox_layout = QHBoxLayout()
        open_cluster_checkbox_layout.addWidget(self.open_cluster)
        open_cluster_checkbox_layout.addWidget(open_cluster_modifier)
        open_cluster_checkbox_layout.addStretch()

        # Open cluster explanation
        open_cluster_explanation = QLabel('''Open clusters are very common star groups, smaller than globular clusters and located solely in the galactic disk. An open cluster is usually two to 15 parsecs in diameter, and can contain up to several thousand stars. These stars all formed together and have since moved through the galaxy as one, mutually bound by gravity. Open clusters can be any age, although very old ones are quite rare. Most are less than 200 million years old, and almost none are older than two billion years. Stars in an open cluster may have planets, if they are old enough and have managed to avoid close encounters with other cluster members. There are several open clusters in Earth's galactic neighborhood, most notably the Ursa Major Moving Cluster (centered about 23 parsecs away) and the Hyades (centered about 45 parsecs away).''')
        open_cluster_explanation.setWordWrap(True)
        open_cluster_explanation.setAlignment(Qt.AlignJustify)

        # Probability table
        one_star        = QLabel('1')
        two_stars       = QLabel('2')
        three_stars     = QLabel('3')
        self.prob_1     = QLabel('50%')
        self.prob_2     = QLabel('45%')
        self.prob_3     = QLabel('5%')
        one_star.setAlignment(Qt.AlignCenter)
        two_stars.setAlignment(Qt.AlignCenter)
        three_stars.setAlignment(Qt.AlignCenter)
        self.prob_1.setAlignment(Qt.AlignCenter)
        self.prob_2.setAlignment(Qt.AlignCenter)
        self.prob_3.setAlignment(Qt.AlignCenter)

        # Probability table layout
        probability_layout = QVBoxLayout()
        probability_table_layout = QGridLayout()
        probability_table_layout.addWidget(QLabel('Roll (3d)')   , 0, 0)
        probability_table_layout.addWidget(QLabel('Stars')       , 0, 1)
        probability_table_layout.addWidget(QLabel('Probability') , 0, 2)
        probability_table_layout.addWidget(QLabel('3-10')        , 1, 0)
        probability_table_layout.addWidget(one_star              , 1, 1)
        probability_table_layout.addWidget(self.prob_1           , 1, 2)
        probability_table_layout.addWidget(QLabel('11-15')       , 2, 0)
        probability_table_layout.addWidget(two_stars             , 2, 1)
        probability_table_layout.addWidget(self.prob_2           , 2, 2)
        probability_table_layout.addWidget(QLabel('16-21')       , 3, 0)
        probability_table_layout.addWidget(three_stars           , 3, 1)
        probability_table_layout.addWidget(self.prob_3           , 3, 2)
        probability_layout.addLayout(probability_table_layout)
        probability_layout.addStretch()

        # Randomize button
        randomize = QPushButton('Randomize')
        randomize.setFont(self.sys_font)
        randomize.pressed.connect(self.randomize_stars)

        # Randomize layout
        randomize_layout = QHBoxLayout()
        randomize_layout.addWidget(randomize)
        randomize_layout.addStretch()

        # Set randomization box layout
        randomization_box_layout = QGridLayout()
        randomization_box_layout.addLayout(open_cluster_checkbox_layout, 0, 0)
        randomization_box_layout.addWidget(open_cluster_explanation, 1, 0)
        randomization_box_layout.addLayout(probability_layout, 0, 1, 2, 1)
        randomization_box_layout.addLayout(randomize_layout, 2, 0, 1, 2)
        randomization.setLayout(randomization_box_layout)

        # Create the layout
        layout = QVBoxLayout()

        # Add children to layout
        layout.addLayout(label_layout)
        layout.addWidget(description)
        layout.addSpacing(10)
        layout.addLayout(selection_layout)
        layout.addSpacing(10)
        layout.addLayout(randomization_layout)
        layout.addStretch()

        # Set the layout
        self.setLayout(layout)

    def update_stars(self, stars):
        system.current.num_of_stars = stars
        self.stars_label.setText(f'Stars: {stars}')

    def update_probability_table(self, check):
        self.prob_1.setText(f'{"16" if check else "50"}%')
        self.prob_2.setText(f'{"58" if check else "45"}%')
        self.prob_3.setText(f'{"26" if check else "5"}%')

    def randomize_stars(self):
        # Get the roll.
        roll = dice.roll('3d6')

        # If open cluster is selected, add to the roll.
        roll += 3 if self.open_cluster.isChecked() else 0

        # Check the table.
        if 3 <= roll <= 10:
            self.update_stars(1)
        elif 11 <= roll <= 15:
            self.update_stars(2)
        else:
            self.update_stars(3)
