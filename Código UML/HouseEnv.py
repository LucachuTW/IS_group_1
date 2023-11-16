#!/usr/bin/python
# -*- coding: UTF-8 -*-
import HouseModel2
import Enviroment
from typing import List

class HouseEnv(Enviroment):
	def init(self):
		pass

	def executeAction(self):
		pass

	def updatePercepts(self):
		pass

	def __init__(self):
		self._model : HouseModel2 = None

