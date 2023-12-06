from abc import ABC, abstractmethod
from typing import Any


class AbstractHouseEnv(ABC):
    @abstractmethod
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

    def setView(self, view: Any) -> None:
        """
        Set the view for the object.

        This method allows assigning a view object to facilitate
        communication and interaction with the current object.

        Args:
        - view (Any): The view object to be set.

        Returns:
            None

        Contributors:
            - @SantiagoRR2004
        """
        self.view = view

    def getView(self) -> Any:
        """
        Get the current view associated with this object.

        Returns:
            Any: The current view.

        Note:
            This method returns the view assigned to the object.
            Ensure that the view has been properly set before calling this method.

        Contributors:
            - @SantiagoRR2004
        """
        return self.view

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
        """
        attributes = ", ".join(
            f"{key}={value!r}" for key, value in self.__dict__.items()
        )
        return f"{self.__class__.__name__}({attributes})"
