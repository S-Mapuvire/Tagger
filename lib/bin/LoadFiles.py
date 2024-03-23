##########################################################################
## Summary
##########################
## The module for whenever a file needs to be grabbed
## Can't figure out why using QFileDialog.getOpenFileNames()
## outside a Qt class doesn't consistently give results...
##########################################################################
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QFileDialog
import sys

"""
Dialog(QFileDialog)

A simple QFileDialog instance.
"""
class Dialog(QFileDialog):
    def __init__(self):
        super().__init__()

"""
get_file_list()

    Opens a dialog box for choosing files.
    Returns a list of strings.
"""
def LoadFiles():
    app = QApplication([])
    dialog = Dialog()

    file_list, delete = dialog.getOpenFileNames()
    print("loading file")
    return file_list

if __name__ == "__main__":
    LoadFiles()
