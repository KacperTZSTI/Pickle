from flask import Flask, request
import user 
from lib.files import PickleFileActions

fa = PickleFileActions()



app = Flask("app")

@app.route("/", methods=["GET"])
def main_route():
    u = fa.loadUser("plik")

    return u.info()

        