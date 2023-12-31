#!/usr/bin/python
# -*- coding: UTF-8 -*-
import AbstractHouseModel
from typing import List

class HouseModel(AbstractHouseModel):
	def __init__(self, aSelf):
		"""Initializes the HouseModel class.
		
		        Args:
		        - None
		
		        Returns:
		        - None
		
		        Contributors:
		            - @SantiagoRR2004
		            - @Ventupentu"""
		self._grid = [[int(x) for x in row] for row in data["grid"]]
		self._symbols = data["symbols"]

	def addDrug(self, aObject, aQuantity):
		pass

	def getDrug(self, aObject):
		pass

	def getOpenStatus(self, aObject):
		pass

	def setOpenStatus(self, aObject, aStatus):
		pass

	def getCapacity(self, aObject):
		pass

	def changePosition(self, aOriginX, aOriginY, aDestinationX, aDestinationY):
		pass

	def getPosition(self, aX, aY):
		pass

	def setPosition(self, aX, aY, aValue):
		pass

	def removeValue(self, aValue):
		pass

	def getPositionOf(self, aValue):
		pass

	def getOpenableStatus(self, aObject):
		pass

	def getDoorStatus(self, aDoorLocation):
		pass

	def closeDoor(self, aDoorLocation):
		pass

	def getSemisolidStatus(self, aObjects):
		pass

	def saveToFile(self, aSelf):
		"""Save the current state of the HouseModel to a file.
		
		        Args:
		            None
		
		        Returns:
		            None"""
		pass

	def openDoor(self, aDoorLocation):
		pass

	def addDrug(self, aSelf, aObject = str, aQuantity = int):
		"""Adds a drug to the object.
		
		        Args:
		        - object: The object to add the drug to.
		        - quantity: The quantity of drugs to add.
		
		        Returns:
		        - None
		
		        Contributors:
		            - @Ventupentu
		            - @SantiagoRR2004"""
		pass

	def getDrug(self, aSelf, aObject = str) -> int:
		"""Gets the drug from the object.
		
		        Args:
		        - object: The object to get the drug from.
		
		        Returns:
		        - The drug from the object.
		
		        Contributors:
		            - @Ventupentu
		            - @SantiagoRR2004"""
		pass

	def getOpenStatus(self, aSelf, aObject = str, aX = int, aY = int) -> long:
		"""Gets the open status of the object.
		
		        Args:
		        - object: The object to get the open status from.
		
		        Returns:
		        - The open status of the object.
		
		        Contributors:
		            - @Ventupentu
		            - @SantiagoRR2004
		            - @LucachuTW"""
		pass

	def setOpenStatus(self, aSelf, aObject = str, aStatus = bool):
		"""Sets the open status of the object.
		
		        Args:
		        - object: The object to set the open status to.
		        - status: The status to set the object to.
		
		        Returns:
		        - None
		
		        Contributors:
		            - @Ventupentu
		            - @SantiagoRR2004
		            - @LucachuTW"""
		pass

	def getCapacity(self, aSelf, aObject = str) -> int:
		"""Gets the capacity of the object.
		
		        Args:
		        - object: The object to get the capacity from.
		
		        Returns:
		        - The capacity of the object.
		
		        Contributors:
		            - @Ventupentu
		            - @SantiagoRR2004"""
		pass

	def changePosition(self, aSelf, aOriginX = int, aOriginY = int, aDestinationX = int, aDestinationY = int):
		"""Changes the position of the object.
		
		        Args:
		        - originX: The x coordinate of the origin.
		        - originY: The y coordinate of the origin.
		        - destinationX: The x coordinate of the destination.
		        - destinationY: The y coordinate of the destination.
		
		        Returns:
		        - None
		
		        Contributors:
		            - @SantiagoRR2004
		            - @antonvm2004"""
		pass

	def getPosition(self, aSelf, aX = int, aY = int) -> int:
		"""Get the position at coordinates (x, y) in the grid.
		
		        Args:
		            x (int): The x-coordinate.
		            y (int): The y-coordinate.
		
		        Returns:
		            The value at the specified position in the grid.
		
		        Contributors:
		            - @antonvm2004"""
		pass

	def setPosition(self, aSelf, aX = int, aY = int, aValue = int):
		"""Set the position at coordinates (x, y) in the grid.
		
		        Args:
		            x (int): The x-coordinate.
		            y (int): The y-coordinate.
		            value: The value to set at the specified position.
		
		        Returns:
		            None
		
		        Contributors:
		            - @antonvm2004"""
		pass

	def removeValue(self, aSelf, aValue = str):
		"""Remove the specified value from the grid.
		
		        Args:
		            value: The value to remove.
		
		        Returns:
		            None
		
		        Contributors:
		            - @antonoterof"""
		pass

	def getPositionOf(self, aSelf, aValue = str):
		"""Get the position of the specified value in the grid.
		
		        Args:
		            value: The value to find the position of.
		
		        Returns:
		            The position of the value in the grid.
		
		        Contributors:
		            - @antonoterof"""
		pass

	def getOpenableStatus(self, aSelf, aObject = str):
		"""Get the openable status of the object.
		
		        Args:
		            object: The object to get the openable status from.
		
		        Returns:
		            The openable status of the object.
		
		        Contributors:
		            - @antonoterof"""
		pass

	def getSemisolidStatus(self, aSelf, aObject = str):
		"""Get the semisolid status of the object.
		
		        Args:
		            object: The object to get the semisolid status from.
		
		        Returns:
		            The semisolid status of the object.
		
		        Contributors:
		            - @antonoterof"""
		pass

	def getDoorStatus(self, aSelf, aDoorLocation = List[int]) -> long:
		"""Get the status of the door.
		
		        Args:
		            doorLocation: The location of the door.
		
		        Returns:
		            The status of the door.
		
		        Contributors:
		            - @antonoterof"""
		pass

	def openDoor(self, aSelf, aDoorLocation = List[int]):
		"""Open a door at the specified location.
		
		        Args:
		            doorLocation (List[int]): The [x, y] coordinates of the door.
		
		        Contributors:
		            - @antonoterof"""
		pass

	def closeDoor(self, aSelf, aDoorLocation = List[int]):
		"""Close a door at the specified location.
		
		        Args:
		            doorLocation (List[int]): The [x, y] coordinates of the door.
		
		        Contributors:
		            - @antonoterof"""
		pass

