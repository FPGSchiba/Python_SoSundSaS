import sys
from pathlib import Path

from PySide6.QtCore import QUrl, QCoreApplication
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineCore import QWebEnginePage
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtGui import QDesktopServices


class WebEnginePage(QWebEnginePage):
    def __init__(self, parent):
        super().__init__(parent)

    def acceptNavigationRequest(self, url: QUrl, *_):
        if url.scheme != "https":
            return True
        QDesktopServices.openUrl(url)
        return False

    def closeEvent(self, event):
        print('close')
        event.accept()

def exit_handler():
    src_dir = Path('G:\\My Drive\\Projects\\Minas Tirith\\')
    web_view.save((src_dir / "Outer-Circle-Minas.svg").__str__())
    print('close')


if __name__ == '__main__':
    src_dir = Path('G:\\My Drive\\Projects\\Minas Tirith\\')
    QCoreApplication.setOrganizationName("QtProject")
    app = QApplication(sys.argv)
    app.aboutToQuit.connect(exit_handler)
    view = QWebEngineView()
    web_view = WebEnginePage(view)

    view.setPage(web_view)
    profile = view.page().profile()

    view.resize(1280, 1280)
    view.show()
    view.setUrl(QUrl.fromLocalFile(src_dir / "Outer-Circle-Minas.svg"))

    sys.exit(app.exec())
