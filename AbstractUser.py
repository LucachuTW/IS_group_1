from abc import ABC, abstractmethod
from typing import Any, List
import threading
from Context import Context


class AbstractUser(ABC):
    requiredData = {}
    exitNegativeFlag = True

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

    @property
    def getContext(self) -> Context:
        return self.context

    def setContext(self, context: Context) -> None:
        self.context = context

    def setPosition(self) -> None:
        """
        Finds the position of symbol on the grid and
        adds it as self.x and self.y

        Returns:
            None: This method does not return any value.

        Problems:
            - No way to check if the number is not prime
            if the symbol is hidden there. This is because
            prime calculations are in the model and the users
            have no direct access to the model.
            - This code is very similar to getPositionOf in houseModel.py,
            the same function could be used. This could be made if the View is added
            some functions that transfer the results of methods from the Model. This
            would also solve the not prime problem.
            - No solutions if the coordinates are not found
            Maybe add default positions that are added by the controller?
            Problem -> Controller should not have this power?

        Contributors:
            - @SantiagoRR2004
        """

        grid = self.getView().draw()
        symbol = self.data["symbol"]
        found = False
        rowNumber = 0

        while not found and rowNumber <= len(grid) - 1:
            columnNumber = 0
            while not found and columnNumber <= len(grid[rowNumber]) - 1:
                if grid[rowNumber][columnNumber] == symbol:
                    self.x = rowNumber
                    self.y = columnNumber
                    found = True
                columnNumber += 1
            rowNumber += 1

        if not found:
            raise Exception("Couldn't find coordinates")

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

        keys = list(self.data.keys()).copy()

        for key in keys:
            if key not in self.requiredData:
                del self.data[key]

    def setUpThreading(self) -> None:
        threads = self.getThreads()
        self.threads = []
        for th in threads:
            self.threads.append(threading.Thread(target=th))
            self.threads[-1].start()

    def deleteThreads(self) -> None:
        self.exitNegativeFlag = False
        for th in self.threads:
            if th != threading.current_thread():
                th.join()

    def getThreads(self) -> List:
        """
        BLA BLA BLA BLA

        Contributors:
            - @SantiagoRR2004
        """
        return []

    def __del__(self) -> None:
        self.deleteThreads()
