from abc import ABC, abstractmethod


class AbstractHouseView(ABC):
    @abstractmethod
    def __init__(self, model) -> None:
        # @SantiagoRR2004
        self.model = model

    def setController(self, controler):
        # @SantiagoRR2004
        self.controler = controler

    def getController(self):
        # @SantiagoRR2004
        return self.controler

    def setModel(self, model):
        # @SantiagoRR2004
        self.model = model

    def getModel(self):
        # @SantiagoRR2004
        return self.model

    def __repr__(self):
        # @SantiagoRR2004
        attributes = ", ".join(
            f"{key}={value!r}" for key, value in self.__dict__.items()
        )
        return f"{self.__class__.__name__}({attributes})"
