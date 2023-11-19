import AbstractHouseEnv


class HouseEnv(AbstractHouseEnv.AbstractHouseEnv):
    def __init__(self) -> None:
        pass

    def checkAddDrug(self, object, quantity):
        # @antonoterof
        model = self.getModel()
        if object == "cabinet":
            if model.getOpenStatus(object) == False:
                return False
        if (model.getAttributeFromDict(object, "numberDrugs") + quantity) < 0:
            return False
        if (
            quantity + model.getAttributeFromDict(object, "numberDrugs")
        ) > model.getAttributeFromDict(object, "maxCapacity"):
            return False
        else:
            return True

    def areAdjacent(self, object1, object2, position1="", position2=""):
        # @SantiagoRR2004
        model = self.getModel()
        if model.getAttributeFromDict(object1, "unique") and model.getPositionOf(
            object1
        ):
            position1 = model.getPositionOf(object1)

        if model.getAttributeFromDict(object2, "unique") and model.getPositionOf(
            object2
        ):
            position2 = model.getPositionOf(object2)

        distance = model.calculateDistanceBetween2Points(
            position1[0], position1[1], position2[0], position2[1]
        )

        if (
            distance <= 1
        ):  # This means you are on the same position, 1 horizontally or 1 vertically
            return True
        else:
            return False

    def transferDrugs(self, mover, giver, reciever, quantity):
        #@Ventupentu
        model = self.getModel()
        if model.getAttributeFromDict(giver, "numberDrugs") < quantity:
            return False
        if model.getAttributeFromDict(reciever, "numberDrugs") + quantity > model.getAttributeFromDict(reciever, "maxCapacity"):
            return False
        else:
            model.setAttributeFromDict(giver, "numberDrugs", model.getAttributeFromDict(giver, "numberDrugs") - quantity)
            model.setAttributeFromDict(reciever, "numberDrugs", model.getAttributeFromDict(reciever, "numberDrugs") + quantity)
            return True
        
        pass
