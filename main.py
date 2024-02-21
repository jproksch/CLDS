import sys

from PyQt6.QtWidgets import QApplication

from MVC.Controller import Controller
from MVC.Model import Model
from MVC.View import View

if __name__ == '__main__':
    app = QApplication(sys.argv)
    model = Model()
    view = View()
    controller = Controller(model, view)
    view.show()
    sys.exit(app.exec())
