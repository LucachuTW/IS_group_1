from abc import ABC, abstractmethod
import AbstractHouseEnv
import AbstractHouseView


class AbstractHouseModel(ABC):
    def setRelationships(self):
        controler = AbstractHouseEnv.AbstractHouseEnv(self)
        view = AbstractHouseView.AbstractHouseView(self)
        view.setController(controler)
        controler.setView(view)
        self.view = view
        self.controler = controler
