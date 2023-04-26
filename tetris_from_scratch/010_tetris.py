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
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget


class Tetris(QMainWindow):
    msg2Statusbar = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusbar = self.statusBar()
        self.msg2Statusbar[str].connect(self.statusbar.showMessage)
        self.msg2Statusbar.emit("ready")
        self.resize(180, 380)
        self.center()
        self.setWindowTitle('Tetris')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def main():
    app = QApplication(sys.argv)
    ex = Tetris()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
