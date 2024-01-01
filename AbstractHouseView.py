from abc import ABC, abstractmethod
from typing import Any


class AbstractHouseView(ABC):
    def __init__(self, model: Any) -> None:
        """
        Initialize the instance with the provided model.

        Args:
        - model (Any): The model to be associated with the instance.

        Returns:
            None

        Contributors:
            - @SantiagoRR2004
        """
        self.model = model

    def setController(self, controler: Any) -> None:
        """
        Set the controller for the object.

        This method allows assigning a controller object to facilitate
        communication and interaction with the current object.

        Args:
        - controller (Any): The controller object to be set.

        Returns:
            None

        Contributors:
        - @SantiagoRR2004
        """
        self.controler = controler

    def getController(self) -> Any:
        """
        Retrieve the controller associated with the current instance.

        Returns:
            Any: The controller object.

        Note:
            This method provides access to the controller assigned to the instance.
            Ensure that the controller has been properly set before calling this method.

        Contributors:
            - @SantiagoRR2004
        """
        return self.controler

    def setModel(self, model: Any) -> None:
        """
        Set the model for the object.

        This method allows assigning a model object to facilitate
        communication and interaction with the current object.

        Args:
        - model (Any): The model object to be set.

        Returns:
            None

        Contributors:
            - @SantiagoRR2004
        """
        self.model = model

    def getModel(self) -> Any:
        """
        Retrieve the model associated with the current instance.

        Returns:
            Any: The model object.

        Note:
            This method provides access to the model assigned to the instance.
            Ensure that the model has been properly set before calling this method.

        Contributors:
            - @SantiagoRR2004
        """
        return self.model

    def __repr__(self) -> str:
        """
        Return a string representation of the object suitable for debugging.

        Returns:
            str: A string representation of the object.

        Contributors:
            - @SantiagoRR2004
            - @antonvm2004
        """
        attributes = ", ".join(
            f"{key}={value!r}" for key, value in self.__dict__.items()
        )
        return f"[{self.__class__.__name__}]: [({attributes})]"
