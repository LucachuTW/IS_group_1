from typing import Any
from AbstractUser import AbstractUser


class Owner(AbstractUser):
    def setup(self):
        self.data = self.getView().drawAgent("owner")
