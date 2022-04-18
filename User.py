import dropbox as dropbox


class User:
    def __init__(self,userName="",password="",oAuthKey=""):
        self.userName = userName
        self.password = password
        self.oAuthKey = "sl.BF_2p_WIZnmdW4MIWDb6yqSDCr-f7M1B0PGIyDyzNZ1OfuP6yDWnzx1F3cVAAD7sB0WN6P642bwPfEJ47THcBBfk1MhW-axNmueWMLcAL8bRhzCP3TMQpCH5iUXm6MSxT288jw69FHuF"
        

    def GetUserName(self):
        return self.userName

    
