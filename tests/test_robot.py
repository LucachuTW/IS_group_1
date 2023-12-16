import unittest
import main
import time


def endEverything(owner, robot, wait: int = 0) -> None:
    time.sleep(wait)
    owner.__del__()
    robot.__del__()


class testRobot(unittest.TestCase):
    def test_example(self):
        items = main.createHouse()

        endEverything(items[3], items[4])


class testNormalRobot(unittest.TestCase):
    def test_example(self):
        items = main.createHouse()

        endEverything(items[3], items[4])


class testEmergencyRobot(unittest.TestCase):
    def test_example(self):
        items = main.createHouse()

        endEverything(items[3], items[4])
