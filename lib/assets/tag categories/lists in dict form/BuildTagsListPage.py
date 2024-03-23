import re
from collections import deque

def buildList(FileSource):
        prev_indents = 0
        line_deque = deque()
        
        with open(FileSource, 'r') as file:
            for i, j in enumerate(file):
                header = None
                body = None
                indents  = len(re.findall(r'\t', j))
                diff = prev_indents - indents
   
                j = str(j.strip())
                
                if j:
                    try:
                        header = re.findall(r'[^{][a-z 0-9 _ - \[ \] /]*:', j)[0]
                        header = header.split(':')[0]
                        
                        body = re.findall(r'\[.*\]', j)[0]
                        body = re.findall(r'[^\[].*[^\]]', body)[0]
                        
                    except Exception as e:
                        print(e)
                        
                    finally:
                        ## first pass inputs automatically
                        if len(line_deque) == 0:
                            line_deque.append({'header': header, 'body': body, 'level': indents+1, 'object': ""})
                        else:
                            #subsection
                            if (diff) < 0:
                               line_deque[len(line_deque) - 1].pop('body')
                               line_deque.append({'header': header, 'body': body, 'level': indents+1, 'object': ""})
                            #different section or same section
                            else:
                                line_deque.append({'header': header, 'body': body, 'level': indents+1, 'object': ""})
                                
                        header = None
                        body = None
                        prev_indents = indents
        return line_deque

def saveList(line_deque, FileOutput):
    with open(FileOutput, 'w') as file:
            for line in line_deque:
                    file.write(str(line))
                    file.write('\n')

if __name__ == "__main__":
        TagsSourceDirectory = r'C:\Users\Aqua\Mega\Code\Tagging Program\lib\assets\tag categories\7 - Adorations and Overall Mood.txt'
        TagsOutput = r'C:\Users\Aqua\Mega\Code\Tagging Program\lib\assets\TagCategoriesDeque.txt'

        Lines = buildList(TagsSourceDirectory)
        saveList(Lines, TagsOutput)
