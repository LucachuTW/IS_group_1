#!/usr/bin/python
# -*- coding: UTF-8 -*-
import AbstractUser
import AbstractHouseEnv
import Enviroment
from typing import List


class HouseEnv(AbstractHouseEnv, Enviroment):
    """House Environment Class.

    This class represents the environment of a house. It includes methods to check if an element is shareable, if a position is movable, and to move an object to a specified position.

    Contributors:
        - @SantiagoRR2004
        - @Ventupentu
        - @antonoterof
        - @LucachuTW"""

    def __init__(self, aSelf):
        self._model = None
        self._unnamed_AbstractUser_: AbstractUser = None
        """# @AssociationKind Composition"""

    def checkAddDrug(self, aObject, aQuantity):
        pass

    def areAdjacent(self, aObject1, aObject2, aPosition1="", aPosition2=""):
        pass

    def transferDrugs(self, aMover, aGiver, aReciever, aQuantity):
        pass

    def moveTo(self, aMover: str, aMoved: str, aX: int, aY: int):
        pass

    def checkIfMovableTo(self, aX: int, aY: int):
        pass

    def moveOwner(self, aDirection: str):
        pass

    def canOwnerMoveTo(self, aLocation):
        pass

    def checkOpeneable(self, aElement: str):
        pass

    def checkIfShareable(self, aElement: str):
        pass

    def checkAddDrug(self, aSelf, aElement=str, aQuantity=int) -> long:
        """Check if a drug can be added to an element.

        This method checks if a specified quantity of drug can be added to a specified element in the model.

        Args:
        - element (str): The element to add the drug to.
        - quantity (int): The quantity of drug to add.

        Returns:
            bool: True if the drug can be added, False otherwise.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu
            - @antonoterof"""
        pass

    def checkOpeneable(self, aSelf, aElement=str) -> long:
        """Check if an element is openable.

        This method checks if a specified element is openable in the model.

        Args:
        - element (str): The element to check openability for.

        Returns:
            bool: True if the element is openable, False otherwise.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu"""
        pass

    def areAdjacent(
        self,
        aSelf,
        aObject1=str,
        aObject2=str,
        aPosition1=List[int],
        aPosition2=List[int],
    ) -> long:
        """Check if two objects are adjacent.

        This method checks if two objects are adjacent in the model. It considers objects to be adjacent if they are at the same position, or 1 position horizontally or vertically apart.

        Args:
        - object1 (str): The first object to check adjacency for.
        - object2 (str): The second object to check adjacency for.

        Returns:
            bool: True if the objects are adjacent, False otherwise.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def transferDrugs(
        self, aSelf, aMover=str, aGiver=str, aReciever=str, aQuantity=int
    ) -> long:
        """Transfer drugs from one object to another.

        This method transfers a specified quantity of drugs from a giver object to a receiver object, if certain conditions are met.

        Args:
        - mover (str): The object that is moving the drugs.
        - giver (str): The object that is giving the drugs.
        - reciever (str): The object that is receiving the drugs.
        - quantity (int): The quantity of drugs to transfer.

        Returns:
            bool: True if the transfer was successful, False otherwise.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def checkIfShareable(self, aSelf, aElement=str) -> long:
        """Check if an element is shareable.

        This method checks if a specified element is shareable in the model.

        Args:
        - element (str): The element to check shareability for.

        Returns:
            bool: True if the element is shareable, False otherwise.

        Contributors:
            - @SantiagoRR2004"""
        pass

    def checkIfMovableTo(self, aSelf, aX=int, aY=int) -> long:
        """Check if a position is movable.

        This method checks if a specified position is movable in the model.

        Args:
        - x (int): The x-coordinate of the position to check.
        - y (int): The y-coordinate of the position to check.

        Returns:
            bool: True if the position is movable, False otherwise.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof"""
        pass

    def moveTo(self, aSelf, aMover=str, aMoved=str, aX=int, aY=int) -> long:
        """Move an object to a specified position.

        This method moves a specified object to a specified position in the model, if certain conditions are met.

        Args:
        - mover (str): The object that is moving.
        - moved (str): The object that is being moved.
        - x (int): The x-coordinate of the position to move to.
        - y (int): The y-coordinate of the position to move to.

        Returns:
            bool: True if the move was successful, False otherwise.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu
            - @LucachuTW"""
        pass

    def moveOwner(self, aSelf, aDirection=str) -> long:
        """Move the owner to an adjacent position.

        Args:
            direction (str): The direction to move the owner ('up', 'down', 'left', 'right').

        Returns:
            bool: True if the movement was successful, False otherwise.

        Contributors:
            - @antonoterof"""
        pass

    def canOwnerMoveTo(self, aSelf, aLocation=List[int]) -> long:
        """Check if the owner can move to the specified position

        Args:
            location (List[int]): Las coordinates [x, y] to verify.

        Returns:
            bool: True if the owner can move to the position, False otherwise."""
        pass
