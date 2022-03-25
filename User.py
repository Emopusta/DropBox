import dropbox as dropbox


class User:
    def __init__(self,userName,password,oAuthKey=""):
        self.userName = userName
        self.password = password
        self.oAuthKey = "sl.BEQ3W8htqgDUTPhf9bcKF4Uz7icA0makJMLH4BvssSuEnKs52it1ME44AsRO47joec9GQ15T4jUqv6mY9cEmQpxLnGqZokLF-Zr1tp21tJy0lwdNnb1zWo6ph--l7hyOAv1ymtdfcEUa"
        

    def GetUserName(self):
        return self.userName

    
