import unittest
from typing import List
import Context
from owner import Owner, NormalOwner, EmergencyOwner
from robot import Robot, NormalRobot, EmergencyRobot
import houseModel
import houseEnv
import houseView


class helpTestRobot:
    """
    This class exists to help test the robot
    """

    def setUp(self) -> None:
        """
        This runs for every test at the start automatically.

        For all these tests we create an owner and a robot with controller and viewer.

        Contributors:
            - @SantiagoRR2004
        """
        self.model = houseModel.HouseModel("environmentBackup.json")
        self.view = houseView.HouseView(self.model)
        self.control = houseEnv.HouseEnv(self.model)
        self.control.setView(self.view)

        self.owner = Owner(self.control, self.view, "owner")
        self.robot = Robot(self.control, self.view, "robot")

    def tearDown(self) -> None:
        """
        This runs for every test at the end automatically.

        It deletes objects to free space up and make sure all threads have finished.

        Contributors:
            - @SantiagoRR2004
        """
        self.deleteThreads([self.owner, self.robot])
        del self.robot
        del self.owner
        del self.control
        del self.view
        del self.model

    @staticmethod
    def deleteThreads(objects: List) -> None:
        """
        Stops threads of objects in a list.

        Args:
        - objects: list of intances to have their threads stopped

        Returns:
        - None

        Contributors:
            - @SantiagoRR2004
        """
        for object in objects:
            object.deleteThreads()


class testRobot(helpTestRobot, unittest.TestCase):
    def test_getContext(self):
        """
        Test if the robot has a context

        Contributors:
            - @SantiagoRR2004
        """
        robot = self.robot
        self.assertIsInstance(robot.context, Context.Context)

    def test_state(self):
        """
        Test if the robot has a context

        Contributors:
            - @SantiagoRR2004
        """
        robot = self.robot
        self.assertTrue(robot.context._state)

    def test_data(self):
        """
        Test if the robot has a data

        Contributors:
            - @SantiagoRR2004
        """
        robot = self.robot
        self.assertTrue(robot.data)
        self.assertIsInstance(robot.data, dict)


class testNormalRobot(helpTestRobot, unittest.TestCase):
    def test_transition_to(self):
        """
        Test that if the owner changes to Normal the robot does too

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        robot = self.robot
        owner.context.transition_to(NormalOwner)
        self.assertIsInstance(robot.context._state, NormalRobot)

    def test_fillUp(self):
        """
        Test that the robot fills up on drugs

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        robot = self.robot
        owner.context.transition_to(NormalOwner)
        robot.context._state.fillUp()

    def test_stayClose(self):
        """
        Test that the robot stays close to the owner

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        robot = self.robot
        owner.context.transition_to(NormalOwner)
        robot.context._state.stayClose()

    def test_giveDrugs(self):
        """
        Test that the robot doesn't give medicine to the owner if he is fine

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        robot = self.robot
        owner.context.transition_to(NormalOwner)
        with self.assertRaises(AttributeError):
            robot.context._state.giveDrugs()


class testEmergencyRobot(helpTestRobot, unittest.TestCase):
    def test_transition_to(self):
        """
        Test that if the owner changes to Emergency the robot does too

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        robot = self.robot
        owner.context.transition_to(EmergencyOwner)
        self.assertIsInstance(robot.context._state, EmergencyRobot)

    def test_stayClose(self):
        """
        Test that the robot doesn't stay close to the owner

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        robot = self.robot
        owner.context.transition_to(EmergencyOwner)
        with self.assertRaises(AttributeError):
            robot.context._state.stayClose()

    def test_moveToOwner(self):
        """
        Test that the robot goes to help the owner

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        robot = self.robot
        owner.context.transition_to(EmergencyOwner)
        robot.context._state.moveToOwner()

    def test_giveDrugs(self):
        """
        Test that the robot gives medicine to the owner

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        robot = self.robot
        owner.context.transition_to(EmergencyOwner)
        robot.context._state.giveDrugs()
