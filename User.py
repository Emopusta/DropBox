import dropbox as dropbox


class User:
    def __init__(self,userName,password):
        self.userName = userName
        self.password = password
        

    def GetUserName(self):
        return self.userName

    
