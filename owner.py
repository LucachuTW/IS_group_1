from typing import List
from AbstractUser import AbstractUser
import random


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

    def setup(self):
        self.data = self.getView().drawAgent("owner")

    def getThreads(self) -> List:
        return [self.changePulse, self.checkForDeath]

    def changePulse(self):
        while self.exitNegativeFlag:
            self.data["pulse"] += random.uniform(-0.1, 0.1)
            if self.data["pulse"] <= 20 or self.data["pulse"] >= 100:
                self.data["health"] -= 0.01

    def checkForDeath(self):
        while self.exitNegativeFlag:
            if self.data["health"] <= 100:
                self.data["health"] += 0.005
            if self.data["health"] <= 0:
                self.data["health"] = 100
                print("Owner has died")
                self.__del__()
