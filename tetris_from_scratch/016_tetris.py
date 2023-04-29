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
from PyQt5.QtGui import QPainter, QColor, QPen


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
    Speed = 300
    Column_Count = 0
    Line_Count = 0

    def __init__(self, parent):
        super().__init__(parent)

        self.initBoard()

    def initBoard(self):
        self.timer = QBasicTimer()
        self.numLinesRemoved = 0

    def squareWidth(self):
        """returns the width of one square"""

        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self):
        """returns the height of one square"""

        return self.contentsRect().height() // Board.BoardHeight

    def start(self):
        self.msg2Statusbar.emit(str(self.numLinesRemoved))
        self.timer.start(Board.Speed, self)

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)
        self.drawGrid(painter)
        self.drawBoard(painter)
        self.drawMove(painter)
        painter.end()

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.msg2Statusbar.emit(str(Board.Line_Count))
            self.update()
        else:
            super(Board, self).timerEvent(event)

    def drawBoard(self, painter):
        rect = self.contentsRect()
        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        for i in range(Board.BoardHeight):
            for j in range(Board.BoardWidth):
                self.drawSquare(painter,
                                rect.left() + j * self.squareWidth(),
                                boardTop + i * self.squareHeight(),
                                QColor(255, 255, 0))

    def drawSquare(self, painter, x, y, color):
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

    def drawMove(self, painter):
        rect = self.contentsRect()
        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()
        self.drawSquare(painter,
                        rect.left() + (Board.Column_Count % Board.BoardWidth) * self.squareWidth(),
                        boardTop + (Board.Line_Count % Board.BoardHeight) * self.squareHeight(),
                        QColor(200, 0, 0))
        Board.Line_Count = Board.Line_Count + 1
        Board.Column_Count = Board.Line_Count // Board.BoardHeight

    def drawGrid(self, painter):
        pen = QPen(Qt.black, 1, Qt.SolidLine)
        rect = self.contentsRect()
        boardTop = rect.bottom() - Board.BoardHeight * self.squareHeight()

        painter.setPen(pen)
        for i in range(Board.BoardHeight):
            painter.drawLine(rect.left(),
                             boardTop + i * self.squareHeight(),
                             rect.left() + rect.width(),
                             boardTop + i * self.squareHeight())

        for j in range(Board.BoardWidth):
            painter.drawLine(rect.left() + j * self.squareWidth(),
                             boardTop,
                             rect.left() + j * self.squareWidth(),
                             rect.bottom())
def main():
    app = QApplication(sys.argv)
    ex = Tetris()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
