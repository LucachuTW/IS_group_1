#!/usr/bin/python
# -*- coding: UTF-8 -*-
import EmergencyRobot
import NormalRobot
import AbstractUser
from typing import List

class Robot(AbstractUser):
	def setup(self, aSelf):
		pass

	def getThreads(self, aSelf) -> List:
		pass

	def changeState(self, aSelf):
		pass

	def stateOfEmergency(self, aSelf) -> long:
		pass

	def startMain(self, aSelf):
		pass

	def checkForDeath(self, aSelf):
		pass

	def __init__(self):
		self._requiredData = {"unique": {"type": bool, "default": True}, "numberDrugs": {"type": int, "default": 0}, "maxCapacity": {"type": int, "default": 2}, "symbol": {"type": int, "default": 11}, "openable": {"type": bool, "default": False}, "semisolid": {"type": bool, "default": True}, "moving": {"type": dict, "default": {"auto": True, "mover": True, "moved": False}}}
		self._data = self.getView().drawAgent("robot")
		self._unnamed_EmergencyRobot_ : EmergencyRobot = None
		"""# @AssociationKind Composition"""
		self._unnamed_NormalRobot_ : NormalRobot = None
		"""# @AssociationKind Composition"""

