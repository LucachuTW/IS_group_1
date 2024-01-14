import json
import AbstractHouseModel
import atexit
import warnings
from typing import List


class HouseModel(AbstractHouseModel.AbstractHouseModel):
    def __init__(self, file: str = "environment.json") -> None:
        """
        Initializes the HouseModel class.

        Args:
        - file: It extracts the house from this file

        Returns:
        - None

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu
        """
        self.saveModelParameters(file)

        atexit.register(self.saveToFile)

    def saveModelParameters(self, file: str) -> None:
        """
        Writes house data as parameters.

        Args:
        - file: It extracts the house data from this file

        Returns:
        - None

        Contributors:
            - @SantiagoRR2004
        """
        with open(file, "r") as file:
            data = json.load(file)

        self.grid = [[int(x) for x in row] for row in data["grid"]]
        self.symbols = data["symbols"]
        self.setAttribute("notElements", data["notElements"])

        for key, value in data.items():
            if key not in data["notElements"]:
                self.setAttribute(key, value)

    def addDrug(self, object: str, quantity: int) -> None:
        """
        Adds a drug to the object.

        Args:
        - object: The object to add the drug to.
        - quantity: The quantity of drugs to add.

        Returns:
        - None

        Contributors:
            - @Ventupentu
            - @SantiagoRR2004
        """
        self.modifyNumericalAttributeFromDict(object, "numberDrugs", quantity)

    def getDrug(self, object: str) -> int:
        """
        Gets the drug from the object.

        Args:
        - object: The object to get the drug from.

        Returns:
        - The drug from the object.

        Contributors:
            - @Ventupentu
            - @SantiagoRR2004
        """
        return self.getAttributeFromDict(object, "numberDrugs")

    def getOpenStatus(self, object: str, x: int = None, y: int = None) -> bool:
        """
        Gets the open status of the object.

        Args:
            - object: The object to get the open status from.
            - x (optional): The x coordinate of the object.
            - y (optional): The y coordinate of the object.

        Returns:
            - The open status of the object.

        Contributors:
            - @Ventupentu
            - @SantiagoRR2004
            - @LucachuTW
        """
        toret = False
        if self.getAttributeFromDict(object, "unique"):
            toret = self.getAttributeFromDict(object, "open")

        elif "open" in self.getAttribute(object):
            toret = self.getAttributeFromDict(object, "open")

        else:
            for individual in self.getAttributeFromDict(object, "subset"):
                if individual["location"] == [x, y]:
                    toret = individual["open"]

        return toret

    def setOpenStatus(
        self, object: str, status: bool, x: int = None, y: int = None
    ) -> None:
        """
        Sets the open status of the object.

        Args:
            - object: The object to set the open status to.
            - status: The status to set the object to.
            - x (optional): The x coordinate of the object.
            - y (optional): The y coordinate of the object.

        Returns:
            - None

        Contributors:
            - @Ventupentu
            - @SantiagoRR2004
            - @LucachuTW
        """
        if self.getAttributeFromDict(object, "unique"):
            self.setAttributeFromDict(object, "open", status)

        elif "open" in self.getAttribute(object):
            self.setAttributeFromDict(object, "open", status)

        else:
            for individual in self.getAttributeFromDict(object, "subset"):
                if individual["location"] == [x, y]:
                    individual["open"] = status

    def getCapacity(self, object: str) -> int:
        """
        Gets the capacity of the object.

        Args:
        - object: The object to get the capacity from.

        Returns:
        - The capacity of the object.

        Contributors:
            - @Ventupentu
            - @SantiagoRR2004
        """
        return self.getAttributeFromDict(object, "maxCapacity")

    def changePosition(
        self, originX: int, originY: int, destinationX: int, destinationY: int
    ) -> None:
        """
        Changes the position of the object.

        Args:
        - originX: The x coordinate of the origin.
        - originY: The y coordinate of the origin.
        - destinationX: The x coordinate of the destination.
        - destinationY: The y coordinate of the destination.

        Returns:
        - None

        Contributors:
            - @SantiagoRR2004
            - @antonvm2004
        """
        value = self.getPosition(originX, originY)
        self.setPosition(originX, originY, "0")
        self.setPosition(destinationX, destinationY, value)

    def getPosition(self, x: int, y: int) -> int:
        """
        Get the position at coordinates (x, y) in the grid.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.

        Returns:
            The value at the specified position in the grid.

        Contributors:
            - @antonvm2004
        """
        return self.grid[x][y]

    def setPosition(self, x: int, y: int, value: int) -> None:
        """
        Set the position at coordinates (x, y) in the grid.

        Args:
            x (int): The x-coordinate.
            y (int): The y-coordinate.
            value: The value to set at the specified position.

        Returns:
            None

        Contributors:
            - @antonvm2004
        """
        self.grid[x][y] = value

    def removeValue(self, value: str) -> None:
        """
        Remove the specified value from the grid.

        Args:
            value: The value to remove.

        Returns:
            None

        Contributors:
            - @antonoterof
        """
        simbolValue = self.getAttributeFromDict(value, "symbol")
        for file in range(len(self.getAttribute("grid"))):
            for simbol in range(len(self.getAttributeFromDict("grid", file))):
                if self.getAttributeFromDict("grid", file)[simbol] == simbolValue:
                    index = self.getAttributeFromDict("grid", file).index(simbolValue)
                    self.getAttributeFromDict("grid", file)[index] = 0
                    break

    def getPositionOf(self, value: str):
        """
        Get the position of the specified value in the grid.
        We only check if the value is in the prime factorization of the number.
        If there are multiples of the same value,
        we return the first one we find.

        Args:
            value: The value to find the position of.

        Returns:
            The position of the value in the grid.

        Contributors:
            - @antonoterof
            - @SantiagoRR2004
        """
        simbolValue = self.getAttributeFromDict(value, "symbol")
        position = False
        found = False
        grid = self.getAttribute("grid")
        rowNum = 0

        while rowNum < len(grid) and not found:
            colNum = 0

            while colNum < len(grid[rowNum]) and not found:
                if simbolValue in self.PrimeFactorization(grid[rowNum][colNum]):
                    position = [rowNum, colNum]
                    found = True
                colNum += 1

            rowNum += 1

        if not found:
            warnings.warn(
                f"The value {simbolValue} from {value} could no be found in the grid."
            )
            # We set the default just in case
            position = [0, 0]

        return position

    def getOpenableStatus(self, object: str):
        """
        Get the openable status of the object.

        Args:
            object: The object to get the openable status from.

        Returns:
            The openable status of the object.

        Contributors:
            - @antonoterof
        """
        return self.getAttributeFromDict(object, "openable")

    def getSemisolidStatus(self, object: str):
        """
        Get the semisolid status of the object.

        Args:
            object: The object to get the semisolid status from.

        Returns:
            The semisolid status of the object.

        Contributors:
            - @antonoterof
        """
        return self.getAttributeFromDict(object, "semisolid")

    def saveToFile(self) -> None:
        """
        Save the current state of the HouseModel to a file.
        We always save to "environment.json"

        Args:
            None

        Returns:
            None

        Contributors:
            - @SantiagoRR2004
        """
        extraItems = ["grid", "symbols", "notElements"]
        saveData = {}

        for item in extraItems:
            saveData[item] = self.getAttribute(item)

        for element in self.getAttribute("symbols").keys():
            saveData[element] = self.getAttribute(element)

        with open("environment.json", "w") as file:
            json.dump(saveData, file)

    def getDoorStatus(self, doorLocation: List[int]) -> bool:
        """
        Get the status of the door.

        Args:
            doorLocation: The location of the door.

        Returns:
            The status of the door.

        Contributors:
            - @antonoterof
        """
        for door in self.getAttributeFromDict("door", "subset"):
            if door["location"] == doorLocation:
                return door["open"]

    def openDoor(self, doorLocation: List[int]) -> None:
        """
        Open a door at the specified location.

        Args:
            doorLocation (List[int]): The [x, y] coordinates of the door.

        Contributors:
            - @antonoterof
        """
        for door in self.getAttributeFromDict("door", "subset"):
            if door["location"] == doorLocation:
                if self.getDoorStatus(doorLocation) == False:
                    door["open"] = True
                break

    def closeDoor(self, doorLocation: List[int]) -> None:
        """
        Close a door at the specified location.

        Args:
            doorLocation (List[int]): The [x, y] coordinates of the door.

        Contributors:
            - @antonoterof
        """
        for door in self.getAttributeFromDict("door", "subset"):
            if door["location"] == doorLocation:
                if self.getDoorStatus(doorLocation) == True:
                    door["open"] = False
                break
