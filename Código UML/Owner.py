#!/usr/bin/python
# -*- coding: UTF-8 -*-
import NormalOwner
import EmergencyOwner
import AbstractUser
from typing import List

class Owner(AbstractUser):
	def setup(self, aSelf):
		pass

	def getThreads(self, aSelf) -> List:
		pass

	def changePulse(self, aSelf):
		pass

	def checkForDeath(self, aSelf):
		pass

	def changeState(self, aSelf):
		pass

	def startMain(self, aSelf):
		pass

	def stateOfEmergency(self, aSelf) -> long:
		pass

	def __init__(self):
		self.___requiredDara = None
		self.___exitNegativeFlag = None
		self._requiredData = {"unique": {"type": bool, "default": }, "numberDrugs": {"type": int, "default": 0}, "maxCapacity": {"type": int, "default": 1}, "symbol": {"type": int, "default": 7}, "openable": {"type": bool, "default": }, "semisolid": {"type": bool, "default": }, "moving": {"type": dict, "default": {"auto": , "mover": , "moved": }}, "pulse": {"type": float, "default": 50}, "health": {"type": float, "default": 100}}
		self._data = self.getView().drawAgent("owner")
		self._unnamed_NormalOwner_ : NormalOwner = None
		"""# @AssociationKind Composition"""
		self._unnamed_EmergencyOwner_ : EmergencyOwner = None
		"""# @AssociationKind Composition"""

