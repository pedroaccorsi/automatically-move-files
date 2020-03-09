from watchdog.observers    import Observer
from DirectoryEventHandler import *
import paths
import time

class DirectoryListenner:
    def __init__(self, src_path):
        self.__src_path = src_path
        self.__event_handler = DirectoryEventHandler()
        self.__event_observer = Observer()

    def run(self):
        self.start()
        try                     : self.__infinite_loop()
        except KeyboardInterrupt: self.stop()
        except Exception as e   : self.stop()

    def __infinite_loop(self):
        while True: time.sleep(1)

    def start(self):
        self.__schedule()
        self.__event_observer.start()

    def stop(self):
        self.__event_observer.stop()
        self.__event_observer.join()

    def __schedule(self):
        self.__event_observer.schedule(
            self.__event_handler,
            self.__src_path,
            recursive=False
        )
