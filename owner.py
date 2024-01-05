from typing import Any, List, Tuple
from AbstractUser import AbstractUser
import random
from Context import Context
from wrapper import Wrapper


class Owner(AbstractUser):
    requiredData = {
        "unique": {"type": bool, "default": True},
        "numberDrugs": {"type": int, "default": 0},
        "maxCapacity": {"type": int, "default": 1},
        "symbol": {"type": int, "default": 7},
        "openable": {"type": bool, "default": False},
        "semisolid": {"type": bool, "default": True},
        "moving": {
            "type": dict,
            "default": {"auto": True, "mover": True, "moved": True},
        },
        "pulse": {"type": float, "default": 50},
        "health": {"type": float, "default": 100},
    }

    def setup(self) -> None:
        """
        Sets up the owner's context, initializes data, and sets the position.

        Args:
            - None

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        self.setContext(Context(NormalOwner, self))
        self.data = self.getView().drawAgent("owner")
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
            self.changePulse,
            self.checkForDeath,
            self.startMain,
            self.changeState,
        ]

    def changePulse(self) -> None:
        """
        Randomly changes the pulse value within a certain range and updates the health value accordingly.

        The pulse value is modified by adding a random number between -0.1 and 0.1.
        If the resulting pulse value is less than or equal to 20 or greater than or equal to 120,
        the health value is decreased by 0.01.

        Returns:
            None

        Contributors:
            - @SantiagoRR2004
        """
        while self.exitNegativeFlag:
            self.data["pulse"] += random.uniform(-0.1, 0.1)
            if self.data["pulse"] <= 20 or self.data["pulse"] >= 120:
                self.data["health"] -= 0.01

    def checkForDeath(self) -> None:
        """
        Checks if the owner's health is below 0 and handles the death scenario.

        If the owner's health is below or equal to 0, the health is reset to 100
        and a message is printed indicating that the owner has died. The __del__
        method is then called to perform any necessary cleanup.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        while self.exitNegativeFlag:
            if self.data["health"] <= 100:
                self.data["health"] += 0.005
            if self.data["health"] <= 0:
                self.data["health"] = 100
                print("Owner has died")
                self.__del__()

    def changeState(self) -> None:
        """
        Changes the state of the owner based on the current conditions.

        If there is a state of emergency, transitions the context to EmergencyOwner.
        Otherwise, transitions the context to NormalOwner.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        while self.exitNegativeFlag:
            if self.stateOfEmergency():
                self.context.transition_to(EmergencyOwner)
            else:
                self.context.transition_to(NormalOwner)

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
        while self.exitNegativeFlag:
            self.context.doSomething()

    def stateOfEmergency(self) -> bool:
        """
        Checks if the owner is in a state of emergency based on their health.

        Returns:
            - bool: True if the owner's health is less than 100, False otherwise.

        Contributors:
            - @SantiagoRR2004
        """
        toret = False
        if self.data["health"] < 100:
            toret = True
        return toret


class NormalOwner(Wrapper, Owner):
    def main(self) -> None:
        """
        The main process for the owner.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        randomNumber = random.random()

        if randomNumber < 0.9:
            self.moveRandomly()
        elif randomNumber > 0.9:
            self.moveRandomlyNearby()

    def moveRandomlyNearby(self) -> None:
        """
        Moves the owner randomly to a nearby location.

        This method selects a random direction from the available options
        (up, down, left, or right) and attempts to move the owner to the
        adjacent cell in that direction. If the move is successful, the
        owner's coordinates are updated accordingly.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        direction = random.choice([[0, 1], [0, -1], [1, 0], [-1, 0]])
        if self.getController().moveTo(
            "owner", "owner", self.x + direction[0], self.y + direction[1]
        ):
            self.x += direction[0]
            self.y += direction[1]

    def moveRandomly(self) -> None:
        """
        Moves the owner randomly to any location.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        objectiveX, objectiveY = self.choosePosition()
        if self.x == objectiveX and self.y == objectiveY:
            self.hasObjective = False

        else:
            nextX, nextY = self.nextPosition(self.x, self.y, objectiveX, objectiveY)
            if self.getController().moveTo("owner", "owner", nextX, nextY):
                self.x = nextX
                self.y = nextY
            else:  # We try to open what is in front of the owner
                pass

    def choosePosition(self) -> Tuple[int, int]:
        """
        Chooses a random position for the owner.

        Returns:
            - Tuple[int, int]: A tuple containing the x and y coordinates of the position.

        Contributors:
            - @SantiagoRR2004
        """
        if not hasattr(self, "hasObjective"):
            self.hasObjective = False

        while not self.hasObjective:
            grid = self.getView().drawMovableTo()
            row = random.randint(0, len(grid) - 1)
            column = random.randint(0, len(grid[row]) - 1)

            if grid[row][column] == 0:
                self.hasObjective = True
                self.objX = row
                self.objY = column

        return self.objX, self.objY


class EmergencyOwner(Wrapper, Owner):
    def main(self) -> None:
        pass
