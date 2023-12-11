from abc import ABC, abstractmethod
from typing import Any


class AbstractUser(ABC):
    def __init__(self, controller: Any, viewer: Any) -> None:
        self.view = viewer
        self.controller = controller
        self.setup()

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
        return self.controller

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

    @abstractmethod
    def setup(self) -> None:
        """
        Perform setup operations for the object.

        This method is meant to be overridden by subclasses to define
        specific setup actions needed for the functionality of the object.
        It is called during the initialization phase to configure the object
        before any other operations are performed.

        Subclasses should implement this method with the necessary steps
        required for proper setup. The method signature must be preserved.

        Returns:
            None: This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        pass
