from typing import Any
from AbstractUser import AbstractUser


class Robot(AbstractUser):
    def setup(self):
        self.data = self.getView().drawAgent("robot")
