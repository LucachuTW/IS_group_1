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

    def test_removeDrugsCorrectly(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        control.getModel().setOpenStatus("cabinet", True)
        initialValue = control.getModel().getDrug("cabinet")
        maximun = control.getModel().getCapacity("cabinet")
        control.getModel().addDrug("cabinet", maximun - initialValue)
        self.assertEqual(control.removeDrug(maximun - 1), True)
        self.assertEqual(control.getModel().getDrug("cabinet"), 1)
