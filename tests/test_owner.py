import unittest
from typing import Any, List
from owner import Owner, NormalOwner, EmergencyOwner
import Context
import houseModel
import houseEnv
import houseView


class helpTestOwner:
    """
    This class exists to help test the owner
    """

    def setUp(self) -> None:
        """
        This runs for every test at the start automatically.

        For all these tests we create an owner with controller and viewer.

        Contributors:
            - @SantiagoRR2004
        """
        self.model = houseModel.HouseModel("environmentBackup.json")
        self.view = houseView.HouseView(self.model)
        self.control = houseEnv.HouseEnv(self.model)
        self.control.setView(self.view)

        self.owner = Owner(self.control, self.view)

    def tearDown(self) -> None:
        """
        This runs for every test at the end automatically.

        It deletes objects to free space up and make sure all threads have finished.

        Contributors:
            - @SantiagoRR2004
        """
        self.deleteThreads([self.owner])
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


class testOwner(helpTestOwner, unittest.TestCase):
    def test_getContext(self):
        """
        Test if the owner has a context

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        self.assertIsInstance(owner.context, Context.Context)

    def test_state(self):
        """
        Test if the owner has a context

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        self.assertTrue(owner.context._state)

    def test_data(self):
        """
        Test if the owner has a data

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        self.assertTrue(owner.data)
        self.assertIsInstance(owner.data, dict)

    def test_setup(self):
        """
        Test that the owner has a setup method

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        owner.setup()
        self.assertIsNone(owner.setup())

    def test_getThreads(self):
        """
        Test the getThreads method of the owner object

        This test checks if the getThreads method of the owner object returns a
        list with callable methods.

        Contributors:
            - @SantiagoRR2004
        """
        threads = self.owner.getThreads()
        self.assertIsInstance(threads, list)
        for th in threads:
            assert callable(th)

    def test_changePulse(self):
        """
        Test the changePulse method of the owner object

        This test checks if the changePulse method of the owner object changes
        the pulse attribute of the owner's data

        Because it changes randomly it could be the same and fail the test

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        pulse = owner.data["pulse"]
        for i in range(10):
            owner.changePulse()
            self.failIfEqual(owner.data["pulse"], pulse)

    def test_checkForDeath(self):
        """
        Test the checkForDeath method of the owner object

        This test checks if the checkForDeath method of the owner object sets
        the health attribute of the owner's data to 100 when the health is 0.

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        owner.data["health"] = -1
        owner.checkForDeath()
        self.assertAlmostEqual(owner.data["health"], 100, delta=0.5)

    def test_stateOfEmergency(self):
        """
        Test the stateOfEmergency method of the owner object

        This test checks if the stateOfEmergency method of the owner object returns
        True when the health attribute of the owner's data is less than or equal to 50
        and false when it is more than 100.

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        testNumbers = {
            20: True,
            50: True,
            15: True,
            100: False,
            99.9999: True,
            101: False,
            99: True,
        }

        for number, value in testNumbers.items():
            owner.data["health"] = number
            self.assertEqual(owner.stateOfEmergency(), value)


class testNormalOwner(helpTestOwner, unittest.TestCase):
    def test_transition_to(self):
        """
        Test that the owner changes to Normal

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        owner.context.transition_to(NormalOwner)
        self.assertIsInstance(owner.context._state, NormalOwner)

    def test_moveRandomly(self):
        """
        Test that the owner can move to a random spot

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        owner.context.transition_to(NormalOwner)
        owner.context._state.moveRandomly()

    def test_moveRandomlyNearby(self):
        """
        Test that the owner can move to a random spot nearby

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        owner.deleteThreads()
        owner.context.transition_to(NormalOwner)
        if isinstance(owner.context._state, NormalOwner):
            owner.context._state.moveRandomlyNearby()

    def test_sitArmchair(self):
        """
        Test that the owner can sit on an armchair

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        owner.context.transition_to(NormalOwner)
        owner.context._state.sitArmchair()


class testEmergencyOwner(helpTestOwner, unittest.TestCase):
    def test_transition_to(self):
        """
        Test that the owner changes to Emergency

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        owner.context.transition_to(EmergencyOwner)
        self.assertIsInstance(owner.context._state, EmergencyOwner)

    def test_moveRandomly(self):
        """
        Test that the owner can't move to a random spot

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        owner.context.transition_to(EmergencyOwner)
        with self.assertRaises(AttributeError):
            owner.context._state.moveRandomly()

    def test_moveRandomlyNearby(self):
        """
        Test that the owner can't move to a random spot nearby

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        owner.context.transition_to(EmergencyOwner)
        with self.assertRaises(AttributeError):
            owner.context._state.moveRandomlyNearby()

    def test_consumeDrugs(self):
        """
        Test that the owner consumes drugs while in emergency

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.owner
        owner.context.transition_to(EmergencyOwner)
        owner.context._state.consumeDrug()
