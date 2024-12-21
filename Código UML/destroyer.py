#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List


class destroyer(object):
    """This class exists so the threads end after all the tests"""

    def setUp(self, aSelf):
        pass

    def tearDown(self, aSelf):
        pass

    def __init__(self):
        self._items = main.createHouse()
