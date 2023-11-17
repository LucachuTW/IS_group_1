from abc import ABC, abstractmethod


class AbstractHouseView(ABC):
    def __init__(self,model) -> None:
        self.model=model

    def setController(self,controler):
        self.controler = controler
