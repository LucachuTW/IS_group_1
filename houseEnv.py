import AbstractHouseEnv
from typing import List


class HouseEnv(AbstractHouseEnv.AbstractHouseEnv):
    def __init__(self) -> None:
        pass

    def checkAddDrug(self, element: str, quantity: int) -> bool:
        # @antonoterof
        # Modified by @Ventupentu
        # @SantiagoRR2004
        model = self.getModel()

        toret = False

        if (
            (quantity + model.getDrug(element)) <= model.getCapacity(element)
            and (model.getDrug(element) + quantity) >= 0
            and (not self.checkOpeneable(element) or model.getOpenStatus(element))
        ):
            toret = True

        return toret

    def checkOpeneable(self, element: str) -> bool:
        # @Ventupentu
        # @SantiagoRR2004
        model = self.getModel()
        return model.getAttributeFromDict(element, "openable")

    def areAdjacent(
        self,
        object1: str,
        object2: str,
        position1: List[int] = "",
        position2: List[int] = "",
    ) -> bool:
        # @SantiagoRR2004
        model = self.getModel()
        toret = False

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
            toret = True

        return toret

    def transferDrugs(
        self, mover: str, giver: str, reciever: str, quantity: int
    ) -> bool:
        # @Ventupentu
        # Modified by @SantiagoRR2004
        model = self.getModel()
        toret = False

        if (
            self.checkAddDrug(reciever, quantity)
            and self.checkAddDrug(giver, -quantity)
            and self.areAdjacent(mover, reciever)
            and model.getAttributeFromDict(mover, "moving")["auto"]
        ):
            model.addDrug(reciever, quantity)
            model.addDrug(giver, -quantity)
            toret = True

        return toret

    def checkIfShareable(self, element: str) -> bool:
        # The element can share space with another right now
        # Antón Of
        # @SantiagoRR2004
        model = self.getModel()

        return model.getSemisolidStatus(element) and (
            not self.checkOpeneable(element) or model.getOpenStatus(element)
        )

    def checkIfMovableTo(self, x: int, y: int) -> bool:
        # @antonoterof
        # @SantiagoRR2004
        model = self.getModel()
        char = model.getPosition(x, y)
        symbols = model.getAttribute("symbols")
        toret = False

        if char == 0 or (
            model.checkIfPrime(char)
            and self.checkIfShareable(
                list(symbols.keys())[list(symbols.values()).index(char)]
            )
        ):
            toret = True

        return toret

    def moveTo(self, mover: str, moved: str, x: int, y: int) -> bool:
        # @Ventupentu
        # @SantiagoRR2004
        model = self.getModel()
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        movedSymbol = model.getAttributeFromDict(moved, "symbol")
        movedToSymbol = model.getPosition(x, y)
        moverCoord = model.getPositionOf(mover)
        movedCoord = model.getPositionOf(moved)

        toret = True

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

        elif not self.checkIfShareable(moved) and movedToSymbol != 0:
            toret = False

        if toret:
            if movedToSymbol == 0:
                model.setPosition(x, y, movedSymbol)
            else:
                model.setPosition(x, y, movedSymbol * movedToSymbol)

            if model.getPosition(movedCoord[0], movedCoord[1]) == movedSymbol:
                model.setPosition(movedCoord[0], movedCoord[1], 0)

            else:
                model.setPosition(
                    movedCoord[0],
                    movedCoord[1],
                    model.getPosition(movedCoord[0], movedCoord[1]) / movedSymbol,
                )

        return toret
