import unittest
import houseModel


class testing(unittest.TestCase):
    def test_addDrug(self):
        # @SantiagoRR2004
        a = houseModel.HouseModel()
        number = a.getDrug("cabinet")
        a.addDrug("cabinet", 3)
        self.assertEqual(a.getDrug("cabinet"), number + 3)

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
        status = model.getOpenStatus("cabinet")
        self.assertEqual(type(status), bool)

    def test_openCabinet(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        model.setOpenStatus("cabinet", True)
        self.assertEqual(model.getOpenStatus("cabinet"), True)

    def test_closeCabinet(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        model.setOpenStatus("cabinet", False)
        self.assertEqual(model.getOpenStatus("cabinet"), False)

    def test_getCabinetCapacity(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        number = model.getCapacity("cabinet")
        self.assertEqual(type(number), int)
