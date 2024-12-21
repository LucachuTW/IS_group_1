#!/usr/bin/python
# -*- coding: UTF-8 -*-
import AbstractUser
import AbstractHouseView
from typing import List


class HouseView(AbstractHouseView):
    def __init__(self, aSelf):
        """Initializes the HouseModel class.

        Args:
        - None

        Returns:
        - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004"""
        self._pygameNotReady = None
        self._images = images
        self._wHITE = 246, 246, 246
        """Define colors"""
        self._bLACK = 0, 0, 0
        self._gRID_SIZE = 50
        """Grid size"""
        self._num_rows = num_rows
        self._num_columns = num_columns
        self._screen = pygame.display.set_mode(WINDOW_WIDTH, WINDOW_HEIGHT)
        self._unnamed_AbstractUser_: AbstractUser = None
        """# @AssociationKind Composition"""

    def draw(self, aSelf):
        """Draw the house.

        Args:
        - None

        Returns:
        - None

        Contributors:
            - @antonoterof
            - @SantiagoRR2004"""
        pass

    def drawAgent(self, aObject):
        pass

    def load_images(self, aSelf):
        pass

    def move_robot(self, aMatrix, aFrorm_pos, aTo_pos):
        pass

    def draw_pieces(self, aMatrix):
        pass

    def preparePygame(self, aSelf):
        """Prepare pygame.

        Args:
        - None

        Returns:
        - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004"""
        pass

    def draw_grid(self, aSelf):
        """Draw the grid.

        Args:
        - None

        Returns:
        - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004"""
        pass

    def updateImage(self, aSelf):
        """Update the image.

        Args:
        - None

        Returns:
        - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004w"""
        pass

    def showImage(self, aSelf):
        """Show the image.

        Args:
        - None

        Returns:
        - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004"""
        pass

    def drawAgent(self, aSelf, aObject):
        """Draw the agent.

        Args:
        - None

        Returns:
        - None

        Contributors:
            - @antonoterof
            - @SantiagoRR2004"""
        pass

    def draw_pieces(self, aSelf, aMatrix):
        """Draw the pieces.

        Args:
        - None

        Returns:
        - None

        Contributors:
            - @antonvm2004
            - @SantiagoRR2004"""
        pass

    def move_robot(self, aSelf, aMatrix, aFrom_pos, aTo_pos):
        """Move the robot.

        Args:
        - None

        Returns:
        - None

        Contributors:
            - @antonvm2004"""
        pass
