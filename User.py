import dropbox as dropbox


class User:
    def __init__(self,userName="",password="",oAuthKey=""):
        self.userName = userName
        self.password = password
        self.oAuthKey = "sl.BHvWzbS400_s2-qitKBRsU74eW2bfnTpI0GrIZf35dHWzfcz2HArC_gFqVEYmyZif4Tpj-SOnjm0x0oMzPo2rT7jMIbWCLBBW8UDNy_RXo0fmsA8ixIXBz1OEqNnefKe1nNMDIWt3M-w"
        

    def GetUserName(self):
        return self.userName

    
