import unittest
import houseModel


class testing(unittest.TestCase):
    def test_addDrug(self):
        # @SantiagoRR2004
        a = houseModel.HouseModel()
        number = a.getDrug()
        a.addDrug(3)
        self.assertEqual(a.getDrug(), number + 3)

    def test_ChangePosition(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        oX, oY, dX, dY = 0, 0, 3, 6
        value = model.getPosition(oX, oY)
        model.changePosition(oX, oY, dX, dY)
        self.assertEqual(value, model.getPosition(dX, dY))

    def test_getCabinetStatus(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        status = model.getCabinetStatus()
        self.assertEqual(type(status), bool)

    def test_openCabinet(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        model.setCabinetStatus(True)
        self.assertEqual(model.getCabinetStatus(), True)

    def test_closeCabinet(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        model.setCabinetStatus(False)
        self.assertEqual(model.getCabinetStatus(), False)
