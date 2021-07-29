import flask_login as fl
import jsonConfig as jc

class User(fl.UserMixin):

    def __init__(self, name):
        self.id = name
        self.name = "user" + str(id)
        self.password = self.name + "_secret"
        self.single = True
        self.accounts = ["Sheppy", "TheArmCommander"]
        self.selectedChampions = ["Lulu", "Aatrox", "Brand"]
        self.matchhistoryEntries = []
        
    def __repr__(self):
        return self.id

    def __str__(self):
        return str(self.id)

    def allowedFeatures(self):
        '''Dynamicly return the features this user is allowed to use'''

        allFeatures = jc.readJsonDir("config/tables/")
        allowedFeatures = []
        if not allowedFeatures:
            allowedFeatures = allFeatures
        else:
            allowedFeatures = filter(lambda x: x["title"] in allowedFeatures, 
                                        allFeatures)
        return sorted(allowedFeatures, key=lambda x: x["title"])
