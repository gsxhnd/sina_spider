import sys
from PyQt5.QtWidgets import QApplication
import PyQt5.uic

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mWindow = PyQt5.uic.loadUi('./UI/testUI.ui')
    mWindow.show()
    sys.exit(app.exec())
