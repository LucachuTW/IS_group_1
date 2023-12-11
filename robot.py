from typing import List
from AbstractUser import AbstractUser


class Robot(AbstractUser):
    def setup(self):
        self.data = self.getView().drawAgent("robot")

    def getThreads(self) -> List:
        return []
