#!/usr/bin/python
# -*- coding: UTF-8 -*-
import HouseEnv
import GridWorldModel
from typing import List

class HouseModel2(GridWorldModel):
	def openCabinet(self) -> long:
		pass

	def closeCabinet(self) -> long:
		pass

	def moveTowards(self) -> long:
		pass

	def getDrug(self) -> long:
		pass

	def addBeer(self) -> long:
		pass

	def handInDrug(self) -> long:
		pass

	def sipDrug(self) -> long:
		pass

	def __init__(self):
		self._availableBeers : int = None
		self._sipCount : int = None
		self._cabinetOpen : long = None
		self._carryingDrug : long = None
		self._model : HouseEnv = None

