import json
import AbstractHouseModel
import houseEnv
import houseView
import atexit
from typing import List

class HouseModel(AbstractHouseModel.AbstractHouseModel):
    def __init__(self):
        """
        Initializes the HouseModel class.

        Args:
        - None

        Returns:
        - None

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu
        """
        self.setRelationships(houseEnv.HouseEnv, houseView.HouseView)


        with open("environment.json", "r") as file:
            data = json.load(file)

        self.grid = [[int(x) for x in row] for row in data["grid"]]
        self.symbols = data["symbols"]
        self.setAttribute("notElements", data["notElements"])

        for key, value in data.items():
            if key not in data["notElements"]:
                self.setAttribute(key, value)

        atexit.register(self.saveToFile)

    def addDrug(self, object, quantity):
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

    def getDrug(self, object):
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

    def getOpenStatus(self, object):
        """
        Gets the open status of the object.

        Args:
        - object: The object to get the open status from.

        Returns:
        - The open status of the object.

        Contributors:
            - @Ventupentu
            - @SantiagoRR2004
            - @LucachuTW
        """
        return self.getAttributeFromDict(object, "open")

    def setOpenStatus(self, object, status):
        """
        Sets the open status of the object.

        Args:
        - object: The object to set the open status to.
        - status: The status to set the object to.

        Returns:
        - None

        Contributors:
            - @Ventupentu
            - @SantiagoRR2004
            - @LucachuTW
        """
        self.setAttributeFromDict(object, "open", status)

    def getCapacity(self, object):
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

    def changePosition(self, originX, originY, destinationX, destinationY):
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

    def getPosition(self, x, y):
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

    def setPosition(self, x, y, value):
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

    def removeValue(self, value):
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

    def getPositionOf(self, value):
        """
        Get the position of the specified value in the grid.

        Args:
            value: The value to find the position of.

        Returns:
            The position of the value in the grid.

        Contributors:
            - @antonoterof
        """
        simbolValue = self.getAttributeFromDict(value, "symbol")
        position = False
        found = False
        for file in range(len(self.getAttribute("grid"))):
            for simbol in range(len(self.getAttributeFromDict("grid", file))):
                if self.getAttributeFromDict("grid", file)[simbol] == simbolValue:
                    position = [file, simbol]
                    found = True
                    break
                elif not self.checkIfPrime(
                    self.getAttributeFromDict("grid", file)[simbol]
                ):
                    if simbolValue in self.PrimeFactorization(
                        self.getAttributeFromDict("grid", file)[simbol]
                    ):
                        position = [file, simbol]
                        found = True
                        break
            if found == True:
                break
        return position

    def getOpenableStatus(self, object):
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

    def getSemisolidStatus(self, object):
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
        
    def saveToFile(self):
        """
        Save the current state of the HouseModel to a file.

        Args:
            None

        Returns:
            None

        """
        extraItems = ["grid","symbols", "notElements"]
        saveData = {}

        for item in extraItems:
            saveData[item] = self.getAttribute(item)

        for element in self.getAttribute("symbols").keys():
            saveData[element] = self.getAttribute(element)

        with open("environment.json", "w") as file:
            json.dump(saveData, file)

    def getDoorStatus(self, doorLocation):
        """
        Get the status of the door.

        Args:
            doorLocation: The location of the door.

        Returns:
            The status of the door.

        Contributors:
            - @antonoterof
        """
        for door in self.getAttributeFromDict("doors", "subset"):
            if door["location"] == doorLocation:
                return door["open"]
            
    def openDoor(self, doorLocation):
        """
        Open a door at the specified location.

        Args:
            doorLocation (List[int]): The [x, y] coordinates of the door.
        
        Contributors:
        - @antonoterof
        """
        for door in self.getAttributeFromDict("doors", "subset"):
            if door["location"] == doorLocation:
                if self.getDoorStatus(doorLocation) == False:
                    door["open"] = True
                break

    def closeDoor(self, doorLocation):
        """
        Close a door at the specified location.

        Args:
            doorLocation (List[int]): The [x, y] coordinates of the door.

        Contributors:
        - @antonoterof
        """
        for door in self.getAttributeFromDict("doors", "subset"):
            if door["location"] == doorLocation:
                if self.getDoorStatus(doorLocation) == True:
                    door["open"] = False
                break

        




