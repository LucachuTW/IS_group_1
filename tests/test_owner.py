import unittest
import main
import time


def endEverything(owner, robot, wait: int = 0) -> None:
    time.sleep(wait)
    owner.__del__()
    robot.__del__()


class testOwner(unittest.TestCase):
    def test_example(self):
        items = main.createHouse()

        endEverything(items[3], items[4])


class testNormalOwner(unittest.TestCase):
    def test_example(self):
        items = main.createHouse()

        endEverything(items[3], items[4])


class testEmergencyOwner(unittest.TestCase):
    def test_example(self):
        items = main.createHouse()

        endEverything(items[3], items[4])
