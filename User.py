from asyncio.windows_events import NULL
import dropbox as dropbox


class User:
    Id = 0
    def __init__(self,userName="",password="",oAuthKey=""):
        
        self.userName = userName
        self.password = password
        self.oAuthKey = "sl.BJPzQCSbwk0yZAtKfmgEDiQALUAgjfdWthIZXz7khrDe0DlruzUcQ-R2N7FiAgViJvKVzUGSsC0N8wYhPQkwY-6o8IzbcaoDZXbGMECTa9lgf07Q9hiEBQqJcJxokucug4U5xg9V3v16"
        
        
    def SetUserId(self,Id):
        self.Id = Id

    def GetUserName(self):
        return self.userName

    
