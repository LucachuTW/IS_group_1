import AbstractHouseView
import pygame
import sys
import copy
from typing import Any, List, Dict, Tuple


class HouseView(AbstractHouseView.AbstractHouseView):
    pygameNotReady = True

    def draw(self) -> List:
        """
        Draw the house.

        Args:
            - None

        Returns:
            - The matrix representing the house view.

        Contributors:
            - @antonoterof
            - @SantiagoRR2004

        """
        model = self.getModel()
        return model.getAttribute("grid")

    def drawMovableTo(self) -> List:
        """
        Draw the a matrix with ones where you would
        be blocked and 0 where you can move to.

        Args:
            - None

        Returns:
            - The matrix representing the house view.

        Contributors:
            - @SantiagoRR2004

        """
        model = self.getModel()
        grid = copy.deepcopy(model.getAttribute("grid"))
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                valueToCheck = grid[row][column]
                if valueToCheck != 0:
                    if self.getModel().checkIfPrime(valueToCheck):
                        for key, value in self.drawAgent("symbols").items():
                            if valueToCheck == value:
                                if self.drawAgent(key)["semisolid"]:
                                    grid[row][column] = 0
                                else:
                                    grid[row][column] = 1
                    else:
                        grid[row][column] = 1
        return grid

    def drawAgent(self, object: str) -> Dict:
        """
        Draw the agent.

        Args:
            - object (str): The name of the agent to draw.

        Returns:
            - The dictionary representing the agent.

        Contributors:
            - @antonoterof
            - @SantiagoRR2004
        """
        model = self.getModel()
        return model.getAttribute(object)

    def findNearestPositionOfSomething(
        self, element: str, searcherX: int = None, searcherY: int = None
    ) -> Tuple[int, int]:
        """
        Find the nearest position of something.
        If the location of the element is not specified,
        the method will find the first position of the element in the house.

        Args:
            - element (str): The name of the element to find.
            - searcherX (int, optional): The x coordinate of center of the search.
            - searcherY (int, optional): The y coordinate of center of the search.

        Returns:
            - Tuple[int, int]: A tuple containing the x and y coordinates of the nearest position.

        Contributors:
            - @SantiagoRR2004
        """
        symbol = self.drawAgent(element)["symbol"]
        grid = self.draw()
        if self.drawAgent(element)["unique"]:
            for row in range(len(grid)):
                for column in range(len(grid[row])):
                    if grid[row][column] == symbol:
                        return row, column
                    if not self.getModel().checkIfPrime(grid[row][column]):
                        if symbol in self.getModel().PrimeFactorization(
                            grid[row][column]
                        ):
                            return row, column

        elif searcherX is None or searcherY is None:
            return self.drawAgent(element)["subset"][0]["location"]

        elif (
            searcherX is not None
            and searcherY is not None
            and "subset" in self.drawAgent(element)
        ):
            best = self.drawAgent(element)["subset"][0]["location"]
            minDistance = self.model.calculateDistanceBetween2Points(
                best[0], best[1], searcherX, searcherY
            )

            for possibility in self.drawAgent(element)["subset"]:
                distance = self.model.calculateDistanceBetween2Points(
                    possibility["location"][0],
                    possibility["location"][1],
                    searcherX,
                    searcherY,
                )
                if distance < minDistance:
                    minDistance = distance
                    best = possibility["location"]

            return best[0], best[1]

        elif searcherX is not None and searcherY is not None:
            rows = len(grid)
            cols = len(grid[0])

            for radius in range(max(rows, cols)):
                for i in range(searcherX - radius, searcherX + radius + 1):
                    for j in range(
                        searcherY - radius,
                        searcherY + radius + 1,
                    ):
                        # Check if the current coordinates are within the matrix bounds
                        if 0 <= i < rows and 0 <= j < cols:
                            # Check if the value at the current coordinates matches the target value
                            if grid[i][j] == symbol:
                                return i, j

        return (
            searcherX,
            searcherY,
        )  # If it can't find anything, return the same position

    def load_images(self) -> None:
        """
        Loads and scales images for the house view.

        Returns:
            None

        Contributors:
            - @antonvm2004
        """
        images = {}
        for name, number in self.drawAgent("symbols").items():
            img_path = f"./images/{name}.png"
            image = pygame.image.load(img_path)
            image = pygame.transform.scale(image, (self.GRID_SIZE, self.GRID_SIZE))
            images[number] = image
        self.images = images

    def draw_grid(self) -> None:
        """
        Draw the grid.

        Args:
            - None

        Returns:
            - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004
        """
        for x in range(0, self.num_columns * self.GRID_SIZE, self.GRID_SIZE):
            pygame.draw.line(
                self.screen, self.BLACK, (x, 0), (x, self.num_rows * self.GRID_SIZE)
            )
        for y in range(0, self.num_rows * self.GRID_SIZE, self.GRID_SIZE):
            pygame.draw.line(
                self.screen, self.BLACK, (0, y), (self.num_columns * self.GRID_SIZE, y)
            )

    def draw_pieces(self, matrix: List) -> None:
        """
        Draw the pieces on the matrix.

        Args:
            - matrix (List): The matrix representing the game board.

        Returns:
            - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004
        """
        for index_i, row in enumerate(matrix):
            for index_j, piece in enumerate(row):
                if piece != 0:
                    pieces = self.getModel().PrimeFactorization(piece)
                    for pi in pieces:
                        self.screen.blit(
                            self.images.get(pi, self.images[2]),
                            (index_j * self.GRID_SIZE, index_i * self.GRID_SIZE),
                        )

    def preparePygame(self) -> None:
        """
        Prepare pygame.

        This method initializes the pygame library and
        sets up the necessary variables and configurations for the game interface.

        Args:
            - None

        Returns:
            - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004
        """
        pygame.init()

        # Define colors
        self.WHITE = (246, 246, 246)
        self.BLACK = (0, 0, 0)

        # Grid size
        self.GRID_SIZE = 50

        matrix = self.draw()

        door_info = self.drawAgent("door")

        num_rows = len(matrix)
        self.num_rows = num_rows
        num_columns = len(matrix[0]) if num_rows > 0 else 0
        self.num_columns = num_columns

        WINDOW_WIDTH = num_columns * self.GRID_SIZE
        WINDOW_HEIGHT = num_rows * self.GRID_SIZE

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Casa domótica")

        self.load_images()

    def showImage(self) -> None:
        """
        Show the image.

        This method displays the image on the screen using the Pygame library.
        It draws a grid and the pieces of the image on the screen.

        Args:
            - None

        Returns:
            - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        matrix = self.draw()

        for index_i, row in enumerate(matrix):
            for index_j, piece in enumerate(row):
                pygame.draw.rect(
                    self.screen,
                    self.WHITE,
                    (
                        index_j * self.GRID_SIZE,
                        index_i * self.GRID_SIZE,
                        self.GRID_SIZE,
                        self.GRID_SIZE,
                    ),
                )

        # self.draw_grid()
        self.draw_pieces(matrix)
        pygame.display.flip()

    def updateImage(self) -> None:
        """
        Update the image.

        This method prepares Pygame if it is not ready and then shows the image.

        Args:
            - None

        Returns:
            - None: This method does not return any value.

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004
        """
        if self.pygameNotReady:
            self.preparePygame()
            self.pygameNotReady = False

        self.showImage()
