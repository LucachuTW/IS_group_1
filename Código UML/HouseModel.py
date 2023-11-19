#!/usr/bin/python
# -*- coding: UTF-8 -*-
import HouseEnv
import GridWorldModel
from typing import List

class HouseModel(GridWorldModel):
	# @LucachuTW-@Ventupentu
	def addDrug(self) -> long:
		pass

	def getDrug(self) -> long:
		pass

	def getOpenStatus(self) -> long:
		pass

	def setOpenStatus(self) -> long:
		pass

	def getCapacity(self) -> long:
		pass

	def changePosition(self) -> long:
		pass

	def getPosition(self) -> long:
		pass

	def setPosition(self) -> long:
		pass

	def removeValue(self) -> long:
		pass

	def getPositionOf(self) -> long:
		pass

	def __init__(self):
		self._availableDrugs : int = None
		self._sipCount : int = None
		self._cabinetOpen : long = None
		self._position : long = None
		self._model : HouseEnv = None

