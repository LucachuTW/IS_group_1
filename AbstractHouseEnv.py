from abc import ABC, abstractmethod
from typing import Any


class AbstractHouseEnv(ABC):
    @abstractmethod
    def __init__(self, model: Any) -> None:
        self.model = model

    def setView(self, view: Any) -> None:
        # @SantiagoRR2004
        self.view = view

    def getView(self) -> Any:
        # @SantiagoRR2004
        return self.view

    def setModel(self, model: Any) -> None:
        # @SantiagoRR2004
        self.model = model

    def getModel(self) -> Any:
        # @SantiagoRR2004
        return self.model

    def __repr__(self) -> str:
        # @SantiagoRR2004
        attributes = ", ".join(
            f"{key}={value!r}" for key, value in self.__dict__.items()
        )
        return f"{self.__class__.__name__}({attributes})"
