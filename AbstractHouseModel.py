from abc import ABC, abstractmethod
import AbstractHouseEnv
import AbstractHouseView
from typing import Any, List


class AbstractHouseModel(ABC):
    def setRelationships(self, environment: Any, viewer: Any) -> Any:
        # @SantiagoRR2004
        controler = environment()
        view = viewer()
        view.setController(controler)
        view.setModel(self)
        controler.setView(view)
        controler.setModel(self)
        self.view = view
        self.controler = controler

    def getController(self) -> Any:
        # @SantiagoRR2004
        return self.controler

    def getView(self) -> Any:
        # @SantiagoRR2004
        return self.view

    def __repr__(self) -> str:
        # @SantiagoRR2004
        attributes = ", ".join(
            f"{key}={value!r}" for key, value in self.__dict__.items()
        )
        return f"{self.__class__.__name__}({attributes})"

    def getAttribute(self, name: str) -> Any:
        # @SantiagoRR2004
        return getattr(self, name.lower())

    def setAttribute(self, name: str, value: Any) -> None:
        # @SantiagoRR2004
        setattr(self, name.lower(), value)

    def getAttributeFromDict(self, name: str, key: Any) -> Any:
        # @SantiagoRR2004
        return self.getAttribute(name)[key]

    def setAttributeFromDict(self, name: str, key: Any, value: Any) -> None:
        # @SantiagoRR2004
        self.getAttribute(name)[key] = value

    def modifyNumericalAttributeFromDict(self, name: str, key: Any, value: int) -> None:
        # @SantiagoRR2004
        original = self.getAttributeFromDict(name,key)
        self.setAttributeFromDict(name, key, original + value)

    @staticmethod
    def calculateDistanceBetween2Points(x1: int, y1: int, x2: int, y2: int) -> float:
        # @SantiagoRR2004
        return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** (1 / 2)

    @staticmethod
    def checkIfPrime(n: int) -> bool:
        # @SantiagoRR2004
        # https://en.wikipedia.org/wiki/Primality_test
        if n <= 3:
            return n > 1
        if n % 2 == 0 or n % 3 == 0:
            return False
        limit = int(n ** (1 / 2))
        for i in range(5, limit + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    @staticmethod
    def PrimeFactorization(n: int) -> List[int]:
        i = 2
        factors = []
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)

        return factors
