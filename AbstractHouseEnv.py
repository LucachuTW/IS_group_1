from abc import ABC, abstractmethod


class AbstractHouseEnv(ABC):
    @abstractmethod
    def __init__(self, model) -> None:
        self.model = model

    def setView(self, view):
        # @SantiagoRR2004
        self.view = view

    def getView(self):
        # @SantiagoRR2004
        return self.view

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
