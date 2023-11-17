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
        # Created by @SantiagoRR2004-@antonvm2004
        value = self.getPosition[originX,originY]
        self.setPosition(originX,originY, "--") 
        self.setPositoin(destinationX,destinationY, "value")

    def getPosition(self, x, y):
        # Created by @antonvm2004
        return self.grid[x,y]
    
    def setPosition(self, x, y, value):
        #Created by @antonvm2004
        self.grid[x,y] = value

    
