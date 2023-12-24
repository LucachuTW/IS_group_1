import unittest
import main
import time
from owner import Owner, NormalOwner, EmergencyOwner
import Context


class destroyer:
    """
    This class exists so the threads end after all the tests
    """

    def setUp(self):
        self.items = main.createHouse()

    def tearDown(self):
        endEverything(self.items[3], self.items[4])


def endEverything(owner: Owner, robot, wait: int = 0) -> None:
    time.sleep(wait)
    owner.__del__()
    robot.__del__()


class testOwner(destroyer, unittest.TestCase):
    def test_getContext(self):
        """
        Test if the owner has a context

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
        self.assertIsInstance(owner.context, Context.Context)

    def test_state(self):
        """
        Test if the owner has a context

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
        self.assertTrue(owner.context._state)

    def test_data(self):
        """
        Test if the owner has a data

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
        self.assertTrue(owner.data)
        self.assertIsInstance(owner.data, dict)

    def test_setup(self):
        """
        Test that the owner has a setup method

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
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
        threads = self.items[3].getThreads()
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
        owner = self.items[3]
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
        owner = self.items[3]
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
        owner = self.items[3]
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


class testNormalOwner(destroyer, unittest.TestCase):
    def test_transition_to(self):
        """
        Test that the owner changes to Normal

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
        owner.context.transition_to(NormalOwner)
        self.assertIsInstance(owner.context._state, NormalOwner)

    def test_moveRandomly(self):
        """
        Test that the owner can move to a random spot

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
        owner.context.transition_to(NormalOwner)
        owner.context._state.moveRandomly()

    def test_moveRandomlyNearby(self):
        """
        Test that the owner can move to a random spot nearby

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
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
        owner = self.items[3]
        owner.context.transition_to(NormalOwner)
        owner.context._state.sitArmchair()


class testEmergencyOwner(destroyer, unittest.TestCase):
    def test_transition_to(self):
        """
        Test that the owner changes to Emergency

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
        owner.context.transition_to(EmergencyOwner)
        self.assertIsInstance(owner.context._state, EmergencyOwner)

    def test_moveRandomly(self):
        """
        Test that the owner can't move to a random spot

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
        owner.context.transition_to(EmergencyOwner)
        with self.assertRaises(AttributeError):
            owner.context._state.moveRandomly()

    def test_moveRandomlyNearby(self):
        """
        Test that the owner can't move to a random spot nearby

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
        owner.context.transition_to(EmergencyOwner)
        with self.assertRaises(AttributeError):
            owner.context._state.moveRandomlyNearby()

    def test_consumeDrugs(self):
        """
        Test that the owner consumes drugs while in emergency

        Contributors:
            - @SantiagoRR2004
        """
        owner = self.items[3]
        owner.context.transition_to(EmergencyOwner)
        owner.context._state.consumeDrug()
