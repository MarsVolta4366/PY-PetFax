from flask import ( Blueprint, render_template )
import json

pets = json.load(open("pets.json"))
# print(pets)
bp = Blueprint("pet", __name__, url_prefix="/pets")

@bp.route("/")
def index():
    return render_template("pets/index.html", pets=pets)

@bp.route("/show/<int:id>")
def showPet(id):
    pet = pets[id - 1]
    return render_template("pets/showPet.html", pet=pet)