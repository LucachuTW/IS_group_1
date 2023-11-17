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
        control.getModel().setCabinetStatus(False)
        self.assertEqual(control.addDrug(5), False)

    def test_cabinetOpen(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        control.getModel().setCabinetStatus(True)
        self.assertEqual(control.addDrug(5), True)

    def test_removeDrugsCorrectly(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        control.getModel().setCabinetStatus(True)
        initialValue = control.getModel().getDrug()
        maximun = control.getModel().getCabinetCapacity()
        control.getModel().setDrug(maximun - initialValue)
        self.assertEqual(control.removeDrug(maximun - 1), True)
        self.assertEqual(control.getModel().getDrug(), 1)
