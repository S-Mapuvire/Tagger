# figure out how to do static variable so as to put a count variable
from pathlib import Path
import os
from lib.bin.mediaItem.getProperties import getProperties

class MediaItem():

    count = 0
    
    def __init__(self, shellItemPath):
        MediaItem.count = MediaItem.count + 1
        itemfile = Path(shellItemPath)
        if not Path.exists(itemfile):
            raise ReferenceError("--file path does not exist.")
        else:
            self._name = itemfile.name
            self._itemPath = itemfile.absolute()
            self._itemProperties = getProperties(self._itemPath)
            
            self._details = {
                "name" : self._name, 
                "path": self._itemPath, 
                "properties": self._itemProperties,
                "count": MediaItem.count,
                }

    def callItem(self):
        return self._details
    
    def openInDefaultProgram(self):
        os.startfile(self._itemPath)
    
    def export(self):
        pass