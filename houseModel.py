import json
import AbstractHouseModel
import houseEnv
import houseView


class HouseModel(AbstractHouseModel.AbstractHouseModel):
    def __init__(self):
        self.setRelationships(houseEnv.HouseEnv, houseView.HouseView)
        # @Ventupentu
        # Modified by @SantiagoRR2004
        with open("environment.json", "r") as file:
            data = json.load(file)

        self.grid = data["grid"]

        for key, value in data.items():
            if key not in data["notElements"]:
                self.setAttribute(key, value)

    def addDrug(self, object, quantity):
        # @Ventupentu
        # Modified by @SantiagoRR2004
        self.modifyNumericalAttributeFromDict(object, "numberDrugs", quantity)

    def getDrug(self, object):
        # @Ventupentu
        # Modified by @SantiagoRR2004
        return self.getAttributeFromDict(object, "numberDrugs")

    def getOpenStatus(self, object):
        # @Ventupentu-@LucachuTW
        # Modified by @SantiagoRR2004
        return self.getAttributeFromDict(object, "open")

    def setOpenStatus(self, object, status):
        # @Ventupentu-@LucachuTW
        # Modified by @SantiagoRR2004
        self.setAttributeFromDict(object, "open", status)

    def getCapacity(self, object):
        # @Ventupentu
        # Modified by @SantiagoRR2004
        return self.getAttributeFromDict(object, "maxCapacity")

    def changePosition(self, originX, originY, destinationX, destinationY):
        # Created by @SantiagoRR2004-@antonvm2004
        value = self.getPosition(originX, originY)
        self.setPosition(originX, originY, "--")
        self.setPosition(destinationX, destinationY, value)

    def getPosition(self, x, y):
        # Created by @antonvm2004
        return self.grid[x][y]

    def setPosition(self, x, y, value):
        # Created by @antonvm2004
        self.grid[x][y] = value
