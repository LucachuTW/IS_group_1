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
