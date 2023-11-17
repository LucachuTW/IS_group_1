from abc import ABC, abstractmethod
import AbstractHouseEnv
import AbstractHouseView


class AbstractHouseModel(ABC):
    def __init__(self) -> None:
        a = AbstractHouseEnv.AbstractHouseEnv(self)
        b = AbstractHouseView.AbstractHouseView(self)
        b.setController(a)
        a.setView(b)
        self.view = b
        self.controler = a
