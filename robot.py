from typing import List
from AbstractUser import AbstractUser
from Context import Context
import random
from wrapper import Wrapper


class Robot(AbstractUser):
    requiredData = {
        "unique": {"type": bool, "default": True},
        "numberDrugs": {"type": int, "default": 0},
        "maxCapacity": {"type": int, "default": 2},
        "symbol": {"type": int, "default": 11},
        "openable": {"type": bool, "default": False},
        "semisolid": {"type": bool, "default": True},
        "moving": {
            "type": dict,
            "default": {"auto": True, "mover": True, "moved": False},
        },
    }

    def setup(self) -> None:
        """
        Sets up the robot by initializing its context, data, and position.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        self.setContext(Context(NormalRobot, self))
        self.data = self.getView().drawAgent(self.name)
        self.setPosition()

    def getThreads(self) -> List:
        """
        Returns a list of threads associated with the robot.
        Each thread represents a specific task or functionality.

        Returns:
            - List: A list of threads.

        Contributors:
            - @SantiagoRR2004
        """
        return [
            {"target": self.changeState, "name": f"{self.name} change state"},
            {"target": self.startMain, "name": f"{self.name} main"},
            {"target": self.checkForDeath, "name": f"{self.name} death"},
        ]

    def changeState(self) -> None:
        """
        Changes the state of the robot based on the current conditions.

        If the state of emergency is True, transitions the robot to the EmergencyRobot state.
        Otherwise, transitions the robot to the NormalRobot state.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        while self.exitNegativeFlag[0]:
            if self.stateOfEmergency():
                self.context.transition_to(EmergencyRobot)
            else:
                self.context.transition_to(NormalRobot)

    def stateOfEmergency(self) -> bool:
        toret = False
        if self.getView().drawAgent("owner")["health"] < 100:
            toret = True
        return toret

    def startMain(self) -> None:
        """
        Starts the main loop of the robot.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        while self.exitNegativeFlag[0]:
            self.context.doSomething()

    def checkForDeath(self) -> None:
        """
        Checks if the owner is dead and deletes the robot instance if true.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004

        Problems:
            - We need to link the owner(s) and the robot because
                sometimes it does't detect the owner's death.
                This could be solved by making the owner send a message
                but this might need ports.

        """
        while self.exitNegativeFlag[0]:
            if self.getView().drawAgent("owner")["health"] <= 0:
                print(f"{self.name} has detected owner's death")
                self.__del__()

    def fillUp(self) -> None:
        """
        Fills up the robot with drugs.
        This is on the general robot class because
        all states might need to fill up.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        objX, objY = self.getView().findNearestPositionOfSomething(
            "cabinet", self.x, self.y
        )

        nearbyPositions = self.calculateNearbyPositions(self.x, self.y, 1)

        if (objX, objY) in nearbyPositions:
            self.getController().openSomething(
                self.name, element="cabinet", opX=self.x, opY=self.y, eX=objX, eY=objY
            )
            if not self.getController().transferDrugs(
                self.name, "cabinet", self.name, 1
            ):
                print(f"Problem, {self.name} could not fill up")
            self.getController().closeSomething(
                self.name, element="cabinet", opX=self.x, opY=self.y, eX=objX, eY=objY
            )

        else:
            nextX, nextY = self.nextPosition(self.x, self.y, objX, objY)
            if self.getController().moveTo(self.name, self.name, nextX, nextY):
                self.x = nextX
                self.y = nextY
            else:
                self.getController().openSomething(self.name, eX=nextX, eY=nextY)


class NormalRobot(Wrapper, Robot):
    def main(self) -> None:
        """
        The main loop of the normal robot.
        It makes sure the robot is always full of drugs and
        then moves close to the owner.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        if self.data["numberDrugs"] < self.data["maxCapacity"]:
            self.fillUp()
        else:
            self.stayClose()

    def stayClose(self) -> None:
        ownerX, ownerY = self.getView().findNearestPositionOfSomething(
            "owner", self.x, self.y
        )

        nearbyPositions = self.calculateNearbyPositions(self.x, self.y, 3)

        if (ownerX, ownerY) not in nearbyPositions:
            nextX, nextY = self.nextPosition(self.x, self.y, ownerX, ownerY)
            if self.getController().moveTo(self.name, self.name, nextX, nextY):
                self.x = nextX
                self.y = nextY
            else:
                self.getController().openSomething(self.name, eX=nextX, eY=nextY)


class EmergencyRobot(Wrapper, Robot):
    def main(self) -> None:
        """
        The main loop of the emergency robot.
        To fix the owner iut needs to have medicine.
        So if it doesn't have any it will fill up.
        Then it will go to the owner and give him the medicine.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """

        if self.data["numberDrugs"] == 0:
            self.fillUp()
        else:
            self.moveToOwner()

    def moveToOwner(self) -> None:
        """
        Moves the robot to help the owner.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu
        """
        ownerX, ownerY = self.getView().findNearestPositionOfSomething(
            "owner", self.x, self.y
        )

        nearbyPositions = self.calculateNearbyPositions(self.x, self.y, 1)

        if ownerX is not None and ownerY is not None:
            if (ownerX, ownerY) in nearbyPositions:
                self.giveDrugs()
            else:
                nextX, nextY = self.nextPosition(self.x, self.y, ownerX, ownerY)
                if self.getController().moveTo(self.name, self.name, nextX, nextY):
                    self.x = nextX
                    self.y = nextY
                else:
                    self.getController().openSomething(self.name, eX=nextX, eY=nextY)

    def giveDrugs(self) -> None:
        """
        Gives medicine to the owner.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @Ventupentu
        """
        self.getController().transferDrugs(self.name, self.name, "owner", 1)
