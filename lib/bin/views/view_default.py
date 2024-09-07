from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QButtonGroup, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout 
from lib.bin.views.theQueue import Queue
from lib.bin.shellItem.theShellItemManager import shellItemManager
from lib.bin.mediaItem.class_mediaItem import MediaItem
import sys

class Window(QMainWindow):
    def __init__(self, managerRef, queueRef):
        super().__init__()
        self.setWindowTitle("::Tag::Aid:: - Let's fix up those tags!")
        #  let's fix up those tags!
        self._buildInterface()
        self._managerRef = managerRef
        self._queueRef = queueRef

    def customButton(self):
        return
        # button has autorepeat false, enabled false by default,
        # set styling here
        # naming is easy
        # reads from the viewer inherently
        # isadded to the button group

    def _buildInterface(self):
        self.container = QWidget(self)
        self.setCentralWidget(self.container)
        self._containerLayout = QHBoxLayout(self.container)

        self._viewerLayout = QVBoxLayout()
        self._containerLayout.addLayout(self._viewerLayout)
        self.viewer = QLabel("This is a screen")
        self._viewerLayout.addWidget(self.viewer)
        
        self._buttonContainer = QWidget()
        self._buttonContainerLayout = QGridLayout()
        self._containerLayout.addLayout(self._buttonContainerLayout)
        self._buttonContainerLayout.addWidget(self._buttonContainer)

        self.navButtons = QButtonGroup(self._buttonContainer)

        self.button1 = QPushButton("Make New Collection")
        self.button1.clicked.connect(self.MakeCollection)
        self._buttonContainerLayout.addWidget(self.button1, 0, 1)
        self.navButtons.addButton(self.button1)
        
        self.button2 = QPushButton("Add to New Collection")
        self.button2.clicked.connect(self.MakeCollectionThenAddItem)
        self.button2.setEnabled(False)
        self.button2.setAutoRepeat(False)
        self._buttonContainerLayout.addWidget(self.button2, 0, 2)
        self.navButtons.addButton(self.button2)
        
        self.button3 = QPushButton("Import to Current Collection...")
        self.button3.clicked.connect(self.ImportItemToCollection)
        self.button3.setEnabled(False)
        self._buttonContainerLayout.addWidget(self.button3, 0, 3)
        self.navButtons.addButton(self.button3)

        self.queueItem = QLabel("This is where the queue goes", self._buttonContainer)
        self._buttonContainerLayout.addWidget(self.queueItem, 0, 4)
        
        self.button4 = QPushButton("Import item(s)...")
        self.button4.clicked.connect(self.ImportItems)
        self._buttonContainerLayout.addWidget(self.button4, 1, 1)
        self.navButtons.addButton(self.button4)
        
        self.button5 = QPushButton("Import Collection(s)...")
        self.button5.clicked.connect(self.ImportCollections)
        self._buttonContainerLayout.addWidget(self.button5, 1, 2)
        self.navButtons.addButton(self.button5)
        
        self.button6 = QPushButton("Add to queue")
        self.button6.clicked.connect(self.QueueAppend)
        self.button6.setEnabled(False)
        self._buttonContainerLayout.addWidget(self.button6, 1, 3)
        self.navButtons.addButton(self.button6)
        
        self.button7 = QPushButton("Confirm edits")
        self.button7.clicked.connect(self.ConfirmEdits)
        self.button7.setEnabled(False)
        self._buttonContainerLayout.addWidget(self.button7, 2, 1)
        self.navButtons.addButton(self.button7)
        
        self.button8 = QPushButton("Delete item")
        self.button8.clicked.connect(self.DeleteItem)
        self.button8.setEnabled(False)
        self._buttonContainerLayout.addWidget(self.button8, 2, 2)
        self.navButtons.addButton(self.button8)
        
        self.button9 = QPushButton("Find item(s)...")
        self.button9.clicked.connect(self.FindItem)
        self._buttonContainerLayout.addWidget(self.button9, 2, 3)
        self.navButtons.addButton(self.button9)
        
        self.button10 = QPushButton("Rename item(s)...")
        self.button10.clicked.connect(self.RenameItem)
        self._buttonContainerLayout.addWidget(self.button10, 3, 1)
        self.navButtons.addButton(self.button10)

        
        self.button11 = QPushButton("Move item...")
        self.button11.clicked.connect(self.MoveItem)
        self.button11.setEnabled(False)
        self._buttonContainerLayout.addWidget(self.button11, 3, 2)
        self.navButtons.addButton(self.button11)
        
        self.button12 = QPushButton("Open item in default program")
        self.button12.clicked.connect(self.OpenItem)
        self.button12.setEnabled(False)
        self._buttonContainerLayout.addWidget(self.button12, 3, 3)
        self.navButtons.addButton(self.button12)

    def MakeCollection(self):
        print('Make a collection')

    def MakeCollectionThenAddItem(self):
        print('Make a collection and add this')

    def ImportItemToCollection(self):
        print('Import an item to this collection')

    def ImportItems(self):
        print('Import files')

    def ImportCollections(self):
        print('Import a collection')
    
    def QueueAppend(self):
        print('Import this item to queue')

    def ConfirmEdits (self):
        print('Confirm Edits and close item')
        
    def DeleteItem (self):
        print('Send this item to recycle bin')
        
    def FindItem (self):
        print('Look for item')
        
    def RenameItem (self):
        print('Rename item')
        
    def MoveItem (self):
        print('Move item')
        
    def OpenItem (self):
        print('Open item')

if __name__ == '__main__':
    app = QApplication([])
    manager = shellItemManager()
    queue = Queue()
    window = Window(manager, queue)
    window.show()
    sys.exit(app.exec())



