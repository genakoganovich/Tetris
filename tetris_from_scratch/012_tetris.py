#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

This example shows an icon
in the titlebar of the window.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QFrame


class Tetris(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        """initiates application UI"""

        self.tboard = Board(self)
        self.setCentralWidget(self.tboard)

        self.statusbar = self.statusBar()
        self.tboard.msg2Statusbar[str].connect(self.statusbar.showMessage)
        self.tboard.start();
        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(int((screen.width() - size.width()) / 2),
                  int((screen.height() - size.height()) / 2))


class Board(QFrame):
    msg2Statusbar = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()

    def initBoard(self):
        pass

    def start(self):
        self.msg2Statusbar.emit("Ready")


def main():
    app = QApplication(sys.argv)
    ex = Tetris()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
