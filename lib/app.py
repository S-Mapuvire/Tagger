import sys

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from pathlib import Path

from bin.tag_editor.tags import Tag_Window

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tagging Program')
        
        self.stylesheet = r'C:\Users\Aqua\Mega\Code\Tagging Program\lib\assets\style.css'
        self.categories = r'C:\Users\Aqua\Mega\Code\Tagging Program\lib\assets\tag categories'

        self.container = QWidget()
        self.setCentralWidget(self.container)
        self.container_layout = QHBoxLayout(self.container)
        
        self._makeTabs()
        #self._createViewer()
        self._createMenu()
        self._createToolBar()
        self._createStatusBar()

    def _makeTabs(self):
        directory_object = Path(self.categories)
        self.Tags_Section = QTabWidget()
        self.container_layout.addWidget(self.Tags_Section)
        self.page_array = []

        for file in directory_object.iterdir():
            page = Tag_Window(file, self.stylesheet)
            page_name = file.stem
            page_container = QWidget()
            self.Tags_Section.addTab(page, page_name)
            self.page_array.append(page)

    def getTags(self):
        for i in self.page_array:
            if (i.get_tags()):
                print(i.get_tags())

   # def _createViewer(self):
                

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)
    
    def _createToolBar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        tools.addAction("Save", self.getTags)
        self.addToolBar(tools)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("Status Bar")
        self.setStatusBar(status)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
