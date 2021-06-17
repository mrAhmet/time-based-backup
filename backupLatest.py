import os
from datetime import datetime
from shutil import make_archive
import time
import ftplib

class backup:
    def __init__(self):
        # server info
        self.host = "192.168.1.48"
        self.user = "hurmaciniz"
        self.password = "Password1"

        # dir info
        self.savePath = '/Users/ahmet/Desktop/' # zipin kayit edilecek yol
        #self.filePath = 'C:\Users\pc\Desktop' # yedekelenecek dosyanin yolu
        #self.filePath2 = 'C:\AKINSOFT'

        # yedek klasor yollari
        self.filePath1 = '/Users/ahmet/Desktop/yedek'
        self.filePath2 = '/Users/ahmet/Desktop/yedek2'

        # zip isimleri
        self.zip1 = 'hurmacinizBackup1' 
        self.zip2 = 'hurmacinizBackup2'
        
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