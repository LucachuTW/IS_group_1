import json
import AbstractHouseModel

class HouseModel(AbstractHouseModel.AbstractHouseModel):
    def __init__(self):
        self.setRelationships()
        #@Ventupentu
        #@SantiagoRR2004 added the environment.json
        with open("environment.json","r") as file:
            data = json.load(file)
        self.grid = data["grid"]
        self._availableDrugs: int = data["cabinet"]["numberDrugs"]

    def addDrug(self, quantity):
        #@Ventupentu
        self._availableDrugs += quantity

    def getDrug(self):
        #@Ventupentu
        return self._availableDrugs
    
    def changePosition(self,originX,originY,destinationX,destinationY):
        # Created by @SantiagoRR2004
        value = self.grid[originX,originY]
        self.grid[originX,originY] = "--"
        self.grid[destinationX,destinationY] = value
