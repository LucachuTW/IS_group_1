import json

class HouseModel():
    def __init__(self):
        #@Ventupentu
        #@SantiagoRR2004 added the environment.json
        with open("environment.json","r") as file:
            data = json.load(file)
        self._availableDrugs: int = data["cabinet"]["numberDrugs"]

    def addDrug(self, quantity):
        #@Ventupentu
        self._availableDrugs += quantity

    def getDrug(self):
        #@Ventupentu
        return self._availableDrugs 