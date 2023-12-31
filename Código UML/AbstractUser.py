#!/usr/bin/python
# -*- coding: UTF-8 -*-
import HouseView
import HouseEnv
import Context
from typing import List

class AbstractUser(object):
	def __init__(self, aModel):
		self.___requiredData = None
		self._exitNegativeFlag = None
		self._view = viewer
		self._controller = controller
		self._threads = []
		self._context = context
		self._unnamed_HouseView_ : HouseView = None
		self._unnamed_HouseEnv_ : HouseEnv = None
		self._unnamed_Context_ : Context = None
		self._unnamed_Context_2 : Context = None
		"""# @AssociationKind Composition"""

	def getController(self, aSelf) -> Any:
		"""Retrieve the controller associated with the current instance.
		
		        Returns:
		            Any: The controller object.
		
		        Note:
		            This method provides access to the controller assigned to the instance.
		            Ensure that the controller has been properly set before calling this method.
		
		        Contributors:
		            - @SantiagoRR2004"""
		pass

	def getView(self, aSelf) -> Any:
		"""Get the current view associated with this object.
		
		        Returns:
		            Any: The current view.
		
		        Note:
		            This method returns the view assigned to the object.
		            Ensure that the view has been properly set before calling this method.
		
		        Contributors:
		            - @SantiagoRR2004"""
		pass

	def setUp(self):
		pass

	def checkData(self, aSelf):
		"""Check if the self.data is correct according to self.requiredData
		
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
		            Check position"""
		pass

	def delteteThreads(self):
		pass

	def getThreads(self, aSelf) -> List:
		"""BLA BLA BLA BLA
		
		        Contributors:
		            - @SantiagoRR2004"""
		pass

	def __del__(self, aSelf):
		pass

	def __init__(self, aSelf, aController = Any, aViewer = Any):
		pass

	def getContext(self, aSelf) -> Context:
		pass

	def setContext(self, aSelf, aContext = Context):
		pass

	def setPosition(self, aSelf):
		"""Finds the position of symbol on the grid and
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
		            - @SantiagoRR2004"""
		pass

	def setup(self, aSelf):
		"""Perform setup operations for the object.
		
		        This method is meant to be overridden by subclasses to define
		        specific setup actions needed for the functionality of the object.
		        It is called during the initialization phase to configure the object
		        before any other operations are performed.
		
		        Subclasses should implement this method with the necessary steps
		        required for proper setup. The method signature must be preserved.
		
		        Returns:
		            None: This method does not return any value.
		
		        Contributors:
		            - @SantiagoRR2004"""
		pass

	def setUpThreading(self, aSelf):
		pass

	def deleteThreads(self, aSelf):
		pass

