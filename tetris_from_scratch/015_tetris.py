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
from PyQt5.QtGui import QPainter, QColor, QBrush


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
        self.tboard.start()
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

    BoardWidth = 10
    BoardHeight = 22

    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()

    def initBoard(self):
        pass

    def squareWidth(self):
        """returns the width of one square"""

        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self):
        """returns the height of one square"""

        return self.contentsRect().height() // Board.BoardHeight

    def start(self):
        self.msg2Statusbar.emit("Ready")

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.drawBoard(painter)
        painter.end()

    def drawBoard(self, painter):
        rect = self.contentsRect()
        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                self.drawSquare(painter,
                                rect.left() + j * self.squareWidth(),
                                boardTop + i * self.squareHeight())

    def drawSquare(self, painter, x, y):
        color = QColor(200, 0, 0)
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)


def main():
    app = QApplication(sys.argv)
    ex = Tetris()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
