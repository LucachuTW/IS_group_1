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
        self.data = self.getView().drawAgent("robot")
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
        return [self.changeState, self.startMain, self.checkForDeath]

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
        while self.exitNegativeFlag:
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
        while self.exitNegativeFlag:
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
        while self.exitNegativeFlag:
            if self.getView().drawAgent("owner")["health"] <= 0:
                print("Robot has detected owner's death")
                self.__del__()


class NormalRobot(Wrapper, Robot):
    def main(self) -> None:
        if self.data["numberDrugs"] < self.data["maxCapacity"]:
            self.fillUp()

    def fillUp(self) -> None:
        """
        Fills up the robot with drugs.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        objX, objY = self.getView().findNearestPositionOfSomething(
            "cabinet", self.x, self.y
        )

        nearbyPositions = [
            [self.x, self.y],
            [self.x, self.y + 1],
            [self.x, self.y - 1],
            [self.x + 1, self.y],
            [self.x - 1, self.y],
        ]

        if [objX, objY] in nearbyPositions:
            self.getController().openSomething(
                "robot", element="cabinet", opX=self.x, opY=self.y, eX=objX, eY=objY
            )
            while self.getController().transferDrugs("robot", "cabinet", "robot", 1):
                pass
            self.getController().closeSomething(
                "robot", element="cabinet", opX=self.x, opY=self.y, eX=objX, eY=objY
            )

        else:
            nextX, nextY = self.nextPosition(self.x, self.y, objX, objY)
            if self.getController().moveTo("robot", "robot", nextX, nextY):
                self.x = nextX
                self.y = nextY
            else:
                self.getController().openSomething("robot", eX=nextX, eY=nextY)


class EmergencyRobot(Wrapper, Robot):
    def main(self) -> None:
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

        nearbyPositions = [
            [self.x, self.y],
            [self.x, self.y + 1],
            [self.x, self.y - 1],
            [self.x + 1, self.y],
            [self.x - 1, self.y],
        ]

        if ownerX is not None and ownerY is not None:
            if [ownerX, ownerY] in nearbyPositions:
                self.giveDrugs()
            else:
                nextX, nextY = self.nextPosition(self.x, self.y, ownerX, ownerY)
                if self.getController().moveTo("robot", "robot", nextX, nextY):
                    self.x = nextX
                    self.y = nextY
                else:
                    self.getController().openSomething("robot", eX=nextX, eY=nextY)

    def giveDrugs(self) -> None:
        """
        Gives medicine to the owner.

        Returns:
            - None. This method does not return any value.

        Contributors:
            - @Ventupentu
        """
<<<<<<< HEAD
    
        if self.data["numberDrugs"] > 0:
            self.getController().transferDrugs("robot", "robot", "owner", 1)
            self.data["numberDrugs"] -= 1
        else:
            self.getController().transferDrugs("robot", "robot", "owner", 0)
    
=======
        self.getController().transferDrugs("robot", "robot", "owner", 1)
>>>>>>> ba725b714ec81651fb27bbbe9022e64ccee7b1e0
