from AbstractUser import AbstractUser
from typing import List, Tuple


class Courier(AbstractUser):
    requiredData = {
        "unique": {"type": bool, "default": True},
        "numberDrugs": {"type": int, "default": 127},
        "maxCapacity": {"type": int, "default": 127},
        "symbol": {"type": int, "default": 17},
        "openable": {"type": bool, "default": False},
        "semisolid": {"type": bool, "default": True},
        "moving": {
            "type": dict,
            "default": {"auto": True, "mover": False, "moved": False},
        },
        "outsidePosition": {"type": list, "default": [12, 0]},
    }

    def setup(self) -> None:
        """
        Sets up the courier's context, initializes data, and sets the position.

        Args:
            - None

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        self.data = self.getView().drawAgent(self.name)
        self.setPosition()

    def getThreads(self) -> List:
        """
        Returns a list of threads.

        Each thread represents a specific task or functionality.

        Returns:
            - List: A list of threads.

        Contributors:
            - @SantiagoRR2004
        """
        return [
            # self.changePulse,
            self.checkForDeath,
            # self.changeState,
            self.startMain,
            self.refillItself,
        ]

    def refillItself(self) -> None:
        """
        Refills itself with drugs when less that

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        refillUnit = self.data["maxCapacity"] // 2
        while self.exitNegativeFlag[0]:
            if self.data["numberDrugs"] < refillUnit:
                self.data["numberDrugs"] = self.data["maxCapacity"]

    def checkForDeath(self) -> None:
        """
        Checks if the owner's health is below 0 and
        then deletes itself.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        while self.exitNegativeFlag[0]:
            if self.getView().drawAgent("owner")["health"] <= 0:
                print(f"{self.name} has detected owner's death")
                self.__del__()

    def startMain(self) -> None:
        """
        Starts the main process.

        This method runs a loop while the exitNegativeFlag is True
        and calls the doSomething method of the context object.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        self.needToRefill = False
        self.cabinets = []
        while self.exitNegativeFlag[0]:
            self.findCabinets()
            if not self.needToRefill:
                self.goOutside()
            else:
                self.refillCabinet()

    def findCabinets(self) -> None:
        """
        Finds the cabinets in the house that need
        to be refilled.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        cabinetInfo = self.getView().drawAgent("cabinet")
        if cabinetInfo["unique"]:
            if cabinetInfo["numberDrugs"] <= 1:
                cX, cY = self.getView().findNearestPositionOfSomething(
                    "cabinet", self.x, self.y
                )
                self.cabinets.append([cX, cY])

            if cabinetInfo["numberDrugs"] == cabinetInfo["maxCapacity"]:
                self.cabinets = []

        else:  # If we add more cabinets
            pass

        if len(self.cabinets) == 0:
            self.needToRefill = False
        else:
            self.needToRefill = True

    def goOutside(self) -> None:
        """
        Makes the courier go outside.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        if [self.x, self.y] != self.data["outsidePosition"]:
            nextX, nextY = self.nextPosition(
                self.x, self.y, *self.data["outsidePosition"]
            )

            if self.getController().moveTo(self.name, self.name, nextX, nextY):
                self.getController().closeSomething(self.name, eX=self.x, eY=self.y)
                self.x = nextX
                self.y = nextY
            else:
                self.getController().openSomething(self.name, eX=nextX, eY=nextY)

    def refillCabinet(self) -> None:
        """
        Refills the cabinet.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        cX, cY = self.cabinets[0]
        nearbyPositions = self.calculateNearbyPositions(cX, cY, 1)

        if (self.x, self.y) in nearbyPositions:
            self.getController().openSomething(
                self.name, element="cabinet", opX=self.x, opY=self.y, eX=cX, eY=cY
            )
            self.getController().transferDrugs(self.name, self.name, "cabinet", 1)
            self.getController().closeSomething(
                self.name, element="cabinet", opX=self.x, opY=self.y, eX=cX, eY=cY
            )

        else:
            nextX, nextY = self.nextPosition(self.x, self.y, cX, cY)
            if self.getController().moveTo(self.name, self.name, nextX, nextY):
                self.getController().closeSomething(self.name, eX=self.x, eY=self.y)
                self.x = nextX
                self.y = nextY
            else:
                self.getController().openSomething(self.name, eX=nextX, eY=nextY)
