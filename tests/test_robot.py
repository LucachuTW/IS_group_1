import unittest
import main
import time
import Context
from owner import Owner, NormalOwner, EmergencyOwner
from robot import Robot, NormalRobot, EmergencyRobot


class destroyer:
    """
    This class exists so the threads end after all the tests
    """

    def setUp(self):
        self.items = main.createHouse()

    def tearDown(self):
        endEverything(self.items[3], self.items[4])


def endEverything(owner: Owner, robot: Robot, wait: int = 0) -> None:
    time.sleep(wait)
    owner.__del__()
    robot.__del__()


class testRobot(destroyer, unittest.TestCase):
    def test_getContext(self):
        """
        Test if the robot has a context

        Contributors:
            - @SantiagoRR2004
        """
        robot = self.items[4]
        self.assertIsInstance(robot.context, Context.Context)

    def test_state(self):
        """
        Test if the robot has a context

        Contributors:
            - @SantiagoRR2004
        """
        robot = self.items[4]
        self.assertTrue(robot.context._state)

    def test_data(self):
        """
        Test if the robot has a data

        Contributors:
            - @SantiagoRR2004
        """
        robot = self.items[4]
        self.assertTrue(robot.data)
        self.assertIsInstance(robot.data, dict)


class testNormalRobot(destroyer, unittest.TestCase):
    def test_transition_to(self):
        """
        Test that if the owner changes to Normal the robot does too

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
        robot = self.items[4]
        owner.context.transition_to(NormalOwner)
        self.assertIsInstance(robot.context._state, NormalRobot)


class testEmergencyRobot(destroyer, unittest.TestCase):
    def test_transition_to(self):
        """
        Test that if the owner changes to Emergency the robot does too

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
        robot = self.items[4]
        owner.context.transition_to(EmergencyOwner)
        self.assertIsInstance(robot.context._state, EmergencyRobot)
