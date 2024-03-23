## make an image resize function
## seperate three into different files
##add a custom scroll bar - vert and hori - and a function to allow the mouse to drag across the image
## when a 'playlist' is loaded, turn load into append
## make it so last location becomes default
## find out how to resize image and implement zoom in in viewer
## add position slider, one button that switches betwen play and pause, looping setting, 
##  implement volume, visualiser for audio w/out video to player
## implement 'playlist'/filestack system
## implement animated image viewer
## figure how to qthreads
## read up on QMediaPlayer

import sys
from pathlib import Path

#from GetProperties import GetProperties
#from LoadFiles import main

from PyQt6.QtCore import QSize, QUrl, Qt, QStandardPaths
from PyQt6.QtGui import QPixmap, QImage, QPalette, QMovie, QAction
from PyQt6.QtMultimedia import QMediaPlayer, QAudio, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QMenu, QSlider, QPushButton,
                             QGridLayout, QMainWindow, QScrollArea, QFileDialog, QDockWidget, QStyle, QToolBar)
from GetProperties import GetProperties

class Viewers(QMainWindow):
    def __init__(self):
        ## Setup
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setStyleSheet("* {border: 1px solid red}")
        
        ## Globals
        self.Files = None
        self.CurrentFile = None
        self._FileTypes = {"Images": [".png", ".jpeg", ".jpg"], "Videos": [".mp4", ".wmv", ".mov", ".mkv", ".avi"], "Audio":[".mp3", ".m4a"]}
        self.Fileloader = QFileDialog()
        
        ## UI Setup

        ## Create the main menu
        menu = self.menuBar()
        fileMenu = QMenu("&File", self)
        menu.addMenu(fileMenu)
        
        ## using standard icons
        ## get standard icon flag
        pixmapi = QStyle.StandardPixmap.SP_DirOpenIcon
        ## then grab the respective icon
        icon = self.style().standardIcon(pixmapi)
        ## get open icon

        ## Create 'load' for file menu
        load_action = QAction(icon, "&Load...", self, shortcut="Ctrl+O", triggered=self._loadFile)
        
        fileMenu.addAction(load_action) ##loadOption = fileMenu.addAction("&Load...")

        fileMenu.addSeparator()

        ## get close icon
        pixmapi = QStyle.StandardPixmap.SP_TitleBarCloseButton
        icon = self.style().standardIcon(pixmapi)

        ## Create 'exit' for file menu
        close_action = QAction(icon, "&Exit", self, shortcut="Ctrl+Q", triggered=self.close)
        fileMenu.addAction(close_action) ## alternative way, without icon = exitOption = fileMenu.addAction("&Exit")
        
        self._buildImageViewer()
        self._buildVideoPlayer()

    ## Build the image viewer pop-up window and hide it
    def _buildImageViewer(self):
        self.ImageViewerDock = QDockWidget("Image Viewer", self)
        self.ImageViewerDock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)

        self.ImageControls = QToolBar()
        
        self.zoomIn = QPushButton(" + ")
        self.zoomIn.setStyleSheet("font-size: 30px;")
        self.zoomIn.clicked.connect(self.expandImage)
        self.ImageControls.addWidget(self.zoomIn)
        
        self.zoomOut = QPushButton(" - ")
        self.zoomOut.setStyleSheet("font-size: 30px;")
        self.zoomOut.clicked.connect(self.shrinkImage)
        self.ImageControls.addWidget(self.zoomOut)

        self.addToolBar(self.ImageControls)

        self.imageLabel = QLabel(self)
        self.imageLabel.setScaledContents(True)

        self.ImageViewer = QScrollArea(self.ImageViewerDock)
        self.ImageViewer.setWidget(self.imageLabel)
        
        self.ImageViewerDock.setWidget(self.ImageViewer)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.ImageViewerDock)

        self._toggleImageViewer(self.ImageViewerDock.isHidden() ^ 1)

    ##put if/else to prevent excessive zooming
    def expandImage(self):
        self.imgwidth = int(self.imgwidth / self.imageRatio)
        self.imgheight = int(self.imgheight / self.imageRatio)

        self.imageLabel.setFixedSize(self.imgwidth, self.imgheight)
        print(self.imgwidth, self.imgheight, self.imageRatio)

    def shrinkImage(self):
        self.imgwidth = int(self.imgwidth * self.imageRatio)
        self.imgheight = int(self.imgheight * self.imageRatio)

        self.imageLabel.setFixedSize(self.imgwidth, self.imgheight)
        print(self.imgwidth, self.imgheight, self.imageRatio)

########################################################################            
        
    ## Build the video player pop-up window and hide it
    def _buildVideoPlayer(self):

        self.VideoPlayerDock = QDockWidget("🖤 Player 🖤", self)
        self.VideoPlayerDock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)

        ## Create the main toolbar
        self.VideoControls = QToolBar()
        self.addToolBar(self.VideoControls)

        ## Create main player
        self.VideoPlayer = QMediaPlayer()
        self._VideoWidget = QVideoWidget()
        self._AudioOutput = QAudioOutput()
        self.VideoPlayer.setVideoOutput(self._VideoWidget)
        self.VideoPlayer.setAudioOutput(self._AudioOutput)
        
        ## Build the video control bar

        ## Slider

        self._volume_slider = QSlider()
        self._volume_slider.setOrientation(Qt.Orientation.Horizontal)
        self._volume_slider.setMinimum(0)
        self._volume_slider.setMaximum(100)
        self._volume_slider.setFixedWidth(100)

        self._volume_slider.setValue(int(self._AudioOutput.volume()))

        linearVolume = QAudio.convertVolume(self._AudioOutput.volume()/100.0,
                                           QAudio.VolumeScale.LogarithmicVolumeScale,
                                           QAudio.VolumeScale.LinearVolumeScale)
        #self._volume_slider.valueChanged.connect(self._AudioOutput.setVolume(int(linearVolume * 100)))

        self._volume_slider.setTickInterval(10)
        self._volume_slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self._volume_slider.setToolTip("Volume")

        self.VideoControls.addWidget(self._volume_slider)

        ## play button
        pixmapi = QStyle.StandardPixmap.SP_MediaPlay
        icon = self.style().standardIcon(pixmapi)

        self._play_action = self.VideoControls.addAction(icon, "Play")
        self._play_action.triggered.connect(self.VideoPlayer.play)
        
        ## pause button
        pixmapi = QStyle.StandardPixmap.SP_MediaPause
        icon = self.style().standardIcon(pixmapi)

        self._pause_action = self.VideoControls.addAction(icon, "Pause")
        self._pause_action.triggered.connect(self.VideoPlayer.pause)
        
        ## stop button
        pixmapi = QStyle.StandardPixmap.SP_MediaStop
        icon = self.style().standardIcon(pixmapi)

        self._stop_action = self.VideoControls.addAction(icon, "Stop")
        self._stop_action.triggered.connect(self._ensure_stopped)

        self.VideoPlayerDock.setWidget(self._VideoWidget)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.VideoPlayerDock)

        self._toggleVideoPlayer(self.VideoPlayerDock.isHidden() ^ 1)
        
    def _buildGIFViewer(self, gif):
        ##        self.videoLabel = QLabel()
##        layout.addWidget(self.videoLabel)
##        dummy_movie = QMovie(r'C:\Users\Aqua\Mega\Code\Tagging Program\=Tests\video.mp4')
##        label.setMovie(dummy_movie)
##
##        if(movie.isValid()):
##            movie.start()

##        self.VideoPlayerView = QScrollArea(self)
##        self.VideoPlayerView.setWidget(self.videoLabel)
        #layout.addWidget(scrollArea)
        return
    
    ## Unhide the image viewer using XOR operations
    ## XOR = uneven inputs is TRUE,
    ## XOR allows for flipping the switch as 0 1 = 1 (where the 0 is the input and 1 is the constant) and 1 1 = 0
    
    def _toggleImageViewer(self, value):
        self.ImageViewerDock.setHidden(value)
        self.ImageControls.setHidden(value)
        
    ## Unhide the video player
    def _toggleVideoPlayer(self, value):
        self.VideoPlayerDock.setHidden(value)
        self.VideoControls.setHidden(value)

    ## Grab the desired file
    ## and check that it is of proper type (sentinel loop)
    def _loadFile(self):
        self.Files, delete = self.Fileloader.getOpenFileNames(self, "Open image, video or audio file", "D:\=Phone\--")
        if self.Files:
            self.CurrentFile = self.Files.pop(0)
            self._selector(self.CurrentFile)
            filepath = Path(self.CurrentFile)
            parent = filepath.parent
            self.CurrentFileProps = GetProperties(Path(self.CurrentFile), Path(parent))
            
    def _selector(self, file):
        Extension = Path(file).suffix

        if Extension in self._FileTypes["Images"]:
            self._displayImageViewer(file)
        elif Extension in self._FileTypes["Videos"]:
            self._displayVideoPlayer(file)
        elif Extension in self._FileTypes["Audio"]:
            self._displayVideoPlayer(file)
        elif Extension == ".gif":
            return #call a different func that uses an animated label
        else:
            print("Unsupported Format")

   ## Use the image viewer
    def _displayImageViewer(self, img):
        if img:
            image = QPixmap(img)
            self.imgwidth = image.width()
            self.imgheight = image.height()
            
            if image.width() > 480:
                self.imgwidth = image.width()//10
            if image.height() > 960:
                self.imgheight = image.height()//10

            self.imageRatio = self.imgwidth/self.imgheight

            self.ImageViewer.setMinimumWidth(self.imgwidth)
            self.ImageViewer.setMinimumHeight(self.imgheight)

            self.imageLabel.setPixmap(image)
            self.imageLabel.setFixedSize(self.imgwidth, self.imgheight)
            
        if self.ImageViewerDock.isHidden():
            self._toggleImageViewer(self.ImageViewerDock.isHidden() ^ 1)

    ## Use the video player
    def _displayVideoPlayer(self, vid):
        if vid:
            self.VideoPlayer.setSource(QUrl.fromLocalFile(vid))
        if self.VideoPlayerDock.isHidden():
            self._toggleVideoPlayer(self.VideoPlayerDock.isHidden() ^ 1)
        self._VideoWidget.show()
        self.VideoPlayer.play()

    def closeEvent(self, event):
        self._ensure_stopped()
        event.accept()

    def _ensure_stopped(self):
        if self.VideoPlayer.playbackState() != QMediaPlayer.PlaybackState.StoppedState:
            self.VideoPlayer.stop()

    def callLoad(self):
        self._loadFile()

def main():
    app = QApplication([])
    viewer_picker = Viewers()
    viewer_picker.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
