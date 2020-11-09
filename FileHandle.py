from cryptography.fernet import Fernet
import json

class FileEncrytion:
    
    def CreateKey(self):
        self.key=Fernet.generate_key()
        self.fernet=Fernet(self.key)

    def LoadKey(self,path):
        f=open(path,'rb')
        self.key=f.read(44)
        self.fernet=Fernet(self.key)
        f.close()

    def LoadSettings(self,path):
        f=open(path,'rb')
        f.seek(44,0)
        data=f.read()
        f.close()
        return json.loads(self.fernet.decrypt(data).decode('utf-8'))

    def EncryptedWrite(self,data,path):
        f=open(path,'wb')
        f.write(self.fernet.encrypt(bytes(data,'utf-8')))
        f.close()

    def EncryptedRead(self,path):
        f=open(path,'rb')
        data=f.read()
        decData=self.fernet.decrypt(data).decode('utf-8')
        f.close()
        return decData

    def Write(self,data,path,mode='w'):
        f=open(path,mode)
        f.write(data)
        f.close()

    def Read(self,path,mode='r'):
        f=open(path,mode)
        data=f.read()
        f.close()
        return data
    def WriteKey(self,path):
        f=open(path,'wb')
        f.write(self.key)
        f.close()

    def WriteSettings(self,path,settings):
        f=open(path,'ab')
        f.write(self.fernet.encrypt(bytes(json.dumps(settings),'utf-8')))
        f.close()
