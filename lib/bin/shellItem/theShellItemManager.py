import os
import shutil
from PyQt6.QtWidgets import QFileDialog
from pathlib import Path

# only one class instance
class shellItemManager():
    """
    Class for making an object for finding files/directories and passing on the lists to other functions
    """
    def __init__(self):
        self._lastDirectory = "C:"
        pass
        
    def importShellItem(self, mode: int):
        """
        Get a shell item
        """
        if type(mode) == int:

            dialog = QFileDialog() 

            if not mode:
                chosenFiles, delete = dialog.getOpenFileNames(None, "Import Media Item", str(self._lastDirectory), "Image Files (*.png *.gif *.jpg *.jpeg);;Text (*.txt);;Video Files (*.mp4);;Audio Files (*.mp3 *.m4a)")
                self._lastDirectory = Path(chosenFiles[0]).parent
                return chosenFiles
            
            elif mode:
                chosenDir = dialog.getExistingDirectory(None, "Import Collection Item", str(self._lastDirectory))
                self._lastDirectory = Path(chosenDir).parent
                return chosenDir
            
            else:
                raise ValueError("--mode can only be 0 or 1")
            
        else:
            raise TypeError(f"--method expects mode argument of type int but instead received {type(mode)}")
    
    def findShellItem(self):
        # call finder
        # call import
        pass
    
    def deleteShellItem(self, absoluteFile):
        shutil.move(absoluteFile, "destination")
        print("deleted")