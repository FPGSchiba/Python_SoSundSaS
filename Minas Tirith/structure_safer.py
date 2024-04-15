import chess
import chess.svg

from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWebEngine import QWebEngineView


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.svg_location = 'G:\\My Drive\\Projects\\Minas Tirith\\Outer-Circle-Minas.svg'

        self.setGeometry(100, 100, 1100, 1100)

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 1080, 1080)

        self.webview = QGraphicsWebView()
        self.webview.resize(SVGwidth, SVGheight)
        self.webview.load(QtCore.QUrl('C:\someTest.svg'))
        self.webview.setFlags(QtGui.QGraphicsItem.ItemClipsToShape)
        self.webview.setCacheMode(QtGui.QGraphicsItem.NoCache)
        self.webview.setZValue(0)

        self.chessboard = chess.Board()
        with open(self.svg_location, 'rb+') as file:
            self.widgetSvg.load(file.read())


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
