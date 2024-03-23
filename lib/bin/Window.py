from PyQt6.QtCore import QSize, QUrl, Qt, QStandardPaths
from PyQt6.QtGui import QPixmap, QImage, QPalette, QMovie, QAction
from PyQt6.QtMultimedia import QMediaPlayer, QAudio, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QDockWidget, QStackedWidget, QScrollArea,
                             QVBoxLayout, QHBoxLayout, QGridLayout,
                             QFileDialog,
                             QToolBar, QMenu,
                             QButtonGroup,
                             QComboBox, QCheckBox, QPushButton, QLabel, QSlider, 
                             QStyle)

from pathlib import Path
from win32com.client import Dispatch, gencache

from collections import deque
from pathlib import Path
import re
import sys

from GetProperties import GetProperties
from TagPicker import TagPicker
from Viewers import Viewers

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.buildElements()

    def buildElements(self):
        Viewer = QDockWidget("Left")
        new_viewer = Viewers()
        new_viewer.callLoad()
        Viewer.setWidget(new_viewer)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, Viewer)

        Properties_Display = QDockWidget("Bottom")
        # Properties_Display.setMaximumHeight(20)
        # properties = QScrollArea()
        # properties.setWidgetResizable(True)
        # Properties_Display.setWidget(properties)     
        container = QWidget()
        container.setMinimumSize(200,200)
        Properties_Display.setWidget(container)
        # properties.setWidget(container)
        container_layout = QVBoxLayout(container)
        


        if new_viewer.CurrentFile:
            for i,j in new_viewer.CurrentFileProps.items():
                if j:
                    label = QLabel(f'{i}: {j}')
                    label.setWordWrap(True)
                    container_layout.addWidget(label)
            if new_viewer.CurrentFileProps['Search Keywords']:
                tags = new_viewer.CurrentFileProps['Search Keywords']
                tags = tags.split('; ')
            else:
                tags = []
            self.tagslabel = QLabel(str(tags))
            container_layout.addWidget(self.tagslabel)
            
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, Properties_Display)

        Tag_Section = QDockWidget("Right")
        new_tagpicker = TagPicker(tags)
        Tag_Section.setWidget(new_tagpicker)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, Tag_Section)

  #  def displayProperties(self):
        
        
if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
    

    
