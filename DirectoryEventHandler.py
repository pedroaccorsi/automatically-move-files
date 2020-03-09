from   watchdog.events import FileSystemEventHandler
import os, time, shutil, paths

class DirectoryEventHandler(FileSystemEventHandler):

    def __init__(self):
        self.downloads = paths.destine

    def on_created(self, event):
        
        time.sleep(0.15)
        file_ext = os.path.splitext(event.src_path)[1]

        if(file_ext and file_ext != '.tmp'):
            file_ext    = file_ext.lower()
            file_name   = self.__get_file_name(event.src_path)
            source_path = self.__get_source_path(event.src_path)
            target_path = self.__get_target_path(source_path, file_name, file_ext)
            file_name   = self.__update_file_name(target_path, file_name, file_ext)

            try:
                shutil.move(source_path, destination := target_path+file_name)
            except Exception as e:
                print(e)

    def __update_file_name(self, target_path, file_name, file_ext):
        i = 0
        while(self.__file_already_exists(target_path, file_name, file_ext)):
            i += 1
            file_name = self.__rename_file(file_name, i)
        return file_name

    def __file_already_exists(self, target_path, file_name, file_ext):
        return os.path.exists(target_path+file_name)

    def __rename_file(self, file_name, i):
        dir, ext = os.path.splitext(file_name)
        dir_len = len(dir)

        if(i > 1):
           dir = dir[:dir_len-3]+'({})'.format(i)+ext
        else:
           dir = dir[:dir_len]+' ({})'.format(i)+ext
        return dir

    def __get_file_name(self, path):
        last_slash = path.rfind('\\')
        file_name  = path = path[last_slash+1:]
        return file_name
            
    def __get_source_path(self, file_path):
        last_slash = file_path.rfind('\\')
        file_path  = file_path[:last_slash] + "/" + file_path[last_slash+1:]
        return file_path

    def __get_target_path(self, file_path, file_name, file_ext):
        target_dir = self.__get_target_dir(file_ext)
        if(os.path.exists(target_dir) == False):
            os.makedirs(target_dir)
        return target_dir   


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
       