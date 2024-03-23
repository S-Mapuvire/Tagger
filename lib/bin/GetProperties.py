##########################################################################
## Imports
##########################
## Path: is used for getting the containing folder of the chosen file. 
## win32com.client: is supplimentary code that assists with instantiating a static dispatch 
## win32gui: is only for a reference to the window over which to put the dialog
## win32com.shell:
##          shell is used for it's methods for converting display names and pidl's 
##          shellcon is used for flags related to methods
##########################################################################
from pathlib import Path
from win32com.client import Dispatch, gencache
import sys

##########################################################################
## Globals
############################
## old_prop_list: is the 'traditional' set of file properties considered 'relevant'
## new_prop_list: is the 'new' set of file properties considered 'relevant'
##########################################################################
OLD_PROP_LIST = {'Name' : 'Full Name', 'Title' : 'Full Source', 'Authors' : 'Creator(s)', 'Tags' : 'Tags', 'Comments': 'Copyright(s)',
                 'Size' : 'Size', 'Item type' : 'Type', 'Date created' : 'Date created', 'Date modified' : 'Date modified',
                 'Length' : 'Length', 'Dimensions' : 'Dimensions', 'Duration' : 'Duration', 'File extension' : 'Extension',
                 'Filename' : 'Filename', 'Width' : 'Width', 'Height' : 'Height',
                 'Folder Name' : 'Folder Name', 'Folder path' : 'Folder path', 'Folder' : 'Folder', 'Path' : 'Path',
                 'Frame height' : 'Video Height', 'Frame rate' : 'Framerate', 'Frame width' : 'Video Width'}

NEW_PROP_LIST = {'Name' : 'Full Name', 'Required attendees' : 'Subject(s)', 'Parental rating' : 'Rating', 'Authors' : 'Creator(s)',
                 'Required attendee addresses' : 'copyright(s)', 'Business address' : 'md5', 'Tags' : 'All tags(s)',
                 'Categories' : 'Image Composition and Style Tags', 'Optional attendees' : 'Animation Tags',
                 'Bcc addresses' : 'Body Tags', 'Cc addresses' : 'Attire and Accessories Tags',
                 'Optional attendee addresses' : 'Settings, Relations, and Roles Tags', 'IM addresses' : 'Sexual and nc-ish Tags',
                 'To addresses' : 'Adorations and Mood', 'Part of set' : 'Set', '#' : 'No. in Set', 'Comments' : 'Commentary',
                 'Language' : 'Translation(s)', 'Business city' : 'Search Keywords', 'User web URL' : 'Full Source',
                 'Email display name' : 'Website Name', 'Email address' : 'Specific Booru Page', 'Email2' : 'Stored Page',
                 'Email3' : 'Source URL(s)', 'Duration' : 'Duration', 'Frame width' : 'Video Width', 'Frame height' : 'Video height',
                 'Bit rate' : 'Bit rate', 'Frame rate' : 'Frame Rate', 'Dimensions' : 'Dimensions',
                 'Width' : 'Width', 'Height' : 'Height', 'Bit depth' : 'Bit depth',
                 'Horizontal resolution' : 'Horizontal Resolution', 'Vertical resolution' : 'Vertical Resolution',
                 'Size' : 'Size', 'Date created' : 'Date created', 'Date modified' : 'Date modified',
                 'Item type' : 'Item type', 'Kind' : 'Kind', 'Folder' : 'Folder', 'Folder path' : 'Folder path',
                 'Attributes' : 'Attributes', 'Owner' : 'Owner', 'Computer' : 'Computer'}

##########################################################################
## Order of operations
##########################
## 1) Make a dispatch object, 
## 2) Make folderObject using shell.NameSpace(path)
## 3) Make fileObject using folderobject.ParseName(file)
## 4) Cycle through property list keys, according to the order in new_prop_list
##  i.e. Set each element of properties_list to have the key of the value for each of new_prop_list element,
## and the values to have the values of the file properties.
##########################################################################

"""
GetProperties(Path Name, Path Directory)

    Returns a dictionary of file properties.

    Directory is used to create a folder object.
    The folder object is used to create a file object.

    The chosen list of 'relevant' properties is iterated through,
    creating a dictionary in it's order.

    Keys are the aliased names of the propery categories as written in new_prop_list
    Values of this dictionary are the actual file's (Name's) properties.
"""
def GetProperties(Name, Directory):
    comparison_var = Path(r'C:')
    if type(Name) != type(comparison_var) or type(Directory) != type(comparison_var):
        raise ValueError('Filename and Directory have to be Path types.')
    if (not Name.is_file() or not Name.exists()):
        raise OSError("File path error - either Filename is not a file, or it does not exist.")
    if (not Directory.is_dir() or not Directory.exists()):
        raise OSError("Directory path error - either Directory is not a folder, or it does not exist.")
    
    PropertiesList = {}
    _shell = gencache.EnsureDispatch("Shell.Application")
    FolderObject = _shell.NameSpace(str(Directory))
    FileObject = FolderObject.ParseName(Name.name)
    print(dir(_shell))
    
    for index, prop in enumerate(NEW_PROP_LIST.keys()):
        try:
            PropertiesList[NEW_PROP_LIST[prop]] = FolderObject.GetDetailsOf(FileObject, index)
        except Exception as e:
            print(f'error {e}')
            
    return PropertiesList

if __name__ == "__main__":
    FileName =  Path(r'D:\=Images\---\darcy redd\darcy redd_explicit_andava_andavaverse_50f9514de80f1ee070656fc639866e37.jpg')
    FileDirectory = Path(r'D:\=Images\---\darcy redd')
    GetProperties(FileName, FileDirectory)
