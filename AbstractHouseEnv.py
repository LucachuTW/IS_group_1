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
