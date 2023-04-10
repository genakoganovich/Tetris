#!/usr/bin/python

"""
ZetCode PyQt5 tutorial

This example shows an icon
in the titlebar of the window.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class Tetris(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
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
