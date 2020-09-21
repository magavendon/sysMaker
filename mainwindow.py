from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QScrollArea
from PySide2.QtWidgets import QStackedWidget
from PySide2.QtWidgets import QWidget

from home import Home
from info import InfoPanel
from menu import Menu

from steps.num_stars   import Num_Stars
from steps.star_masses import Star_Masses

class MainWindow(QWidget):
  def __init__(self):
    # Parent class init
    QWidget.__init__(self)

    # Set default size
    self.resize(800, 800)

    # Add separator line
    h_sep = QFrame()
    h_sep.setFrameStyle(QFrame.HLine)

    # Add main viewer (stacked widget)
    self.view = QStackedWidget()

    # Add menu
    self.menu = Menu()
    self.menu.setVisible(False)

    # Add info view
    self.info = InfoPanel()
    self.info.toggle_menu.connect(lambda: self.menu.setVisible(not self.menu.isVisible()))

    # Populate main viewer.
    # These lines must be after adding info view, so the title can be updated.
    self.add_screen(Home())
    self.add_screen(Num_Stars())
    self.add_screen(Star_Masses())

    # Add separator line
    v_sep = QFrame()
    v_sep.setFrameStyle(QFrame.VLine)

    # Create the layout
    layout = QGridLayout()
    layout.setMargin(0)
    layout.setSpacing(0)

    # Add children to layout
    layout.addWidget(self.info, 0, 0, 1, 3)
    layout.addWidget(h_sep, 1, 0, 1, 3)
    layout.addWidget(self.menu, 2, 0)
    layout.setColumnStretch(0, 0)
    layout.addWidget(v_sep, 2, 1)
    layout.setColumnStretch(1, 0)
    layout.addWidget(self.view, 2, 2)
    layout.setColumnStretch(2, 1)

    # Set the layout
    self.setLayout(layout)

  def add_screen(self, new_screen):
    def update_screen(ndx):
      self.view.setCurrentIndex(ndx)
      self.info.title.setText(self.view.currentWidget().widget().title)
      self.view.currentWidget().widget().update_info()
      self.menu.setVisible(False)

    # Setup screen connection.
    new_screen.show.connect(update_screen)

    # Place screen in a scroll area.
    scroll_area = QScrollArea()
    scroll_area.setWidget(new_screen)

    # Add screen instances.
    self.view.addWidget(scroll_area)

    # Add the screen to the menu.
    self.menu.add_button(new_screen.title, self.view.count() - 1, update_screen)

  def mousePressEvent(self, e):
    # Get menu dimensions
    left   = self.menu.geometry().x()
    right  = self.menu.geometry().width() - left
    top    = self.menu.geometry().y()
    bottom = self.menu.geometry().height() - top

    # Get click location
    x = e.pos().x()
    y = e.pos().y()

    # If click is outside the menu, hide it
    if not (left < x < right and top < y < bottom):
      self.menu.hide()
