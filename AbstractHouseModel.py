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

    def getAttribute(self, name):
        # @SantiagoRR2004
        return getattr(self, name)

    def setAttribute(self, name, value):
        # @SantiagoRR2004
        return setattr(self, name, value)

    def getAttributeFromDict(self, name, key):
        # @SantiagoRR2004
        return self.getAttribute(name)[key]

    def setAttributeFromDict(self, name, key, value):
        # @SantiagoRR2004
        self.getAttribute(name)[key] = value

    def modifyNumericalAttributeFromDict(self, name, key, value):
        # @SantiagoRR2004
        original = self.getAttribute(name)[key]
        self.setAttributeFromDict(name, key, original + value)
