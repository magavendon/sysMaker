from PySide2.QtWidgets import QFrame
from PySide2.QtWidgets import QGridLayout
from PySide2.QtWidgets import QStackedWidget
from PySide2.QtWidgets import QWidget

from home import Home
from info import InfoPanel
from menu import Menu

from steps.num_stars import Num_Stars

class MainWindow(QWidget):
  def __init__(self):
    # Parent class init
    QWidget.__init__(self)

    # Set default size
    self.resize(800, 600)

    # Add separator line
    h_sep = QFrame()
    h_sep.setFrameStyle(QFrame.HLine)

    # Add main viewer (stacked widget)
    self.view = QStackedWidget()

    # Add menu
    self.menu = Menu()

    # Add info view
    self.info = InfoPanel()
    self.info.toggle_menu.connect(lambda: self.menu.setVisible(not self.menu.isVisible()))

    # Populate main viewer.
    # These lines must be after adding info view, so the title can be updated.
    self.add_screen(Home())
    self.add_screen(Num_Stars())

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
    def update_screen(ndx, title):
      self.view.setCurrentIndex(ndx)
      self.info.title.setText(title)

    # Setup screen connection.
    new_screen.show.connect(update_screen)

    # Add screen instances.
    self.view.addWidget(new_screen)

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
