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
        self.password = "6cb427bf2577947e39671187cd319b44"

        # dir info
        self.filePath1 = r'C:\AKINSOFT'
        self.filePath2 = r'C:\Users\pc\Desktop'
        self.tmp = r'C:\Users\pc\AppData\Local\Temp'

        
    def backupTime(self):
        date = datetime.now()
        today = date.today()
        bcpTime = today.strftime("%d")

        self.desktopStatus = False
        self.akinsoftStatus = False

        lastBackupTime = 5
        
        if bcpTime[0] == "0":
            bcpTime = int(bcpTime[1])
        else:
            bcpTime = int(bcpTime)

        if(date.hour == 9):
            self.akinsoftStatus = True
            if((bcpTime - lastBackupTime) == 7 or (lastBackupTime - bcpTime) == 7):
                self.desktopStatus = True
        else:
            print("saat bekleniyor.")
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
            print("Giriş yapılıyor...")
            self.login()
            print("akinsoft zipleniyor...")
            self.makeArchive(self.zip1,self.filePath1)
            self.upload(self.zip1)
            print("zip yüklendi...")
            time.sleep(43200)

        if self.desktopStatus:
            print("desktop zipleniyor...")
            self.login()
            self.makeArchive(self.zip2,self.filePath2)
            self.upload(self.zip2)
            time.sleep(43200)


    def login(self):
        self.conn = ftplib.FTP(self.host)
        self.conn.login(user=self.user,passwd=self.password)
        print("Bağlandı...")
 
    def upload(self,zipName):
        name = zipName+'.zip'
        bcpFile = open(name,'rb')
        self.conn.storbinary('STOR '+name,bcpFile)
        self.conn.quit()

    # temp dir and server old backup clear
    def clean(seld):
        pass

    def main(self):
        self.backupStart()

if __name__ == '__main__':
    backup = backup()
    while True:
        backup.backupStart()
