import dropbox as dropbox


class User:
    def __init__(self,userName,password,authCode = ""):
        self.userName = userName
        self.password = password
        self.authCode = authCode

    def GetUserName(self):
        return self.userName

    
