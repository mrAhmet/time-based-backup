import os
from datetime import datetime
from shutil import make_archive
import time
import ftplib

class backup:
    def __init__(self):
        # server info
        self.host = "" # ftp server host
        self.user = "" # ftp server user
        self.password = "" # ftp server password

        # dir info
        self.savePath = '' # save zip path

        # backup paths
        self.filePath1 = ''
        self.filePath2 = ''

        # zip names
        self.zip1 = '' 
        self.zip2 = ''
        
    def backupTime(self):
        date = datetime.now()
        if("{}".format(date.hour) == "{}".format(11)):
            return True
        else:
            time.sleep(1800)
            return False

    def makeArchive(self,name,path):
        os.chdir(self.savePath)
        make_archive(name,'zip',path)
        
    def backupStart(self):
        self.makeArchive(self.zip1,self.filePath1)
        self.makeArchive(self.zip2,self.filePath2)

    def login(self):
        self.conn = ftplib.FTP(self.host)
        self.conn.login(user=self.user,passwd=self.password) 

    def upload(self,file):
        try:
            zipname = file+'.zip'
            backupFile = open(zipname,'rb')
            self.conn.storbinary('STOR '+zipname,backupFile)
            #self.conn.quit()
        
        except:
            print("Error...")
    
    def main(self):
        while True:
            if self.backupTime():
                self.backupStart()
                self.login()
                self.upload(self.zip1)
                self.upload(self.zip2)
                self.conn.quit()
                print("3600 second")
                time.sleep(3600)

x = backup()
x.main()
