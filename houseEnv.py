import AbstractHouseEnv


class HouseEnv(AbstractHouseEnv.AbstractHouseEnv):
    def __init__(self) -> None:
        pass

    def checkAddDrug(self, object, quantity):
        # @antonoterof
        # modified by @Ventupentu
        model = self.getModel()
        if object == "cabinet":
            if model.getOpenStatus(object) == False:
                return False
        if (model.getDrug(object) + quantity) < 0:
            return False
        if (quantity + model.getDrug(object)) > model.getCapacity(object):
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
        # @Ventupentu
        # Modified by @SantiagoRR2004
        model = self.getModel()
        if (
            self.checkAddDrug(reciever, quantity)
            and self.checkAddDrug(giver, -quantity)
            and self.areAdjacent(mover, reciever)
            and model.getAttributeFromDict(mover, "moving")["auto"]
        ):
            model.addDrug(reciever, quantity)
            model.addDrug(giver, -quantity)
            return True

        else:
            return False
