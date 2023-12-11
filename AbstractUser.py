from abc import ABC, abstractmethod
from typing import Any, List
import threading


class AbstractUser(ABC):
    requiredData = {}

    def __init__(self, controller: Any, viewer: Any) -> None:
        self.view = viewer
        self.controller = controller
        self.setup()
        self.checkData()
        self.setUpThreading()

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

    def checkData(self) -> None:
        """
        Check if the self.data is correct according to self.requiredData

        We establish the correct values in the dict data if needed and remove all unnecesary ones

        Need to have dicts of data and requiredData already created

        Returns:
            None: This method does not return any value.

        Contributors:
            - @SantiagoRR2004

        Things to add:
            Check that the values inside of a dict are correct
            Check intervals in ints
            Check uniqueness
            Check position
        """
        for key, value in self.requiredData.items():
            if key not in self.data:
                self.data[key] = value["default"]

            else:
                if not isinstance(type(self.data[key]), value["type"]):
                    self.data[key] = value["default"]

        self.data = {
            key: value for key, value in self.data.items() if key in self.requiredData
        }

    def setUpThreading(self) -> None:
        threads = self.getThreads()
        for th in threads:
            threading.Thread(target=th).start()

    @abstractmethod
    def getThreads(self) -> List:
        """
        BLA BLA BLA BLA

        Contributors:
            - @SantiagoRR2004
        """
        pass
