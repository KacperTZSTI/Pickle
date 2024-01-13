import user 
from lib.files import PickleFileActions
fa = PickleFileActions()

u = fa.loadUser("plik")

u.info()