#this renames files by adding a prefix of 'unfav - ' to the start
#this can be generalised into a prefix-adder...hmmm
from pathlib import Path
import re
from PyQt6.QtWidgets import QFileDialog, QMainWindow, QApplication


# remover
# adder
# template rename
# template(seperator, )
# template edit


# def rename_remover(inputFiles: list, fragment: str):
#     if not(fragment):
#         raise KeyError("-function expects fragment but received none.")
#     if not(inputFiles):
#         raise KeyError("--function call is missing any file paths")
#     if type(inputFiles).__name__ != 'list':
#         raise TypeError(f"--function expects file path of type 'list' but received {type(inputFiles).__name__}")
    
#     for file in inputFiles:
#         originalfile = file = Path(file)

#         if not(file.exists):
#             raise FileNotFoundError("--file not found")

#         print(f"received {file}\n")
        
#         filename = file.stem
#         ext = file.suffix

#         filename_parts = re.split(fragment, filename)

#         filename = ""

#         # replace w a reduce
#         for element in filename_parts:
#             filename = filename + element

#         filename = filename + ext
        
#         file = file.parent/filename

#         originalfile.rename(file)

#         print(f"after removals, filename is now:\n {file}\n")

#         return file

# def rename_adder(inputFiles: list, *, prefix: str = "", suffix: str = "", fragment: str = "", frag_before: str = "", frag_after: str = ""):
    
#     if not(prefix or suffix or fragment):
#         raise KeyError("-function expects a prefix, a suffix, or a fragment but received none.")
#     if not(inputFiles):
#         raise KeyError("--function call is missing any file paths")
#     if not(type(inputFiles).__name__ == 'list'):
#         raise TypeError(f"--function expects file path of type 'list' but received {type(inputFiles)}")
    
#     for file in inputFiles:
#         originalfile = file = Path(file)
        
#         if not(file.exists):
#             raise FileNotFoundError("--file not found")
        
#         print(f"received {file}\n")
        
#         filename = file.stem
#         ext = file.suffix

#         filename_parts = f"{prefix + filename + suffix + ext}"

#         file = file.parent/filename_parts
        
#         originalfile.rename(file)
        
#         print(f"after additions, filename is now:\n {file}\n")

#         return file

# def template_renamer(template, template_sep, *new_template):
#     elements = template.split(template_sep)
#     for element in elements:
#         print(element)
#         print("enter new element")

# def template_changer(old_format, new_format, new_elements):
#     pass

if __name__ == "__main__":
    app = QApplication([])
    dialog = QFileDialog()

    file, delete = dialog.getOpenFileName()

    file = Path(file)

    # add word, remove word, 

    # re.split()
    # re.findall
    # re.search()

#     frag = input("type in thing to remove: ")
#     print(f"received {frag}")


#     rename_remover(inputFiles=[file], fragment=frag)


#     pre = input("type in prefix if any: ")
#     print(f"received {pre}")
#     suf = input("type in suffix if any: ")
#     print(f"received {suf}")

#     rename_adder(inputFiles=[file], prefix=pre, suffix=suf)

#     # name_template = "{creator}_{copyright}_{characters}_{md5}_{extension}"


#     # name = name_template.format(creator=elements[0], copyright=elements[1], characters=elements[2], md5=elements[3],extension=elements[4])