from asyncio.windows_events import NULL
import dropbox as dropbox


class User:
    
    def __init__(self,Id=None,userName="",password="",oAuthKey=""):
        self.Id = Id 
        self.userName = userName
        self.password = password
        self.oAuthKey = ""
        
        
    def SetUserId(self,Id):
        self.Id = Id

    def GetUserName(self):
        return self.userName

    
