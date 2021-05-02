import os
from datetime import datetime
from shutil import make_archive
import time

class backup:

    def __init__(self):
        self.backupDir = "" # zip file save path
        self.sourceDir = "" # source files path
    
    def backupTime(self):
        date = datetime.now()
        if(date.hour == 21): # time 24-hour clock format
            return True
        else:
            time.sleep(1800)
            return False

    def zipFile(self,zipName):
        os.chdir(self.backupDir)
        make_archive(zipName,"zip",self.sourceDir)
    
    def backupStart(self):
        while True:
            if self.backupTime():
                self.zipFile("dailyBackup")
                time.sleep(3600)
        

if __name__ == "__main__":
    x = backup()
    x.backupStart()
