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
        self.setContext(Context(NormalRobot, self))
        self.data = self.getView().drawAgent("robot")
        self.setPosition()

    def getThreads(self) -> List:
        return [self.changeState, self.startMain, self.checkForDeath]

    def changeState(self) -> None:
        while self.exitNegativeFlag:
            if self.stateOfEmergency:
                self.context.transition_to(EmergencyRobot)
            else:
                self.context.transition_to(NormalRobot)

    def stateOfEmergency(self) -> bool:
        toret = random.choice([True, False])
        return toret

    def startMain(self) -> None:
        while self.exitNegativeFlag:
            self.context.doSomething()

    def checkForDeath(self) -> None:
        while self.exitNegativeFlag:
            # Need to improve this
            # We might need to link a robot and his owner(s)
            # Or make the owner send a message but this might need ports
            if self.getView().drawAgent("owner")["health"] <= 0:
                self.__del__()


class NormalRobot(Wrapper, Robot):
    def main(self) -> None:
        pass


class EmergencyRobot(Wrapper, Robot):
    def main(self) -> None:
        pass
