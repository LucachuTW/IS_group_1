import AbstractHouseView
import pygame
import sys
import copy
from typing import Any, List


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
            for column in range(len(grid[0])):
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

    def drawAgent(self, object: Any) -> None:
        """
        Draw the agent.

        Args:
            - object (Any): The object to be drawn.

        Returns:
            - None

        Contributors:
            - @antonoterof
            - @SantiagoRR2004
        """
        model = self.getModel()
        return model.getAttribute(object)

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
                    self.screen.blit(
                        self.images.get(piece, self.images[2]),
                        (index_j * self.GRID_SIZE, index_i * self.GRID_SIZE),
                    )

    def move_robot(self, matrix: List, from_pos: List, to_pos: List) -> None:
        """
        Move the robot from one position to another in the matrix.

        Args:
            - matrix (List[List[str]]): The matrix representing the house view.
            - from_pos (List[int]): The current position of the robot in the matrix.
            - to_pos (List[int]): The target position where the robot should be moved.

        Returns:
            - None

        Contributors:
            - @antonvm2004
        """
        current_piece = matrix[from_pos[0]][from_pos[1]]

        if 0 <= to_pos[0] < len(matrix) and 0 <= to_pos[1] < len(matrix[0]):
            target_piece = matrix[to_pos[0]][to_pos[1]]

            if current_piece == "11":
                if target_piece == "3":
                    matrix[to_pos[0]][to_pos[1]] = current_piece
                    matrix[from_pos[0]][from_pos[1]] = "0"
                elif target_piece == "0":
                    matrix[to_pos[0]][to_pos[1]] = current_piece
                    matrix[from_pos[0]][from_pos[1]] = "0"
                else:
                    matrix[from_pos[0]][from_pos[1]] = current_piece

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
        pygame.display.set_caption("Interface with Mobile Image")

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

        robot_pos = [10, 11]  # Initial robot position

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

        self.draw_grid()
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
