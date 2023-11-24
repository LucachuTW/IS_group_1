import unittest
import houseEnv
import houseModel


class testing(unittest.TestCase):

    def test_createsController(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        self.assertIsInstance(control, houseEnv.HouseEnv)
        # Check that houseEnv is instantiated

    def test_addDrugs1(self):
        # @SantiagoRR2004
        # Modified by @antonoterof
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, False)
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.checkAddDrug("cabinet", maximun - initialValue), False)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # Fails because it isn't open

    def test_addDrugs2(self):
        # @SantiagoRR2004
        # Modified by @antonoterof
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, True)
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.checkAddDrug(tester, maximun - initialValue), True)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # The tester can be filled

    def test_addDrugs3(self):
        # @SantiagoRR2004
        # Modified by @antonoterof
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, True)
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(
            control.checkAddDrug(tester, maximun - initialValue + 1), False
        )
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # Overfills the tester

    def test_addDrugs4(self):
        # @SantiagoRR2004
        # Modified by @antonoterof
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, True)
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.checkAddDrug(tester, -maximun - 1), False)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # Tries to remove too many from tester

    def test_addDrugs5(self):
        # @SantiagoRR2004
        # Modified by @antonoterof
        tester = "robot"
        control = houseModel.HouseModel().getController()
        maximun = control.getModel().getCapacity(tester)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.checkAddDrug(tester, maximun - initialValue), True)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # Could fill up the tester that doesn't have attribute open without problems

    def test_addDrugs6(self):
        # @SantiagoRR2004
        # Modified by @antonoterof
        tester = "cabinet"
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus(tester, True)
        initialValue = control.getModel().getDrug(tester)
        self.assertEqual(control.checkAddDrug(tester, -initialValue), True)
        self.assertEqual(control.getModel().getDrug(tester), initialValue)
        # Empties up the tester without problems

    def test_nextToEachOther1(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            0, 1, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), True)
        # Check that the agents are nearby

    def test_nextToEachOther2(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), True)
        # Check that the agents are nearby

    def test_nextToEachOther3(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), True)
        # Check that the agents are nearby

    def test_nextToEachOther4(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(
            0, 1, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), True)
        # Check that the agents are nearby

    def test_nextToEachOther5(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            1, 1, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), False)
        # Check that the agents are nearby

    def test_nextToEachOther6(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.removeValue("cabinet")
        model.removeValue("owner")
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            0, 2, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), False)
        # Check that the agents are nearby


    def test_transferDrugs1(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "cabinet"
        reciever = "robot"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(giver, True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), True)
        self.assertEqual(control.getModel().getDrug(giver), maximun1 - 1)
        self.assertEqual(control.getModel().getDrug(reciever), 1)
        # No failures, it transfers 1 Drug

    def test_transferDrugs2(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "robot"
        reciever = "cabinet"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(reciever, True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), True)
        self.assertEqual(control.getModel().getDrug(giver), maximun1 - 1)
        self.assertEqual(control.getModel().getDrug(reciever), 1)
        # No failures, it transfers 1 Drug

    def test_transferDrugs3(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "cabinet"
        giver = "robot"
        reciever = "cabinet"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(reciever, True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), False)
        self.assertEqual(control.getModel().getDrug(giver), maximun1)
        self.assertEqual(control.getModel().getDrug(reciever), 0)
        # Fails because mover can't transfer because it can't move on it's own

    def test_transferDrugs4(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "robot"
        reciever = "cabinet"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 1, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(reciever, True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), False)
        self.assertEqual(control.getModel().getDrug(giver), maximun1)
        self.assertEqual(control.getModel().getDrug(reciever), 0)
        # Fails because they aren't adjacent

    def test_transferDrugs5(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "cabinet"
        reciever = "robot"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(giver, True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(
            control.transferDrugs(mover, giver, reciever, maximun2 + 1), False
        )
        self.assertEqual(control.getModel().getDrug(giver), maximun1)
        self.assertEqual(control.getModel().getDrug(reciever), 0)
        # Not enough space on the reciever

    def test_transferDrugs6(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "robot"
        reciever = "cabinet"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(reciever, True)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(
            control.transferDrugs(mover, giver, reciever, maximun1 + 1), False
        )
        self.assertEqual(control.getModel().getDrug(giver), maximun1)
        self.assertEqual(control.getModel().getDrug(reciever), 0)
        # Not enough drugs on the giver

    def test_transferDrugs7(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        mover = "robot"
        giver = "cabinet"
        reciever = "robot"

        model.removeValue(mover)
        model.removeValue(giver)
        model.removeValue(reciever)

        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict(giver, "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict(reciever, "symbol")
        )
        control.getModel().setOpenStatus(giver, False)

        initialValue1 = control.getModel().getDrug(giver)
        maximun1 = control.getModel().getCapacity(giver)
        initialValue2 = control.getModel().getDrug(reciever)
        maximun2 = control.getModel().getCapacity(reciever)

        control.getModel().addDrug(giver, maximun1 - initialValue1)
        control.getModel().addDrug(reciever, -initialValue2)

        self.assertEqual(control.transferDrugs(mover, giver, reciever, 1), False)
        self.assertEqual(control.getModel().getDrug(giver), maximun1)
        self.assertEqual(control.getModel().getDrug(reciever), 0)
        # Cabinet isn't open
        
    def test_checkOpeneable_true(self):
        # @Ventupentu
        env = houseEnv.HouseEnv()
        model = houseModel.HouseModel()
        model.getAttributeFromDict("door", "openeable")
        env.setModel(model)
        result = env.checkOpeneable("door")
        self.assertTrue(result)

    def test_checkOpeneable_false(self):
        # @Ventupentu
        env = houseEnv.HouseEnv()
        model = houseModel.HouseModel()
        model.getAttributeFromDict("walls", "openeable", False)
        env.setModel(model)
        result = env.checkOpeneable("window")
        self.assertFalse(result)