import os
from datetime import datetime
from datetime import date
import hashlib
from shutil import make_archive
import time
import ftplib

class backup:

    def __init__(self):
        # server info
        self.host = "192.168.1.48"
        self.user = "hurmaciniz"
        self.hashAL = hashlib.new('MD5')
        self.hashAL.update("hrm2021hrm")
        self.password = self.hashAL.hexdigest()

        # dir info
        self.filePath1 = 'C:\Users\pc\Desktop' 
        self.filePath2 = 'C:\AKINSOFT'
        self.tmp = 'C:\Users\pc\AppData\Local\Temp'

        
    def backupTime():
        date = datetime.now()
        today = date.today()
        bcpTime = today.strftime("%d")

        desktopStatus = False
        akinsoftStatus = False

        lastBackupTime = 12
        
        if bcpTime[0] == "0":
            bcpTime = int(bcpTime[1])
        else:
            bcpTime = int(bcpTime)

        if(date.hour == 9):
            akinsoftStatus = True
            if((bcpTime - lastBackupTime) == 7 or (lastBackupTime - bcpTime) == 7):
                desktopStatus = True
        else:
            time.sleep(1800)

    def makeArchive(self,name,path):
        os.chdir(self.tmp)
        make_archive(name,'zip',path)
        
    def backupStart(self):
        self.backupTime()
        today = date.today()

        self.zip1 = "%s-akinsoft" % today.strftime("%d.%m.%Y")
        self.zip2 = "%s-desktop" % today.strftime("%d.%m.%Y")

        if self.akinsoftStatus:
            self.login()
            self.makeArchive(self.zip1,self.filePath1)
            self.upload()

        if self.desktopStatus:
            self.login()
            self.makeArchive(self.zip2,self.filePath2)
            self.upload()


    def login(self):
        self.conn = ftplib.FTP(self.host)
        self.conn.login(user=self.user,passwd=self.password) 
 
    def upload(self,zipPath):
        bcpFile = open("%s.zip" % zipPath)
        self.conn.storbinary('STOR {} {}'.format("%s.zip" % zipPath,bcpFile))
        self.conn.quit()

    # temp dir and server old backup clear
    def clean(seld):
        pass

    def main(self):
        self.backupStart()

if __name__ == '__main__':
    backup = backup()
    backup.backupStart()