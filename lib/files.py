from lib.abstract import AbstractFileActions
import pickle
import user


#DRY -dont repeat yuself
class PickleFileActions(AbstractFileActions):
    def __init__(self):
        pass
    
    def saveUser(self, user, filename):
        with open(filename, "wb") as f:
            pickle.dump(user, f)

    def loadUser(self, filename):
        with open(filename, "rb") as f:
            return pickle.load(f)