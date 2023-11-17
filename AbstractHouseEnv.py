from abc import ABC, abstractmethod


class AbstractHouseEnv(ABC):
    def __init__(self,model) -> None:
        self.model=model

    def setView(self,view):
        self.view = view
