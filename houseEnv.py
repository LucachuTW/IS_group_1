import AbstractHouseEnv
from typing import List, Dict


class HouseEnv(AbstractHouseEnv.AbstractHouseEnv):
    """
    House Environment Class.

    This class represents the environment of a house.
    It includes methods to check if
    an element is shareable, if a position is movable,
    and to move an object to a specified position.

    Contributors:
        - @SantiagoRR2004
        - @Ventupentu
        - @antonoterof
        - @LucachuTW
    """

    def getFunctionsChangeModel(self) -> List:
        """
        Returns the list of functions to change the model.
        This was made to separete the controller from the view.
        This would be used by the graphical interface.

        Returns:
            List: A list of functions to change the model.

        Contributors:
            - @SantiagoRR2004
        """
        functionsChangeModel = [
            self.transferDrugs,
            self.moveTo,
            self.changeOpenClose,
            self.consumeDrugs,
        ]
        return functionsChangeModel

    def checkAddDrug(self, element: str, quantity: int) -> bool:
        """
        Check if a drug can be added to an element.

        This method checks if a specified quantity of drug can be added to a specified element in the model.

        Args:
        - element (str): The element to add the drug to.
        - quantity (int): The quantity of drug to add.

        Returns:
            bool: True if the drug can be added, False otherwise.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu
            - @antonoterof
        """
        model = self.getModel()

        toret = False

        if isinstance(quantity, str):
            return toret

        if (
            (quantity + model.getDrug(element)) <= model.getCapacity(element)
            and (model.getDrug(element) + quantity) >= 0
            and (not self.checkOpeneable(element) or model.getOpenStatus(element))
        ):
            toret = True

        return toret

    def checkOpeneable(self, element: str, eX: int = None, eY: int = None) -> bool:
        """
        Check if an element is openable.

        This method checks if a specified element is openable in the model.

        Args:
            - element (str): The element to check openability for.
            - eX (int, optional): The X-coordinate of the element. Defaults to None.
            - eY (int, optional): The Y-coordinate of the element. Defaults to None.

        Returns:
            bool: True if the element is openable, False otherwise.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu
        """
        model = self.getModel()
        return model.getAttributeFromDict(element, "openable")

    def areAdjacent(
        self,
        object1: str,
        object2: str,
        position1: List[int] = "",
        position2: List[int] = "",
    ) -> bool:
        """
        Check if two objects are adjacent.

        This method checks if two objects are adjacent in the model. It considers objects to be adjacent if they are at the same position, or 1 position horizontally or vertically apart.

        Args:
            - object1 (str): The first object to check adjacency for.
            - object2 (str): The second object to check adjacency for.

        Returns:
            bool: True if the objects are adjacent, False otherwise.

        Contributors:
            - @SantiagoRR2004
        """
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

        if (position1[0] >= 0 and position2[0] < 0) or (
            position1[0] < 0 and position2[0] >= 0
        ):  # Can't interact across the left and right because the matrix isn't a sphere
            toret = False

        elif (position1[1] >= 0 and position2[1] < 0) or (
            position1[1] < 0 and position2[1] >= 0
        ):  # Can't interact across the top and bottom because the matrix isn't a sphere
            toret = False

        return toret

    def transferDrugs(
        self, mover: str, giver: str, reciever: str, quantity: int
    ) -> bool:
        """
        Transfer drugs from one object to another.

        This method transfers a specified quantity of drugs from a giver object to a receiver object, if certain conditions are met.

        Args:
        - mover (str): The object that is moving the drugs.
        - giver (str): The object that is giving the drugs.
        - reciever (str): The object that is receiving the drugs.
        - quantity (int): The quantity of drugs to transfer.

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

        self.getView().updateImage()
        return toret

    def checkIfShareable(self, element: str, X: int = None, Y: int = None) -> bool:
        """
        Check if an element is shareable.

        This method checks if a specified element is shareable in the model.

        Args:
            - element (str): The element to check shareability for.
            - X (int, optional): The X-coordinate of the element. Defaults to None.
            - Y (int, optional): The Y-coordinate of the element. Defaults to None.

        Returns:
            bool: True if the element is shareable, False otherwise.

        Contributors:
            - @SantiagoRR2004
        """
        model = self.getModel()

        return model.getSemisolidStatus(element) and (
            not self.checkOpeneable(element, X, Y) or model.getOpenStatus(element, X, Y)
        )

    def checkIfMovableTo(self, x: int, y: int) -> bool:
        """
        Check if a position is movable.

        This method checks if a specified position is movable in the model.

        Args:
        - x (int): The x-coordinate of the position to check.
        - y (int): The y-coordinate of the position to check.

        Returns:
            bool: True if the position is movable, False otherwise.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof
        """
        model = self.getModel()
        char = model.getPosition(x, y)
        symbols = model.getAttribute("symbols")
        toret = False

        if char == 0:
            toret = True

        elif model.checkIfPrime(char):
            name = list(symbols.keys())[list(symbols.values()).index(char)]

            if self.checkIfShareable(name, x, y):
                toret = True

        return toret

    def moveTo(self, mover: str, moved: str, x: int, y: int) -> bool:
        """
        Move an object to a specified position.

        This method moves a specified object to a specified position in the model, if certain conditions are met.

        Args:
        - mover (str): The object that is moving.
        - moved (str): The object that is being moved.
        - x (int): The x-coordinate of the position to move to.
        - y (int): The y-coordinate of the position to move to.

        Returns:
            bool: True if the move was successful, False otherwise.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu
            - @LucachuTW
        """
        model = self.getModel()
        if (
            x < 0
            or y < 0
            or x >= len(model.getAttribute("grid"))
            or y >= len(model.getAttribute("grid")[x])
        ):
            return False

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

        self.getView().updateImage()
        return toret

    def moveOwner(self, direction: str) -> bool:
        """
        Move the owner to an adjacent position.

        Args:
            direction (str): The direction to move the owner ('up', 'down', 'left', 'right').

        Returns:
            bool: True if the movement was successful, False otherwise.

        Contributors:
            - @antonoterof
        """
        model = self.getModel()
        owner = "owner"

        if direction == "up":
            new_x, new_y = (
                model.getPositionOf(owner)[0] - 1,
                model.getPositionOf(owner)[1],
            )
        elif direction == "down":
            new_x, new_y = (
                model.getPositionOf(owner)[0] + 1,
                model.getPositionOf(owner)[1],
            )
        elif direction == "left":
            new_x, new_y = (
                model.getPositionOf(owner)[0],
                model.getPositionOf(owner)[1] - 1,
            )
        elif direction == "right":
            new_x, new_y = (
                model.getPositionOf(owner)[0],
                model.getPositionOf(owner)[1] + 1,
            )
        else:
            return False

        # Check if the owner can move to the new coordinates
        if not self.canOwnerMoveTo([new_x, new_y]):
            return False

        # Devuelve true si se puede realizar el movimiento
        return True

    def canOwnerMoveTo(self, location: List[int]) -> bool:
        """
        Check if the owner can move to the specified position

        Args:
            location (List[int]): Las coordinates [x, y] to verify.

        Returns:
            bool: True if the owner can move to the position, False otherwise.
        """
        model = self.getModel()
        owner = "owner"

        # Lógica para verificar si la ubicación está dentro de los límites el entorno
        # Falta por implementar return False

        # Lógica para verificar su en la ubicación hay una puerta
        # Abrir la puerta return True

        # Lógica para verificar si la ubicación está bloqueada por un muro
        if (
            model.getPosition(location[0], location[1])
            == model.getAttribute("symbols")["wall"]
        ):
            return False

        return True

    def changeOpenClose(
        self,
        value: bool,
        opener: str,
        element: str,
        opX: int,
        opY: int,
        eX: int,
        eY: int,
    ) -> bool:
        """
        Changes the open/close status of an element in the house environment.

        Args:
            value (bool): The new open/close status of the element.
            opener (str): The identifier of the opener element.
            element (str): The identifier of the element to be opened/closed.
            opX (int): The X coordinate of the opener element.
            opY (int): The Y coordinate of the opener element.
            eX (int): The X coordinate of the element to be opened/closed.
            eY (int): The Y coordinate of the element to be opened/closed.

        Returns:
            bool: True if the open/close status was successfully changed, False otherwise.

        Contributors:
            - @SantiagoRR2004
        """
        toret = False

        if self.checkOpeneable(element, eX, eY) and self.areAdjacent(
            opener, element, [opX, opY], [eX, eY]
        ):
            self.getModel().setOpenStatus(element, value, eX, eY)
            toret = True
            self.getView().updateImage()

        return toret

    def openSomething(
        self,
        opener: str,
        element: str = None,
        opX: int = None,
        opY: int = None,
        eX: int = None,
        eY: int = None,
    ) -> bool:
        """
        Fills all the values to be able to open something.

        Args:
            opener (str): The name of the opener.
            element (str, optional): The name of the element to be opened. Defaults to None.
            opX (int, optional): The X-coordinate of the opener. Defaults to None.
            opY (int, optional): The Y-coordinate of the opener. Defaults to None.
            eX (int, optional): The X-coordinate of the element to be opened. Defaults to None.
            eY (int, optional): The Y-coordinate of the element to be opened. Defaults to None.

        Returns:
            bool: True if the opening operation is successful, False otherwise.

        Contributors:
            - @SantiagoRR2004
        """
        model = self.getModel()
        toret = False

        if model.getAttributeFromDict(opener, "unique"):
            opX, opY = model.getPositionOf(opener)

        elif opX == None or opY == None:
            return toret

        if element == None and (eX == None or eY == None):
            return toret

        if element == None:
            numberElement = model.getPosition(eX, eY)
            for key in model.getAttribute("symbols").keys():
                if model.getAttribute("symbols")[key] == numberElement:
                    element = key

        if element == None:  # If the element is not in the model
            return toret

        if eX == None or eY == None:
            eX, eY = model.getPositionOf(element)

        return self.changeOpenClose(True, opener, element, opX, opY, eX, eY)

    def closeSomething(
        self,
        opener: str,
        element: str = None,
        opX: int = None,
        opY: int = None,
        eX: int = None,
        eY: int = None,
    ) -> bool:
        """
        Fills all the values to be able to close something.

        Args:
            opener (str): The name of the closer.
            element (str, optional): The name of the element to be closed. Defaults to None.
            opX (int, optional): The X-coordinate of the closer. Defaults to None.
            opY (int, optional): The Y-coordinate of the closer. Defaults to None.
            eX (int, optional): The X-coordinate of the element to be closed. Defaults to None.
            eY (int, optional): The Y-coordinate of the element to be closed. Defaults to None.

        Returns:
            bool: True if the closing operation is successful, False otherwise.

        Contributors:
            - @SantiagoRR2004
        """
        model = self.getModel()
        toret = False

        if model.getAttributeFromDict(opener, "unique"):
            opX, opY = model.getPositionOf(opener)

        elif opX == None or opY == None:
            return toret

        if element == None and (eX == None or eY == None):
            return toret

        if element == None:
            numberElement = model.getPosition(eX, eY)
            for key in model.getAttribute("symbols").keys():
                if model.getAttribute("symbols")[key] == numberElement:
                    element = key

        if element == None:  # If the element is not in the model
            return toret

        if eX == None or eY == None:
            eX, eY = model.getPositionOf(element)

        return self.changeOpenClose(False, opener, element, opX, opY, eX, eY)

    def consumeDrugs(
        self,
        element: str,
        quantity: int,
        eX: int = None,
        eY: int = None,
        fixes: Dict = {},
    ) -> bool:
        """
        Consume drugs from an element.

        This method consumes a specified quantity of drugs from a specified element in the model, if certain conditions are met.

        Args:
            - element (str): The element to consume the drugs from.
            - quantity (int): The quantity of drugs to consume.
            - eX (int, optional): The X-coordinate of the element. Defaults to None.
            - eY (int, optional): The Y-coordinate of the element. Defaults to None.
            - fixes (Dict, optional): A dictionary of fixes to apply. Defaults to {}.

        Returns:
            bool: True if the consumption was successful, False otherwise.

        Example of fixes:
        >>> fixes = {"pulse": 50}

        Contributors:
            - @SantiagoRR2004
        """
        model = self.getModel()
        toret = False

        if self.checkAddDrug(element, -quantity):
            for stat, correctValue in fixes.items():
                model.setAttributeFromDict(element, stat, correctValue)
            model.addDrug(element, -quantity)
            toret = True

        self.getView().updateImage()
        return toret
