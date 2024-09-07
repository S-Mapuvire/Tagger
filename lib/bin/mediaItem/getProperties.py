#https://sylikc.github.io/pyexiftool/examples.html
from exiftool import ExifToolHelper
import os
from pathlib import Path

def getProperties(file):
    file = Path(file)
    if not (file.exists):
        raise ReferenceError("File path does not exist.")
    
    #  wantedProps = ["XMP:Title", "XMP:Subject", "XMP:RatingValue", "EXIF:Artist",
    #      "XMP:Copyright", "IPTC:Credit", "IPTC:ObjectName", "IPTC:ObjectAttributeReference", "IPTC:Keywords", 
    #      "IPTC:OwnerID", "IPTC:UniqueDocumentID", "IPTC:JobID",
    #      "IPTC:MasterDocumentID", "IPTC:ShortDocumentID", "EXIF:Model", "IPTC:City", "IPTC:Sub-location", "IPTC:By-lineTitle", "IPTC:By-line", "XMP:ArtworkSource", "IPTC:ContentLocationName", "XMP:ArtworkSourceInvURL", "EXIF:ImageDescription"]
        
    wantedProps = ["EXIF:ImageDescription", "EXIF:XPSubject", "XMP:RatingValue", "EXIF:Artist","EXIF:Copyright", "Microsoft:Conductor", "Microsoft:Director", "Microsoft:Producer", "IPTC:Keywords", "Microsoft:Writer", "Microsoft:Publisher", "ItemList:Composer","Microsoft:Period", "Microsoft:Mood", "XMP-MP:RegionPersonDisplayName", "ItemList:DiskNumber", "XMP-microsoft:LensManufacturer", "EXIF:UserComment", "EXIF:Make", "Microsoft:ContentDistributor", "Microsoft:AuthorURL", "Microsoft:PromotionURL", "XMP-microsoft:LensModel"]
    

    translatedProps = ["Title", "Characters", "Rating", "Artist",
         "Copyright", "Search List", "ID", "md5", "All Tags", 
         "Tag set 1", "Tag set 2", "Tag set 3",
         "Tag set 4", "Tag set 5", "Orientation", "Pool", "# in Pool", "Commentary", "Translation", "Website Name", "Page URL", "Image URL", "Source URL"]
    
    fileProps = wantedProps

    with ExifToolHelper() as et:
        for fileInfo in et.get_metadata(file):
            for propName, propValue in fileInfo.items():
                if propName in wantedProps:
                    fileProps[fileProps.index(propName)] = {translatedProps[fileProps.index(propName)] : propValue}

    return fileProps

    #d['File:FileType']