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

    def setUp(self):
        self.controller = Mock()
        self.viewer = Mock()
        self.owner = Owner(self.controller, self.viewer)

    def test_setup(self):
        self.owner.setup()
        self.viewer.drawAgent.assert_called_with("owner")
        self.assertIsNotNone(self.owner.data)

    def test_getThreads(self):
        threads = self.owner.getThreads()
        self.assertEqual(len(threads), 4)

    def test_changePulse(self):
        self.owner.exitNegativeFlag = False
        self.owner.changePulse()
        self.assertTrue(20 <= self.owner.data["pulse"] <= 120)

    def test_checkForDeath(self):
        self.owner.exitNegativeFlag = False
        self.owner.data["health"] = 0
        self.owner.checkForDeath()
        self.assertEqual(self.owner.data["health"], 100)

    def test_changeState(self):
        self.owner.exitNegativeFlag = False
        self.owner.stateOfEmergency = True
        self.owner.changeState()
        self.assertIsInstance(self.owner.context, EmergencyOwner)

    def test_stateOfEmergency(self):
        self.owner.data["health"] = 50
        self.assertTrue(self.owner.stateOfEmergency())

if __name__ == "__main__":
    unittest.main()


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
