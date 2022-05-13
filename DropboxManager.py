import dropbox as dropbox
from User import User 

class DropboxManager(User):

    def __init__(self,admin):
        dbx = dropbox.Dropbox(admin.oAuthKey)
        dbx.users_get_current_account()
        self.OAuthKey = dbx._oauth2_access_token
      
        
        deneme = str(dbx.files_list_folder("")).split(",")
        print(deneme)
        for i in deneme:
            if i.find("name="):
                print(i)


    def UploadFile(self,privateKey,publicKey,file,destination,sendTo):
        return 0
