from abc import ABC, abstractmethod
from typing import Any, List, Tuple
import threading
from Context import Context


class AbstractUser(ABC):
    requiredData = {}
    exitNegativeFlag = [True]

    def __init__(self, controller: Any, viewer: Any, name: str) -> None:
        """
        Initializes an instance of the AbstractUser class.
        It needs a controller and a viewer to work.
        The name is the name in the environment.

        Args:
            - controller (Any): The controller object.
            - viewer (Any): The viewer object.
            - name (str): The name in the environment.

        Contributors:
            - @SantiagoRR2004
        """
        self.view = viewer
        self.controller = controller
        self.name = name
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
        """
        Returns the context associated with the user.

        Returns:
            Context: The context associated with the user.

        Contributors:
            - @SantiagoRR2004
        """
        return self.context

    def setContext(self, context: Context) -> None:
        """
        Sets the context for the user.

        Parameters:
            context (Context): The context to set.

        Returns:
            None

        Contributors:
            - @SantiagoRR2004
        """
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
            print(f"Trying to find {symbol} in:")
            for row in grid:
                print(row)
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
                if not isinstance(self.data[key], value["type"]):
                    self.data[key] = value["default"]

        keys = list(self.data.keys()).copy()

        for key in keys:
            if key not in self.requiredData:
                del self.data[key]

    def setUpThreading(self) -> None:
        """
        Set up and start the threads for the user.

        Returns:
            None: This method does not return any value.

        Contributors:
            - @SantiagoRR2004
        """
        threads = self.getThreads()
        self.threads = []
        # threading.stack_size(1024 * 1024 * 1024)
        for th in threads:
            self.threads.append(threading.Thread(target=th))
            self.threads[-1].start()

    def deleteThreads(self) -> None:
        """
        Deletes all threads except the current thread.

        This method sets the `exitNegativeFlag` to False and joins all threads
        in the `threads` list, except the current thread.

        Returns:
            None
        """
        self.exitNegativeFlag[0] = False
        for th in self.threads:
            if th != threading.current_thread():
                th.join()

    def getThreads(self) -> List:
        """
        Returns the threads for the user.
        Needs to be implemented by the subclass.

        Returns:
            List: The threads for the user.

        Contributors:
            - @SantiagoRR2004
        """
        return []

    def __del__(self) -> None:
        """
        Deletes the threads for the user.

        Returns:
            None: This method does not return any value.

        Contributors:
            - @SantiagoRR2004

        Note:
            This method is called when the object is deleted.
            It is used to delete the threads associated with the user.
        """
        self.deleteThreads()

    def nextPosition(
        self, originX: int, originY: int, desX: int, desY: int
    ) -> Tuple[int, int]:
        """
        Calculates the next position for the user to move to using the A* algorithm.

        Args:
            originX (int): The x-coordinate of the current position.
            originY (int): The y-coordinate of the current position.
            desX (int): The x-coordinate of the destination position.
            desY (int): The y-coordinate of the destination position.

        Returns:
            Tuple[int, int]: The next position as a tuple of (x, y) coordinates.

        Contributors:
            - @SantiagoRR2004
        """
        binaryGrid = self.getView().drawMovableTo()
        binaryGrid[desX][desY] = 0
        next = self.aStar(binaryGrid, originX, originY, desX, desY)
        # The first in the list is the node of origin
        return next[1]

    @staticmethod
    def aStar(
        graph: List[List[int]], originX: int, originY: int, desX: int, desY: int
    ) -> List[Tuple[int, int]]:
        """
        Finds the shortest path from the origin coordinates to the destination coordinates using the A* algorithm.

        The graph has obstacles represented by 1 and traversable cells represented by 0.

        Args:
            graph (List[List[int]]): The graph representing the game board.
            originX (int): The x-coordinate of the origin.
            originY (int): The y-coordinate of the origin.
            desX (int): The x-coordinate of the destination.
            desY (int): The y-coordinate of the destination.

        Returns:
            List[Tuple[int, int]]: The list of coordinates representing the shortest path from the origin to the destination.

        Contributors:
            - @SantiagoRR2004
        """

        def is_valid_move(x: int, y: int, graph: List[List[int]]) -> bool:
            """
            Check if the move is valid within the given graph.

            The move is valid if the coordinates are within the bounds of the graph
            and the cell is traversable (0).

            Args:
                x (int): The x-coordinate of the move.
                y (int): The y-coordinate of the move.
                graph (List[List[int]]): The graph representing the game board.

            Returns:
                bool: True if the move is valid, False otherwise.

            Contributors:
                - @SantiagoRR2004
            """
            # Check if the move is within the bounds and the cell is traversable
            return 0 <= x < len(graph) and 0 <= y < len(graph[0]) and graph[x][y] == 0

        def findClosestNode(
            nodes: List[Tuple[Tuple[int, int], List]], goal: Tuple[int, int]
        ) -> Tuple[Tuple[int, int], List]:
            """
            Finds the closest node in the list of nodes to the given goal coordinates.

            It also removes that node from the list.

            Args:
                nodes (List[Tuple[Tuple[int, int], List]]): A list of nodes, where each node is represented by a tuple
                    containing its coordinates and a list of additional information.
                goal (Tuple[int, int]): The goal coordinates to find the closest node to.

            Returns:
                Tuple[Tuple[int, int], List]: The coordinates and additional information of the closest node.

            Contributors:
                - @SantiagoRR2004
            """
            bestNode = nodes[0]
            minDistance = (bestNode[0][0] - goal[0]) ** 2 + (
                bestNode[0][1] - goal[1]
            ) ** 2

            for node in nodes:
                distance = (node[0][0] - goal[0]) ** 2 + (node[0][1] - goal[1]) ** 2
                if distance < minDistance:
                    bestNode = node
                    minDistance = distance

            nodes.remove(bestNode)
            return bestNode[0], bestNode[1]

        openSet = []
        closedSet = set()

        startNode = (originX, originY)
        goalNode = (desX, desY)

        openSet.append((startNode, []))  # (node, path)

        while openSet:
            currentNode, currentPath = findClosestNode(openSet, goalNode)

            if currentNode == goalNode:
                return currentPath + [currentNode]

            closedSet.add(currentNode)

            x, y = currentNode

            # Define possible moves (up, down, left, right)
            moves = AbstractUser.calculateNearbyPositions(x, y, 1)

            for neighbor in moves:
                if is_valid_move(*neighbor, graph) and neighbor not in closedSet:
                    openSet.append((neighbor, currentPath + [currentNode]))

        return None  # No path found

    @staticmethod
    def calculateNearbyPositions(
        x: int, y: int, numMoves: int = 1
    ) -> List[Tuple[int, int]]:
        """
        Calculates the nearby positions that can be reached with numMoves.

        Args:
            - x (int): The x-coordinate of the current position.
            - y (int): The y-coordinate of the current position.
            - numMoves (int): The number of moves to consider.

        Returns:
            - List[Tuple[int, int]]: A list of tuples representing the nearby positions.

        Contributors:
            - @SantiagoRR2004
        """
        positions = []

        for horizontal in range(-numMoves, numMoves + 1):
            for vertical in range(-numMoves, numMoves + 1):
                if abs(horizontal) + abs(vertical) <= numMoves:
                    positions.append((x + horizontal, y + vertical))

        return positions
