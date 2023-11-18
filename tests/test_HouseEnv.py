import unittest
import houseEnv
import houseModel


class testing(unittest.TestCase):
    def test_createsController(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        self.assertIsInstance(control, houseEnv.HouseEnv)

    def test_cabinetClosed(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus("cabinet", False)
        self.assertEqual(control.addDrug("cabinet", 5), False)

    def test_cabinetOpen(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus("cabinet", True)
        self.assertEqual(control.addDrug("cabinet", 5), True)

    def test_nextToEachOther1(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.remove("cabinet")
        model.remove("owner")
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            0, 1, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), True)

    def test_nextToEachOther2(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.remove("cabinet")
        model.remove("owner")
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), True)

    def test_nextToEachOther3(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.remove("cabinet")
        model.remove("owner")
        model.setPosition(
            1, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), True)

    def test_nextToEachOther4(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.remove("cabinet")
        model.remove("owner")
        model.setPosition(
            0, 1, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), True)

    def test_nextToEachOther5(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.remove("cabinet")
        model.remove("owner")
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            1, 1, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), False)

    def test_nextToEachOther6(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        model = control.getModel()
        model.remove("cabinet")
        model.remove("owner")
        model.setPosition(
            0, 0, control.getModel().getAttributeFromDict("cabinet", "symbol")
        )
        model.setPosition(
            0, 2, control.getModel().getAttributeFromDict("owner", "symbol")
        )
        self.assertEqual(control.areAdjacent("cabinet", "owner"), False)

    def test_removeDrugsCorrectly(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus("cabinet", True)
        initialValue = control.getModel().getDrug("cabinet")
        maximun = control.getModel().getCapacity("cabinet")
        control.getModel().addDrug("cabinet", maximun - initialValue)
        self.assertEqual(control.removeDrug(maximun - 1), True)
        self.assertEqual(control.getModel().getDrug("cabinet"), 1)
