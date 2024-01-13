import user 
import pickle #smell
from lib.files import PickleFileActions


fa = PickleFileActions()

n = input("Your name:")
n2 = input("Your surname:")
a = input("Your age:")

u = user.User(n, n2, a)


with open("plik", "wb") as f: #Kod smierdzi
    pickle.dump(u, f)
#fa.saveUser(u, "plik")

u.info()