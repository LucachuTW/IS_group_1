from abc import ABC, abstractmethod
from typing import Any


class AbstractHouseView(ABC):
    @abstractmethod
    def __init__(self, model: Any) -> None:
        # @SantiagoRR2004
        self.model = model

    def setController(self, controler: Any) -> None:
        # @SantiagoRR2004
        self.controler = controler

    def getController(self) -> Any:
        # @SantiagoRR2004
        return self.controler

    def setModel(self, model: Any) -> None:
        # @SantiagoRR2004
        self.model = model

    def getModel(self) -> Any:
        # @SantiagoRR2004
        return self.model

    def __repr__(self) -> str:
        # @antonvm2004
        attributes = ", ".join(
            f"{key}={value!r}" for key, value in self.__dict__.items()
        )
        return f"[{self.__class__.__name__}]: [({attributes})]"
