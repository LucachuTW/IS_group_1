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
        Test the setup method of the owner object

        This test checks if the setup method of the owner object works correctly. 
        It checks if the drawAgent method of the viewer is called with "owner" as 
        argument and if the data attribute of the owner object is not None after 
        the setup.

        Contributors:
            - @LucachuTW
        """
        self.owner.setup()
        self.viewer.drawAgent.assert_called_with("owner")
        self.assertIsNotNone(self.owner.data)

    def test_getThreads(self):
        """
        Test the getThreads method of the owner object

        This test checks if the getThreads method of the owner object returns a 
        list with 4 elements.

        Contributors:
            - @LucachuTW
        """
        threads = self.owner.getThreads()
        self.assertEqual(len(threads), 4)

    def test_changePulse(self):
        """
        Test the changePulse method of the owner object

        This test checks if the changePulse method of the owner object changes 
        the pulse attribute of the owner's data to a value between 20 and 120.

        Contributors:
            - @LucachuTW
        """
        self.owner.exitNegativeFlag = False
        self.owner.changePulse()
        self.assertTrue(20 <= self.owner.data["pulse"] <= 120)

    def test_checkForDeath(self):
        """
        Test the checkForDeath method of the owner object

        This test checks if the checkForDeath method of the owner object sets 
        the health attribute of the owner's data to 100 when the health is 0.

        Contributors:
            - @LucachuTW
        """
        self.owner.exitNegativeFlag = False
        self.owner.data["health"] = 0
        self.owner.checkForDeath()
        self.assertEqual(self.owner.data["health"], 100)

    def test_changeState(self):
        """
        Test the changeState method of the owner object

        This test checks if the changeState method of the owner object changes 
        the context of the owner to an instance of the EmergencyOwner class when 
        the stateOfEmergency attribute of the owner is True.

        Contributors:
            - @LucachuTW
        """
        self.owner.exitNegativeFlag = False
        self.owner.stateOfEmergency = True
        self.owner.changeState()
        self.assertIsInstance(self.owner.context, EmergencyOwner)

    def test_stateOfEmergency(self):
        """
        Test the stateOfEmergency method of the owner object

        This test checks if the stateOfEmergency method of the owner object returns 
        True when the health attribute of the owner's data is less than or equal to 50.

        Contributors:
            - @LucachuTW
        """
        self.owner.data["health"] = 50
        self.assertTrue(self.owner.stateOfEmergency())


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
