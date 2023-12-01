import AbstractHouseEnv
from typing import List


class HouseEnv(AbstractHouseEnv.AbstractHouseEnv):
    """
    House Environment class that extends AbstractHouseEnv.

    This class provides methods to interact with the house environment.

    Contributors:
        - @SantiagoRR2004
    """
    def __init__(self) -> None:
        """
        Initialize the HouseEnv instance.

        Args:
            None

        Returns:
            None

        Contributors:
            - @SantiagoRR2004
        """
        pass

    def checkAddDrug(self, element: str, quantity: int) -> bool:
        """
        Check if the given quantity of drug can be added to the given element.

        Args:
            - element (str): The element to which the drug is to be added.
            - quantity (int): The quantity of drug to be added.

        Returns:
            bool: True if the drug can be added, False otherwise.

        Contributors:
            - @antonoterof
            - @Ventupentu
            - @SantiagoRR2004
        """
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
        """
        Check if the given element is openable.

        Args:
            - element (str): The element to be checked.

        Returns:
            bool: True if the element is openable, False otherwise.

        Contributors:
            - @Ventupentu
            - @SantiagoRR2004
        """
        model = self.getModel()
        return model.getAttributeFromDict(element, "openable")

    def areAdjacent(
        self,
        object1: str,
        object2: str,
        position1: List[int] = ","
        """
        Check if the given objects are adjacent.

        Args:
            - object1 (str): The first object.
            - object2 (str): The second object.
            - position1 (List[int]): The position of the first object.

        Returns:
            bool: True if the objects are adjacent, False otherwise.

        Contributors:
            - @SantiagoRR2004
        """
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

    def transferDrugs(self, origin: str, destination: str, quantity: int) -> bool:
        """
        Transfer the given quantity of drugs from the origin to the destination.

        Args:
            - origin (str): The origin of the transfer.
            - destination (str): The destination of the transfer.
            - quantity (int): The quantity of drugs to be transferred.

        Returns:
            bool: True if the transfer was successful, False otherwise.

        Contributors:
            - @SantiagoRR2004
        """
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
        """
        Check if the given element is shareable.

        Args:
            - element (str): The element to be checked.

        Returns:
            bool: True if the element is shareable, False otherwise.

        Contributors:
            - @SantiagoRR2004
        """
        model = self.getModel()

        return model.getSemisolidStatus(element) and (
            not self.checkOpeneable(element) or model.getOpenStatus(element)
        )

    def checkIfMovableTo(self, x: int, y: int) -> bool:
        """
        Check if the given coordinates are movable.

        Args:
            - x (int): The x-coordinate to be checked.
            - y (int): The y-coordinate to be checked.

        Returns:
            bool: True if the coordinates are movable, False otherwise.

        Contributors:
            - @SantiagoRR2004
        """
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
        """
        Move the 'moved' element to the given coordinates.

        Args:
            - mover (str): The element that is moving.
            - moved (str): The element to be moved.
            - x (int): The x-coordinate to move to.
            - y (int): The y-coordinate to move to.

        Returns:
            bool: True if the move was successful, False otherwise.

        Contributors:
            - @Ventupentu
            - @SantiagoRR2004
        """
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
