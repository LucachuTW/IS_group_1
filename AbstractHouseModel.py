from abc import ABC, abstractmethod
import AbstractHouseEnv
import AbstractHouseView


class AbstractHouseModel(ABC):
    def setRelationships(self, environment, viewer):
        # @SantiagoRR2004
        controler = environment()
        view = viewer()
        view.setController(controler)
        view.setModel(self)
        controler.setView(view)
        controler.setModel(self)
        self.view = view
        self.controler = controler

    def getController(self):
        # @SantiagoRR2004
        return self.controler

    def getView(self):
        # @SantiagoRR2004
        return self.view

    def __repr__(self):
        # @SantiagoRR2004
        attributes = ", ".join(
            f"{key}={value!r}" for key, value in self.__dict__.items()
        )
        return f"{self.__class__.__name__}({attributes})"
