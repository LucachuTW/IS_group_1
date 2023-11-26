import AbstractHouseEnv


class HouseEnv(AbstractHouseEnv.AbstractHouseEnv):
    def __init__(self) -> None:
        pass

    def checkAddDrug(self, object, quantity):
        # @antonoterof
        # Modified by @Ventupentu
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

    def checkOpeneable(self, object):
        # @Ventupentu
        model = self.getModel()
        if model.getAttributeFromDict(object, "openable"):
            return True
        else:
            return False

    def areAdjacent(self, object1, object2, position1="", position2=""):
        # @SantiagoRR2004
        model = self.getModel()
        if (
            position1 == ""
            and model.getAttributeFromDict(object1, "unique")
            and model.getPositionOf(object1)
        ):
            position1 = model.getPositionOf(object1)

        if (
            position2 == ""
            and model.getAttributeFromDict(object2, "unique")
            and model.getPositionOf(object2)
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

    def checkIfShareable(self, element: str) -> bool:
        # The element can share space with another right now
        # Antón Of
        model = self.getModel()
        if model.getSemisolidStatus(element) == False:
            return False
        if model.getOpenableStatus(element) == True:
            if model.getOpenStatus(element) == True:
                return True
            else:
                return False
        if model.getOpenableStatus(element) == False:
            return True

    def checkIfMovableTo(self, x: int, y: int) -> bool:
        # @antonoterof
        model = self.getModel()
        if int(model.getPosition(x, y)) == 0:
            return True
        if not model.checkIfPrime(int(model.getPosition(x, y))):
            return False
        if model.getPosition(x, y) != 0:
            for element in model.getAttribute("symbols"):
                if model.getAttributeFromDict("symbols", element) == model.getPosition(
                    x, y
                ):
                    if self.checkIfShareable(element) == True:
                        return True
                    else:
                        return False

    def moveTo(self, mover: str, moved: str, x: int, y: int) -> bool:
        # @Ventupentu
        # @SantiagoRR2004
        model = self.getModel()
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        movedSymbol = model.getAttributeFromDict(moved, "symbol")
        moverCoord = model.getPositionOf(mover)
        movedCoord = model.getPositionOf(moved)

        # toret = None

        if not self.checkIfMovableTo(x, y):
            toret = False

        elif mover == moved and not model.getAttributeFromDict(moved, "moving")["auto"]:
            toret = False

        elif mover != moved and (
            not model.getAttributeFromDict(mover, "moving")["mover"]
            or not model.getAttributeFromDict(moved, "moving")["moved"]
        ):
            toret = False

        elif not self.areAdjacent(mover, moved):
            toret = False

        elif not self.areAdjacent(moved, "None", position2=[x, y]):
            toret = False

        elif not self.checkIfShareable(moved) and int(model.getPosition(x, y)) != 0:
            toret = False

        else:
            toret = True

        if toret:
            if int(model.getPosition(x, y)) == 0:
                model.setPosition(x, y, movedSymbol)
            else:
                model.setPosition(x, y, movedSymbol * model.getPosition(x, y))

            if model.getPosition(movedCoord[0], movedCoord[1]) == movedSymbol:
                model.setPosition(movedCoord[0], movedCoord[1], 0)

            else:
                model.setPosition(
                    movedCoord[0],
                    movedCoord[1],
                    model.getPosition(movedCoord[0], movedCoord[1]) / movedSymbol,
                )

        return toret
