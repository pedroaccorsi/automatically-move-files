# downloads-organizer
 
This script adds a listenner to my Downloads directory (excluding its subsidrectories). Whenever a new file is added to it, it is moved to a separete folder as per its file type. These are the hardcoded destinations:

```python

    def __get_target_dir(self, file_ext):
        if  (file_ext == '.jpg'  or file_ext == '.png' ): return self.downloads +'images/'    
        elif(file_ext == '.zip'  or file_ext == '.rar' ): return self.downloads +'compressed/'
        elif(file_ext == '.mkv'  or file_ext == '.mp4' ): return self.downloads +'videos/'    
        elif(file_ext == '.docx' or file_ext == '.doc' ): return self.downloads +'words/'     
        elif(file_ext == '.sap'                        ): return self.downloads +'conections/'
        elif(file_ext == '.torrent'                    ): return self.downloads +'torents/'   
        elif(file_ext == '.xlsx'                       ): return self.downloads +'excel/'
        elif(file_ext == '.pptx'                       ): return self.downloads +'ppts/'      
        elif(file_ext == '.pdf'                        ): return self.downloads +'pdfs/'      
        elif(file_ext == '.exe'                        ): return self.downloads +'exec/'  
        elif(file_ext == '.abap'                       ): return self.downloads +'abap/'    
        elif(file_ext == '.txt'                        ): return self.downloads +'txts/'    
        else:                                             return self.downloads +'others/'
```

A future idea is to make these definitions be set via *config.ini* or something alike, so that it can be changed without having to rewrite the script. This will be usefull in case it is converted into a *.exe* for future use.

