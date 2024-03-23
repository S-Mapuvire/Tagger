## figure out how to edit tag category and tag category (dict form) file once each time any section needs change



# add highlight to selected tags
# add dividers, more easily separate sections
# edit header sizes



##################### Imports #####################
##
## deque is used to hold the chosen tags
## Path is used for choosing files
## re is used for scanning the dict layout file
###################################################
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage, QPalette, QMovie, QAction
from PyQt6.QtMultimedia import QMediaPlayer, QAudio, QAudioOutput
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QDockWidget, QStackedWidget, QScrollArea,
                             QVBoxLayout, QGridLayout,
                             QButtonGroup,
                             QComboBox, QCheckBox, QPushButton, QLabel)

from collections import deque
from pathlib import Path
import re
import sys

##################### Main Object #####################
class TagPicker(QMainWindow):
    def __init__(self, startingTags):
        #### Window settings ####
        super().__init__()
        QPalette.WindowText
        self.setWindowTitle('Tag Selection')
        self.setMinimumSize(300,500)

        #### Globals ####
        self.tagsOnFile_to_tagsInPicker = []
        if type(startingTags) == list:
            for tag in startingTags:
                tag = tag.lower().strip()

            self._tags = startingTags
            self.missingTags = startingTags
            self.tagsOnFile_to_tagsInPicker.append(len(self._tags))
            self.tagsOnFile_to_tagsInPicker.append(0)
        else:
            raise ValueError('starting_tags should be type list')
        
        self._tagsDir = Path(r'C:\Users\Aqua\Mega\Code\Tagging Program\lib\assets\tag categories\lists in dict form')
        style_sheet = r'C:\Users\Aqua\Mega\Code\Tagging Program\lib\assets\pinkpill.css'

        with open(style_sheet, 'r') as sheet:
            self.setStyleSheet(sheet.read())

        #### UI Setup #####
        self._establishTagsSection()
        self._buildTagBox()
        self._addPrintButton()

    ##################### Build Container Widgets #####################
    ##
    ## _DockArea = the dock that holds the entire tag category system
    ## _Container = the holding widget that holds the tag checkboxes and page select
    ## _TagTabs = the stacked widget that holds the different tag category pages
    ## _Pages = the drop down that chooses the specific tag category section
    ## _AllButtons = the button group that holds the tag checkboxes
    ################################################################
    def _establishTagsSection(self):
        self._tagsDockArea = QDockWidget('Tags Section', self)

        self._tagsContainer = QWidget()
        self._tagsContainerLayout = QVBoxLayout(self._tagsContainer)
        self._tagsDockArea.setWidget(self._tagsContainer)

        self._tagTabs = QStackedWidget()
        self._tagsContainerLayout.addWidget(self._tagTabs)
        
        self._tagsPageSelector = QComboBox()
        self._tagsContainerLayout.addWidget(self._tagsPageSelector)        
        
        self._tagButtonsGroup = QButtonGroup(parent=self._tagsDockArea)
        self._tagButtonsGroup.setExclusive(False)
        self._tagButtonsGroup.buttonClicked.connect(self._display)
        
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, self._tagsDockArea)

    ##################### Build the tag checkbox area #####################
    ##
    ## Iterate through the files that hold the tag body and header orders

    ##
    ## Count = Row number
    ## ScrollArea = Basic unit of a tag checkbox area, inside of each page is a scroll area
    ## TagsArea =  Container inside the scroll area
    ##
    ################################################################
    def _buildTagBox(self):
        rowCount = 0

        for file in self._tagsDir.iterdir():
            if file.stem != 'BuildTagsListPage':
                
                ## Inside of each page is a scroll area
                tagsPageScrollArea = QScrollArea()
                tagsPageScrollArea.setWidgetResizable(True)
                tagsPageScrollAreaLayout  = QVBoxLayout(tagsPageScrollArea)
                self._tagTabs.addWidget(tagsPageScrollArea)

                ## Container inside the scroll area
                tagsPageContainer = QWidget()
                tagsPageContainer.setStyleSheet("background-color: beige")
                tagsPageContainerLayout = QGridLayout(parent=tagsPageContainer)
                tagsPageScrollArea.setWidget(tagsPageContainer)

                ## Add the page to the dropdown list
                self._tagsPageSelector.addItem(file.stem.split('- dict')[0])
                self._tagsPageSelector.activated.connect(self._tagTabs.setCurrentIndex)

                with open(file, 'r') as f:
                    for line in f:
                        ## Have to use eval because otherwise it's taken as a string
                        ## and casting doesn't work since it requires a key and value pair
                        tagSection = eval(f'{line}')
                        
                        ## Level determines the header size
                        if tagSection['level'] > 5:
                            level = 5 % tagSection['level']
                        else:
                            level = tagSection['level'] % 5
                            if level == 0:
                                level = 5
                        color =  'e' + str(level) + 'adb6'

                        ## Display a tag checkbox section
                        ## Row is incremented after every header
                        if 'body' in tagSection.keys():
                            header = QLabel(f"<h{level}>{tagSection['header']}", parent=tagsPageContainer)
                            header.setStyleSheet(f"background-color: #{color}; border: 1px double black")
                            # header.setStyleSheet("background-color: #e4adb6; border: 1px double black")
                            rowCount+=1
                            tagsPageContainerLayout.addWidget(header, rowCount, 0)
                            rowCount+=1
                            the_tags = tagSection['body'].split(',')

                            ## the_tags = the separate tags
                            ## remove whitespace, create a new checkbox object,
                            ## increment row if it is the 5th object,
                            ## add checkbox to container & to button group
                            for index, element in enumerate(the_tags):
                                message = element.strip()
                                tagSection['object'] = QCheckBox(message)
                                
                                if tagSection['object'].text() in self._tags:
                                    tagSection['object'].setChecked(True)
                                    self.missingTags.remove(tagSection['object'].text())
                                    self.tagsOnFile_to_tagsInPicker[1] = self.tagsOnFile_to_tagsInPicker[1]+1

                                if (index != 0 and index%5 == 0):
                                    rowCount+=1    
                                tagsPageContainerLayout.addWidget(tagSection['object'], rowCount, index%5)                    
                                self._tagButtonsGroup.addButton(tagSection['object'])
                            ## Increment row after a tag body section
                            rowCount+=1

                        ## Main headers
                        else:
                            header = QLabel(f"<h{level}>{tagSection['header']}", parent=tagsPageContainer)
                            # header.setStyleSheet(f"background-color: #eeced3; border: 1px double black")
                            
                            header.setStyleSheet(f"background-color: #{color}; border: 1px double black")
                            tagsPageContainerLayout.addWidget(header, rowCount, 0)
                            rowCount+=1
        print(f'There are {self.tagsOnFile_to_tagsInPicker[0]} tags on the file and {self.tagsOnFile_to_tagsInPicker[1]} of them are in the picker meaning {self.tagsOnFile_to_tagsInPicker[1]-self.tagsOnFile_to_tagsInPicker[0]} tags not in the picker')
        print(f'These are {self.missingTags}')

    ##################### Connection for tag checkboxes #####################
    def _display(self, button):
        if button.isChecked():
            self._tags.append(button.text())
        else:
            self._tags.remove(button.text())

    ##################### Printing the tag list #####################
    def printTags(self):
        self._tags.sort()
        finalTags = ""
        for tag in self._tags:
            finalTags = finalTags + tag + '; '
        print(finalTags)

    ##################### This button prints the tag list #####################
    def _addPrintButton(self):
        self.PrintTagButton = QPushButton("Print Tags")
        self._tagsContainerLayout.addWidget(self.PrintTagButton)
        self.PrintTagButton.clicked.connect(self.printTags)
        self.PrintTagButton.setObjectName("Print_Tag_Btn")
        print(self.PrintTagButton.setObjectName("printBtn"))

if __name__ == '__main__':
    app = QApplication([])
    tagsSection = TagPicker([])
    tagsSection.show()
    sys.exit(app.exec())
