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
            if self.stateOfEmergency:
                self.context.transition_to(EmergencyRobot)
            else:
                self.context.transition_to(NormalRobot)

    def stateOfEmergency(self) -> bool:
        toret = random.choice([True, False])
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
                self.__del__()


class NormalRobot(Wrapper, Robot):
    def main(self) -> None:
        pass


class EmergencyRobot(Wrapper, Robot):
    def main(self) -> None:
        pass
