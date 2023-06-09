import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget
from PyQt5.QtWidgets import QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget ()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botao')
        self.btn.setStyleSheet('font-size: 30px;')
        self.grid.addWidget(self.btn, 0,0,1,1)

        self.btn.clicked.connect(lambda: print('ola Mundo'))

        self.setCentralWidget(self.cw)

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
