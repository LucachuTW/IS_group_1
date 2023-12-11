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
    }

    def setup(self):
        self.data = self.getView().drawAgent("owner")

    def getThreads(self) -> List:
        return [self.changePulse()]

    def changePulse(self):
        for i in range(1000):
            self.data["pulse"] += random.uniform(-0.1, 0.1)
            print(self.data["pulse"])
