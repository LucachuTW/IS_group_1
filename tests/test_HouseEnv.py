import unittest
import houseEnv
import houseModel
import atexit


class helpTestController:
    """
    This class exists to help test the controller
    """

    def setUp(self):
        """
        This runs for every test at the start automatically.

        For all these tests we only need the model and controller.

        Contributors:
            - @SantiagoRR2004
        """
        self.model = houseModel.HouseModel("environmentBackup.json")
        atexit.unregister(self.model.saveToFile)
        self.control = houseEnv.HouseEnv(self.model)

    def tearDown(self):
        """
        This runs for every test at the end automatically.

        It deletes objects to free space up.
        It might not be necessary.

        Contributors:
            - @SantiagoRR2004
        """
        del self.control
        del self.model


class testController(helpTestController, unittest.TestCase):
    def test_createsController(self):
        """
        Test if the controller is created.

        This method checks if the controller is created.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        self.assertIsInstance(control, houseEnv.HouseEnv)

    def test_checkAddDrug1(self):
        """
        Test adding drugs to a cabinet when it is not open.

        This method tests the scenario where drugs are added to a cabinet when it is
        not open so it should return False.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof
        """
        tester = "cabinet"
        control = self.control
        self.model.setOpenStatus(tester, False)
        maximun = self.model.getCapacity(tester)
        initialValue = self.model.getDrug(tester)
        self.assertFalse(control.checkAddDrug("cabinet", maximun - initialValue))
        self.assertEqual(self.model.getDrug(tester), initialValue)

    def test_checkAddDrug2(self):
        """
        Test adding drugs to a cabinet when it is open.

        This method tests the scenario where drugs are added to a
        cabinet when it is open. No problems arise so it returns True
        and the number doesn't change.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof
        """
        tester = "cabinet"
        control = self.control
        self.model.setOpenStatus(tester, True)
        maximun = self.model.getCapacity(tester)
        initialValue = self.model.getDrug(tester)
        self.assertTrue(control.checkAddDrug(tester, maximun - initialValue))
        self.assertEqual(self.model.getDrug(tester), initialValue)

    def test_checkAddDrug3(self):
        """
        Test adding drugs to a cabinet to overfill it.

        This method tests the scenario where drugs are added
        to a cabinet to overfill it. It returns False and the
        value stays constant.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof
        """
        tester = "cabinet"
        control = self.control
        self.model.setOpenStatus(tester, True)
        maximun = self.model.getCapacity(tester)
        initialValue = self.model.getDrug(tester)
        self.assertFalse(control.checkAddDrug(tester, maximun - initialValue + 1))
        self.assertEqual(self.model.getDrug(tester), initialValue)

    def test_checkAddDrug4(self):
        """
        Test adding too many negative drugs to a cabinet.

        This method tests the scenario where negative drugs are added to a cabinet
        in excess. It returnd False and the value stays the same.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof
        """
        tester = "cabinet"
        control = self.control
        self.model.setOpenStatus(tester, True)
        maximun = self.model.getCapacity(tester)
        initialValue = self.model.getDrug(tester)
        self.assertFalse(control.checkAddDrug(tester, -maximun - 1))
        self.assertEqual(self.model.getDrug(tester), initialValue)

    def test_checkAddDrug5(self):
        """
        Test adding drugs to a robot.

        This method tests the scenario where drugs are added to a robot
        until it's maxed. This works because the robot can carry
        drugs. This is a special case because robot doesn't
        have the attribute open.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof
        """
        tester = "robot"
        control = self.control
        maximun = self.model.getCapacity(tester)
        self.model.getAttribute(tester).pop("open", None)
        initialValue = self.model.getDrug(tester)
        self.assertTrue(control.checkAddDrug(tester, maximun - initialValue))
        self.assertEqual(self.model.getDrug(tester), initialValue)

    def test_checkAddDrug6(self):
        """
        Test removing drugs from a cabinet.

        This method tests the scenario where drugs are removed from a cabinet
        until it has cero. It returns True and the value doesn't change.

        Contributors:
            - @SantiagoRR2004
            - @antonoterof
        """
        tester = "cabinet"
        control = self.control
        self.model.setOpenStatus(tester, True)
        initialValue = self.model.getDrug(tester)
        self.assertTrue(control.checkAddDrug(tester, -initialValue))
        self.assertEqual(self.model.getDrug(tester), initialValue)

    def test_checkAddDrug7(self):
        """
        Test adding strings to a cabinet.

        This method tests the scenario where a string is added to a cabinet.
        The result is False.

        Contributors:
            - @antonoterof
        """
        tester = "cabinet"
        control = self.control
        self.model.setOpenStatus(tester, True)
        initialValue = self.model.getDrug(tester)
        self.assertFalse(control.checkAddDrug(tester, "String"))
        self.assertEqual(self.model.getDrug(tester), initialValue)

    def test_checkAddDrug8(self):
        """
        Test adding strings to a agent (robot).

        This method tests the scenario where a string is added to an agent.

        Contributors:
            - @antonoterof
        """
        tester = "robot"
        control = self.control
        initialValue = self.model.getDrug(tester)
        self.assertFalse(control.checkAddDrug(tester, "String"))
        self.assertEqual(self.model.getDrug(tester), initialValue)

    def test_areAdjacent1(self):
        """
        This method tests if two agents are next
        to each other in the house model when one is below
        at a distance of one unit.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(0, 0, self.model.getAttributeFromDict("cabinet", "symbol"))
        model.setPosition(0, 1, self.model.getAttributeFromDict("owner", "symbol"))
        self.assertTrue(control.areAdjacent("cabinet", "owner"))

    def test_areAdjacent2(self):
        """
        Test if two agents are next to each other.

        This method tests if two agents are next to
        each other in the house model when one is to the right
        at a distance of one unit.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(0, 0, self.model.getAttributeFromDict("cabinet", "symbol"))
        model.setPosition(1, 0, self.model.getAttributeFromDict("owner", "symbol"))
        self.assertTrue(control.areAdjacent("cabinet", "owner"))

    def test_areAdjacent3(self):
        """
        Test if two agents are next to each other.

        This method tests if two agents are next to
        each other in the house model when one is on top
        at a distance of one unit.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(1, 0, self.model.getAttributeFromDict("cabinet", "symbol"))
        model.setPosition(0, 0, self.model.getAttributeFromDict("owner", "symbol"))
        self.assertTrue(control.areAdjacent("cabinet", "owner"))

    def test_areAdjacent4(self):
        """
        Test if two agents are next to each other.

        This method tests if two agents are next to
        each other in the house model when one is to the left
        at a distance of one unit.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(0, 1, self.model.getAttributeFromDict("cabinet", "symbol"))
        model.setPosition(0, 0, self.model.getAttributeFromDict("owner", "symbol"))
        self.assertTrue(control.areAdjacent("cabinet", "owner"))

    def test_areAdjacent5(self):
        """
        This method tests if two agents are
        diagonally from each other. This means they are not
        next to each other.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(0, 0, self.model.getAttributeFromDict("cabinet", "symbol"))
        model.setPosition(1, 1, self.model.getAttributeFromDict("owner", "symbol"))
        self.assertFalse(control.areAdjacent("cabinet", "owner"))

    def test_areAdjacent6(self):
        """
        This method tests if two agents are at a distance
        of 2 units horizontally. This means they are not
        next to each other.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(0, 0, self.model.getAttributeFromDict("cabinet", "symbol"))
        model.setPosition(0, 2, self.model.getAttributeFromDict("owner", "symbol"))
        self.assertFalse(control.areAdjacent("cabinet", "owner"))

    def test_areAdjacent7(self):
        """
        This method tests if two agents are next
        to each other in the house model if one on
        the other side.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(0, 0, self.model.getAttributeFromDict("cabinet", "symbol"))
        model.setPosition(0, -1, self.model.getAttributeFromDict("owner", "symbol"))
        self.assertFalse(control.areAdjacent("cabinet", "owner"))

    def test_areAdjacent8(self):
        """
        This method tests if two agents are next
        to each other in the house model if one on
        the other side by giving negative coordinates
        that appear to be one unit away.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(0, 0, self.model.getAttributeFromDict("cabinet", "symbol"))
        model.setPosition(0, -1, self.model.getAttributeFromDict("owner", "symbol"))
        self.assertFalse(control.areAdjacent("cabinet", "owner", [0, 0], [0, -1]))

    def test_areAdjacent9(self):
        """
        This method tests if two agents are next
        to each other in the house model if both have negative
        coordinates but are next to each other.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(-2, -3, self.model.getAttributeFromDict("cabinet", "symbol"))
        model.setPosition(-2, -2, self.model.getAttributeFromDict("owner", "symbol"))
        self.assertTrue(control.areAdjacent("cabinet", "owner", [-2, -3], [-2, -2]))

    def test_areAdjacent10(self):
        """
        This method tests if two agents are next
        to each other in the house model if both have negative
        coordinates but are next to each other.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(-2, -3, self.model.getAttributeFromDict("cabinet", "symbol"))
        model.setPosition(-2, -2, self.model.getAttributeFromDict("owner", "symbol"))
        self.assertTrue(control.areAdjacent("cabinet", "owner"))

    def test_transferDrugs1(self):
        """
        This method tests the scenario where drugs are transferred from the cabinet to one agent.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        giver = "cabinet"
        reciever = "robot"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(0, 0, self.model.getAttributeFromDict(giver, "symbol"))
        model.setPosition(1, 0, self.model.getAttributeFromDict(reciever, "symbol"))
        self.model.setOpenStatus(giver, True)

        initialValue1 = self.model.getDrug(giver)
        maximun1 = self.model.getCapacity(giver)
        initialValue2 = self.model.getDrug(reciever)
        maximun2 = self.model.getCapacity(reciever)

        self.model.addDrug(giver, maximun1 - initialValue1)
        self.model.addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), True)
        self.assertEqual(self.model.getDrug(giver), maximun1 - 1)
        self.assertEqual(self.model.getDrug(reciever), 1)

    def test_transferDrugs2(self):
        """
        This method tests the scenario where drugs are transferred from one agent to the cabinet.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        giver = "robot"
        reciever = "cabinet"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(0, 0, self.model.getAttributeFromDict(giver, "symbol"))
        model.setPosition(1, 0, self.model.getAttributeFromDict(reciever, "symbol"))
        self.model.setOpenStatus(reciever, True)

        initialValue1 = self.model.getDrug(giver)
        maximun1 = self.model.getCapacity(giver)
        initialValue2 = self.model.getDrug(reciever)
        maximun2 = self.model.getCapacity(reciever)

        self.model.addDrug(giver, maximun1 - initialValue1)
        self.model.addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), True)
        self.assertEqual(self.model.getDrug(giver), maximun1 - 1)
        self.assertEqual(self.model.getDrug(reciever), 1)

    def test_transferDrugs3(self):
        """
        This method tests the scenario where drugs are transferred from the cabinet to one agent.
        Fails because the motor can't be transferred because it can't move on its own.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "cabinet"
        giver = "robot"
        reciever = "cabinet"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(0, 0, self.model.getAttributeFromDict(giver, "symbol"))
        model.setPosition(1, 0, self.model.getAttributeFromDict(reciever, "symbol"))
        self.model.setOpenStatus(reciever, True)

        initialValue1 = self.model.getDrug(giver)
        maximun1 = self.model.getCapacity(giver)
        initialValue2 = self.model.getDrug(reciever)
        maximun2 = self.model.getCapacity(reciever)

        self.model.addDrug(giver, maximun1 - initialValue1)
        self.model.addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), False)
        self.assertEqual(self.model.getDrug(giver), maximun1)
        self.assertEqual(self.model.getDrug(reciever), 0)

    def test_transferDrugs4(self):
        """
        This method tests the scenario where drugs are transferred from one agent to the cabinet.
        Fails because they aren't adjacent.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        giver = "robot"
        reciever = "cabinet"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(0, 0, self.model.getAttributeFromDict(giver, "symbol"))
        model.setPosition(1, 1, self.model.getAttributeFromDict(reciever, "symbol"))
        self.model.setOpenStatus(reciever, True)

        initialValue1 = self.model.getDrug(giver)
        maximun1 = self.model.getCapacity(giver)
        initialValue2 = self.model.getDrug(reciever)
        maximun2 = self.model.getCapacity(reciever)

        self.model.addDrug(giver, maximun1 - initialValue1)
        self.model.addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), False)
        self.assertEqual(self.model.getDrug(giver), maximun1)
        self.assertEqual(self.model.getDrug(reciever), 0)

    def test_transferDrugs5(self):
        """
        This method tests the scenario where drugs are transferred from the cabinet to one agent.
        Fails because it isn't enough space on the reciever.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        giver = "cabinet"
        reciever = "robot"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(0, 0, self.model.getAttributeFromDict(giver, "symbol"))
        model.setPosition(1, 0, self.model.getAttributeFromDict(reciever, "symbol"))
        self.model.setOpenStatus(giver, True)

        initialValue1 = self.model.getDrug(giver)
        maximun1 = self.model.getCapacity(giver)
        initialValue2 = self.model.getDrug(reciever)
        maximun2 = self.model.getCapacity(reciever)

        self.model.addDrug(giver, maximun1 - initialValue1)
        self.model.addDrug(reciever, -initialValue2)

        self.assertEqual(
            control.transferDrugs(mover, giver, reciever, maximun2 + 1), False
        )
        self.assertEqual(self.model.getDrug(giver), maximun1)
        self.assertEqual(self.model.getDrug(reciever), 0)

    def test_transferDrugs6(self):
        """
        This method tests the scenario where drugs are transferred from one agent to the cabinet.
        Fails because it isn't enough drugs on the giver.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        giver = "robot"
        reciever = "cabinet"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(0, 0, self.model.getAttributeFromDict(giver, "symbol"))
        model.setPosition(1, 0, self.model.getAttributeFromDict(reciever, "symbol"))
        self.model.setOpenStatus(reciever, True)

        initialValue1 = self.model.getDrug(giver)
        maximun1 = self.model.getCapacity(giver)
        initialValue2 = self.model.getDrug(reciever)
        maximun2 = self.model.getCapacity(reciever)

        self.model.addDrug(giver, maximun1 - initialValue1)
        self.model.addDrug(reciever, -initialValue2)

        self.assertEqual(
            control.transferDrugs(mover, giver, reciever, maximun1 + 1), False
        )
        self.assertEqual(self.model.getDrug(giver), maximun1)
        self.assertEqual(self.model.getDrug(reciever), 0)

    def test_transferDrugs7(self):
        """
        This method tests the scenario where drugs are transferred from the cabinet to one agent.
        Fails because cabinet isn't open.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        giver = "cabinet"
        reciever = "robot"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(0, 0, self.model.getAttributeFromDict(giver, "symbol"))
        model.setPosition(1, 0, self.model.getAttributeFromDict(reciever, "symbol"))
        self.model.setOpenStatus(giver, False)

        initialValue1 = self.model.getDrug(giver)
        maximun1 = self.model.getCapacity(giver)
        initialValue2 = self.model.getDrug(reciever)
        maximun2 = self.model.getCapacity(reciever)

        self.model.addDrug(giver, maximun1 - initialValue1)
        self.model.addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), False)
        self.assertEqual(self.model.getDrug(giver), maximun1)
        self.assertEqual(self.model.getDrug(reciever), 0)

    def test_checkOpeneable1(self):
        """
        It is ensure that the method returns a Boolean value.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu
        """
        control = self.control
        self.assertIsInstance(control.checkOpeneable("door"), bool)

    def test_checkOpeneable2(self):
        """
        It is ensure that the method works correctly.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu
        """
        control = self.control
        element = "cabinet"
        open = self.model.getAttributeFromDict(element, "openable")
        self.assertEqual(control.checkOpeneable(element), open)

    def test_checkIfShareable1(self):
        """
        It is ensure that the method works correctly.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        element = "cabinet"

        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", True)

        self.assertEqual(control.checkIfShareable(element), True)

    def test_checkIfShareable2(self):
        """
        It is ensure that the method works correctly.
        The object can not share space because it is openable and not is open.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        element = "cabinet"

        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", False)

        self.assertEqual(control.checkIfShareable(element), False)

    def test_checkIfShareable3(self):
        """
        It is ensure that the method works correctly.
        The object can share space because it is semisolid and not openable.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        element = "cabinet"

        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", False)

        booleans = [True, False]
        for dontCareIfOpen in booleans:
            model.setAttributeFromDict(element, "open", dontCareIfOpen)
            self.assertEqual(control.checkIfShareable(element), True)

    def test_checkIfShareable4(self):
        """
        It is ensure that the method works correctly.
        The object can not share space because it is not semisolid.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        element = "cabinet"

        model.setAttributeFromDict(element, "semisolid", False)

        booleans = [True, False]
        for dontCareIfOpenable in booleans:
            model.setAttributeFromDict(element, "openable", dontCareIfOpenable)
            for dontCareIfOpen in booleans:
                model.setAttributeFromDict(element, "open", dontCareIfOpen)
                self.assertEqual(control.checkIfShareable(element), False)

    def test_checkIfMovableTo1(self):
        """
        It is ensure that the method works correctly.
        The agent can move to the position (0,0) because it is empty.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        model.setPosition(0, 0, 0)
        self.assertEqual(control.checkIfMovableTo(0, 0), True)

    def test_checkIfMovableTo2(self):
        """
        It is ensure that the method works correctly.
        The agent cannot move to position (0,0) because a prime number is formed

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        model.setPosition(0, 0, 6)
        self.assertEqual(control.checkIfMovableTo(0, 0), False)

    def test_checkIfMovableTo3(self):
        """
        It is ensure that the method works correctly.
        The agent can move to position (0,0) because object is semisolid, openable and it is open.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)
        model.setPosition(0, 0, elementSymbol)

        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", True)

        self.assertEqual(control.checkIfMovableTo(0, 0), True)

    def test_checkIfMovableTo4(self):
        """
        It is ensure that the method works correctly.
        The agent can move to position (0,0) because object is semisolid, and no openable .

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)
        model.setPosition(0, 0, elementSymbol)

        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", False)

        booleans = [True, False]
        for dontCareIfOpen in booleans:
            model.setAttributeFromDict(element, "open", dontCareIfOpen)
            self.assertEqual(control.checkIfMovableTo(0, 0), True)

    def test_checkIfMovableTo5(self):
        """
        It is ensure that the method works correctly.
        The agent can not move to position (0,0) because object is not semisolid.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)
        model.setPosition(0, 0, elementSymbol)

        model.setAttributeFromDict(element, "semisolid", False)

        booleans = [True, False]
        for dontCareIfOpenable in booleans:
            model.setAttributeFromDict(element, "openable", dontCareIfOpenable)
            for dontCareIfOpen in booleans:
                model.setAttributeFromDict(element, "open", dontCareIfOpen)
                self.assertEqual(control.checkIfMovableTo(0, 0), False)

    def test_checkIfMovableTo6(self):
        """
        It is ensure that the method works correctly.
        The agent can not move to position (0,0) because object is semisolid, openable and it is no open.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)
        model.setPosition(0, 0, elementSymbol)

        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", False)

        self.assertEqual(control.checkIfMovableTo(0, 0), False)

    def test_moveTo1(self):
        """
        It is ensure that the method works correctly.
        The agent can move to position (1,0) without problems.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 0, moverSymbol)
        model.setPosition(1, 0, 0)

        self.assertEqual(control.moveTo(mover, moved, 1, 0), True)
        self.assertEqual(model.getPosition(0, 0), 0)
        self.assertEqual(model.getPosition(1, 0), moverSymbol)

    def test_moveTo2(self):
        """
        It is ensure that the method works correctly.
        The agent can move to position (1,0) because the object that is in that position is semisolid and no openable.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        model.getAttributeFromDict(mover, "moving")["mover"] = False
        model.getAttributeFromDict(mover, "moving")["moved"] = False
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover
        model.setAttributeFromDict(moved, "semisolid", True)
        model.setAttributeFromDict(moved, "openable", False)

        model.removeValue(mover)

        model.setPosition(1, 0, moverSymbol)

        self.assertEqual(control.moveTo(mover, moved, 1, 0), True)
        self.assertEqual(model.getPosition(1, 0), moverSymbol)

    def test_moveTo3(self):
        """
        It is ensure that the method works correctly.
        The agent can move to position (0,1) without problems.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 0, moverSymbol)
        model.setPosition(0, 1, 0)

        self.assertEqual(control.moveTo(mover, moved, 0, 1), True)
        self.assertEqual(model.getPosition(0, 0), 0)
        self.assertEqual(model.getPosition(0, 1), moverSymbol)

    def test_moveTo4(self):
        """
        It is ensure that the method works correctly.
        The agent can move to position (0,0) without problems.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(1, 0, moverSymbol)
        model.setPosition(0, 0, 0)

        self.assertEqual(control.moveTo(mover, moved, 0, 0), True)
        self.assertEqual(model.getPosition(1, 0), 0)
        self.assertEqual(model.getPosition(0, 0), moverSymbol)

    def test_moveTo5(self):
        """
        It is ensure that the method works correctly.
        The agent can be returned to position (0,0) without problems.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 1, moverSymbol)
        model.setPosition(0, 0, 0)

        self.assertEqual(control.moveTo(mover, moved, 0, 0), True)
        self.assertEqual(model.getPosition(0, 1), 0)
        self.assertEqual(model.getPosition(0, 0), moverSymbol)

    def test_moveTo6(self):
        """
        It is ensure that the method works correctly.
        The agent can not move diagonally.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 0, moverSymbol)
        model.setPosition(1, 1, 0)

        self.assertEqual(control.moveTo(mover, moved, 1, 1), False)
        self.assertEqual(model.getPosition(0, 0), moverSymbol)
        self.assertEqual(model.getPosition(1, 1), 0)

    def test_moveTo7(self):
        """
        It is ensure that the method works correctly.
        The agent can not move to far away.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 0, moverSymbol)
        model.setPosition(2, 2, 0)

        self.assertEqual(control.moveTo(mover, moved, 2, 2), False)
        self.assertEqual(model.getPosition(0, 0), moverSymbol)
        self.assertEqual(model.getPosition(2, 2), 0)

    def test_moveTo8(self):
        """
        It is ensure that the method works correctly.
        The agent can not move itself.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = False
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 0, moverSymbol)
        model.setPosition(1, 0, 0)

        self.assertEqual(control.moveTo(mover, moved, 1, 0), False)
        self.assertEqual(model.getPosition(0, 0), moverSymbol)
        self.assertEqual(model.getPosition(1, 0), 0)

    def test_moveTo9(self):
        """
        It is ensure that the method works correctly.
        The agent can not move to position that is occupied by 2 other objects.

        Contributors:
            - @SantiagoRR2004
            - @Ventupentu
        """
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = mover

        model.removeValue(mover)

        model.setPosition(0, 0, moverSymbol)
        model.setPosition(1, 0, 6)

        self.assertEqual(control.moveTo(mover, moved, 1, 0), False)
        self.assertEqual(model.getPosition(0, 0), moverSymbol)
        self.assertEqual(model.getPosition(1, 0), 6)

    def test_moveTo10(self):
        """
        It is ensure that the method works correctly.
        The agent can move the object without problems.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = False
        model.getAttributeFromDict(mover, "moving")["mover"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = "cabinet"
        model.getAttributeFromDict(moved, "moving")["auto"] = False
        model.getAttributeFromDict(moved, "moving")["moved"] = True
        movedSymbol = model.getAttributeFromDict(moved, "symbol")

        model.removeValue(mover)
        model.removeValue(moved)

        model.setPosition(0, 0, movedSymbol)
        model.setPosition(0, 1, moverSymbol)
        model.setPosition(1, 0, 0)

        self.assertEqual(control.moveTo(mover, moved, 1, 0), True)
        self.assertEqual(model.getPosition(0, 0), 0)
        self.assertEqual(model.getPosition(1, 0), movedSymbol)
        self.assertEqual(model.getPosition(0, 1), moverSymbol)

    def test_moveTo11(self):
        """
        It is ensure that the method works correctly.
        The agent can not move the object because mover and moved need to be adjacent.

        Contributors:
            - @SantiagoRR2004
        """
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = False
        model.getAttributeFromDict(mover, "moving")["mover"] = True
        moverSymbol = model.getAttributeFromDict(mover, "symbol")
        moved = "cabinet"
        model.getAttributeFromDict(moved, "moving")["auto"] = False
        model.getAttributeFromDict(moved, "moving")["moved"] = True
        movedSymbol = model.getAttributeFromDict(moved, "symbol")

        model.removeValue(mover)
        model.removeValue(moved)

        model.setPosition(0, 0, movedSymbol)
        model.setPosition(0, 2, moverSymbol)
        model.setPosition(1, 0, 0)

        self.assertEqual(control.moveTo(mover, moved, 1, 0), False)
        self.assertEqual(model.getPosition(0, 0), movedSymbol)
        self.assertEqual(model.getPosition(1, 0), 0)
        self.assertEqual(model.getPosition(0, 2), moverSymbol)

    def test_moveTo12(self):
        # @SantiagoRR2004
        # No problem
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moved = mover
        model.setAttributeFromDict(moved, "semisolid", True)
        model.setAttributeFromDict(moved, "openable", True)
        model.setAttributeFromDict(moved, "open", True)
        movedSymbol = model.getAttributeFromDict(moved, "symbol")
        model.removeValue(mover)

        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)
        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", True)

        model.setPosition(0, 0, movedSymbol)
        model.setPosition(1, 0, elementSymbol)

        self.assertEqual(control.moveTo(mover, moved, 1, 0), True)
        self.assertEqual(model.getPosition(0, 0), 0)
        self.assertEqual(model.getPosition(1, 0), movedSymbol * elementSymbol)

    def test_moveTo13(self):
        # @SantiagoRR2004
        # No problem
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moved = mover
        model.setAttributeFromDict(moved, "semisolid", True)
        model.setAttributeFromDict(moved, "openable", True)
        model.setAttributeFromDict(moved, "open", True)
        movedSymbol = model.getAttributeFromDict(moved, "symbol")
        model.removeValue(mover)

        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)
        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", True)

        model.setPosition(1, 0, movedSymbol)
        model.setPosition(2, 0, elementSymbol)

        self.assertEqual(control.moveTo(mover, moved, 2, 0), True)
        self.assertEqual(model.getPosition(1, 0), 0)
        self.assertEqual(model.getPosition(2, 0), movedSymbol * elementSymbol)

    def test_moveTo14(self):
        # @SantiagoRR2004
        # Other item isn't open so it doesn't work
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moved = mover
        model.setAttributeFromDict(moved, "semisolid", True)
        model.setAttributeFromDict(moved, "openable", False)
        movedSymbol = model.getAttributeFromDict(moved, "symbol")
        model.removeValue(mover)

        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)
        model.setAttributeFromDict(element, "semisolid", True)
        model.setAttributeFromDict(element, "openable", True)
        model.setAttributeFromDict(element, "open", False)

        model.setPosition(0, 0, movedSymbol)
        model.setPosition(1, 0, elementSymbol)

        booleans = [True, False]
        for dontCareIfOpen in booleans:
            model.setAttributeFromDict(moved, "open", dontCareIfOpen)
            self.assertEqual(control.moveTo(mover, moved, 1, 0), False)
            self.assertEqual(model.getPosition(0, 0), movedSymbol)
            self.assertEqual(model.getPosition(1, 0), elementSymbol)

    def test_moveTo15(self):
        # @SantiagoRR2004
        # Other item can't share space with each other
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moved = mover
        movedSymbol = model.getAttributeFromDict(moved, "symbol")
        model.removeValue(mover)

        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)
        model.setAttributeFromDict(element, "semisolid", False)

        model.setPosition(0, 0, movedSymbol)
        model.setPosition(1, 0, elementSymbol)

        booleans = [True, False]
        for dontCareIfSemisolidOfMoved in booleans:
            model.setAttributeFromDict(moved, "semisolid", dontCareIfSemisolidOfMoved)
            for dontCareIfOpenableOfMoved in booleans:
                model.setAttributeFromDict(moved, "openable", dontCareIfOpenableOfMoved)
                for dontCareIfOpenOfMoved in booleans:
                    model.setAttributeFromDict(moved, "open", dontCareIfOpenOfMoved)
                    for dontCareIfOpenableOfElement in booleans:
                        model.setAttributeFromDict(
                            element, "openable", dontCareIfOpenableOfElement
                        )
                        for dontCareIfOpenOfElement in booleans:
                            model.setAttributeFromDict(
                                element, "open", dontCareIfOpenOfElement
                            )
                            self.assertEqual(control.moveTo(mover, moved, 1, 0), False)
                            self.assertEqual(model.getPosition(0, 0), movedSymbol)
                            self.assertEqual(model.getPosition(1, 0), elementSymbol)

    def test_moveTo16(self):
        # @SantiagoRR2004
        # No problem moving out of another element
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moved = mover
        movedSymbol = model.getAttributeFromDict(moved, "symbol")
        model.removeValue(mover)

        element = "cabinet"
        elementSymbol = model.getAttributeFromDict(element, "symbol")
        model.removeValue(element)

        model.setPosition(0, 0, movedSymbol * elementSymbol)
        model.setPosition(1, 0, 0)

        booleans = [True, False]
        for dontCareIfSemisolidOfMoved in booleans:
            model.setAttributeFromDict(moved, "semisolid", dontCareIfSemisolidOfMoved)
            for dontCareIfOpenableOfMoved in booleans:
                model.setAttributeFromDict(moved, "openable", dontCareIfOpenableOfMoved)
                for dontCareIfOpenOfMoved in booleans:
                    model.setAttributeFromDict(moved, "open", dontCareIfOpenOfMoved)
                    for dontCareIfSemisolidOfElement in booleans:
                        model.setAttributeFromDict(
                            element, "semisolid", dontCareIfSemisolidOfElement
                        )
                        for dontCareIfOpenableOfElement in booleans:
                            model.setAttributeFromDict(
                                element, "openable", dontCareIfOpenableOfElement
                            )
                            for dontCareIfOpenOfElement in booleans:
                                model.setAttributeFromDict(
                                    element, "open", dontCareIfOpenOfElement
                                )

                                model.setPosition(0, 0, movedSymbol * elementSymbol)
                                model.setPosition(1, 0, 0)

                                self.assertEqual(
                                    control.moveTo(mover, moved, 1, 0), True
                                )
                                self.assertEqual(model.getPosition(0, 0), elementSymbol)
                                self.assertEqual(model.getPosition(1, 0), movedSymbol)

    def test_moveMultipleTimes(self):
        control = self.control
        model = self.model
        mover = "robot"
        model.getAttributeFromDict(mover, "moving")["auto"] = True
        moved = mover
        movedSymbol = model.getAttributeFromDict(moved, "symbol")
        model.removeValue(mover)

        model.setPosition(0, 0, movedSymbol)
        coordinates = [1, 2, 3]
        for i in coordinates:
            model.setPosition(i, 0, 0)

        for i in coordinates:
            self.assertEqual(control.moveTo(mover, moved, i, 0), True)
            self.assertEqual(model.getPosition(i - 1, 0), 0)
            self.assertEqual(model.getPosition(i, 0), movedSymbol)
