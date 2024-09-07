# get image file to test on... 
# turn into deque?
# Create, Query, Append, Pop, Clear

from PyQt6.QtWidgets import QApplication
from lib.bin.shellItem.theShellItemManager import shellItemManager
from lib.bin.mediaItem.class_mediaItem import MediaItem
from pathlib import Path

class Queue():
    
    def __init__(self):
        self._queueItems = []
    
    def addItem(self, managerRef: shellItemManager, position: int = 0):
        """
        Takes in a ref to a shell manager and an optional positional index
        """
        file_list = managerRef.importShellItem(0)
        for file in file_list:
            media_item = MediaItem(Path(file))
            self._queueItems.append(media_item.callItem())
    
    def removeItem(self, *, item: MediaItem = None, index: int = None):
        if type(item) == MediaItem:
            # find item
            # print(f"Removed {self._queueItems[index]}")
            print("Work in progress")
            pass
        elif type(index) == int:
            print(f"Removed {self._queueItems[index]}")
            self._queueItems.pop(self._queueItems[index])
        else:
            raise TypeError("Neither argument is of correct type.") 

    def clearAll(self):
        self._queueItems.clear()
    
    def getQueueItem(self, *, item: MediaItem  = None, index: int = None):
        # either get by index or file
        if type(item) == MediaItem:
            # find item
            # print(f"Removed {self._queueItems[index]}")
            print("Work in progress")
            pass
        elif type(index) == int:
            media_item = self._queueItems[index]
            return media_item
        else:
            raise TypeError("Neither argument is of correct type.")
    
    def getFirstItem(self):
        if self._queueItems:
            return self._queueItems[0]
        else:
            raise IndexError("Cannot get from an empty queue")

    def getLastItem(self):
        if self._queueItems:
            return self._queueItems[-1]
        else:
            raise IndexError("Cannot get from an empty queue")
    
    def getQueueDetails(self):
        if self._queueItems:
            length = len(self._queueItems)
            items = []
            for item in self._queueItems:
                items.append(item['name'])
            return {"length": length, "items": items}
        else:
            return "Queue is empty"
    
    def pushToCollection(self):
        # check whether current or existing or new collection
        print("Work in progress")