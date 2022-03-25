import dropbox as dropbox
from User import User 
class DropboxManager:

    def __init__(self,admin):
        dbx = dropbox.Dropbox(admin.oAuthKey)
        dbx.users_get_current_account()
        self.OAuthKey = dbx._oauth2_access_token
        

    def UploadFile(self,privateKey,publicKey,file,destination,sendTo):
        return 0
