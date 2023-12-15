from typing import List
from AbstractUser import AbstractUser
import random
from Context import Context


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
        self.setContext(Context(NormalOwner))
        self.data = self.getView().drawAgent("owner")
        self.setPosition()

    def getThreads(self) -> List:
        return [self.changePulse, self.checkForDeath, self.changeState, self.startMain]

    def changePulse(self) -> None:
        while self.exitNegativeFlag:
            self.data["pulse"] += random.uniform(-0.1, 0.1)
            if self.data["pulse"] <= 20 or self.data["pulse"] >= 120:
                self.data["health"] -= 0.01

    def checkForDeath(self) -> None:
        while self.exitNegativeFlag:
            if self.data["health"] <= 100:
                self.data["health"] += 0.005
            if self.data["health"] <= 0:
                self.data["health"] = 100
                self.handleDeath()

    def changeState(self) -> None:
        while self.exitNegativeFlag:
            if self.stateOfEmergency():
                self.context.transition_to(EmergencyOwner)
            else:
                self.context.transition_to(NormalOwner)

    def startMain(self) -> None:
        while self.exitNegativeFlag:
            self.context.doSomething()

    def stateOfEmergency(self) -> bool:
        return self.data["health"] < 100
    
    def handleDeath(self) -> None:
        print("Owner has died")
        self.__del__()



class NormalOwner(Owner):
    def main(self) -> None:
        print(111111111)


class EmergencyOwner(Owner):
    def main(self) -> None:
        print(222222222)
