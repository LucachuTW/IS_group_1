#!/usr/bin/python
# -*- coding: UTF-8 -*-
import AbstractUser
from typing import List

class Context(object):
	"""The Context defines the interface of interest to clients. It also maintains
	    a reference to an instance of a State subclass, which represents the current
	    state of the Context.
	
	    Contributors:
	        - @SantiagoRR2004"""
	def __init__(self, aSelf, aState, aUser):
		"""Initialize the Context instance with the given state.
		
		        This method sets the initial state of the Context.
		
		        Args:
		            - state (State): The initial state.
		            - user (Any): The instance which is using Context.
		
		        Contributors:
		            - @SantiagoRR2004"""
		self._state = state(self.user)
		self._user = user
		self._unnamed_AbstractUser_ : AbstractUser = None
		self._unnamed_AbstractUser_2 : AbstractUser = None
		"""# @AssociationKind Composition"""

	def transition_to(self, aSelf, aState):
		"""The Context allows changing the State object at runtime.
		
		        This method changes the current state of the Context to the given state.
		
		        Args:
		            - state (State): The state to transition to.
		
		        Contributors:
		            - @SantiagoRR2004"""
		pass

	def doSomething(self, aSelf):
		"""The Context delegates part of its behavior to the current State object.
		
		        This method calls the main method of the current state.
		
		        Contributors:
		            - @SantiagoRR2004"""
		pass

