import unittest
import houseModel


class testing(unittest.TestCase):
    def test_addDrug(self):
        # @SantiagoRR2004
        a = houseModel.HouseModel()
        number = a.getDrug("cabinet")
        a.addDrug("cabinet", 3)
        self.assertEqual(a.getDrug("cabinet"), number + 3)

    def test_addDrugsCorrectly1(self):
        # @antonoterof
        control = houseModel.HouseModel()
        tester = "cabinet"
        control.setOpenStatus(tester, True)
        maximun = control.getCapacity(tester)
        initialValue = control.getDrug(tester)
        control.addDrug(tester, -initialValue)
        self.assertEqual(control.getDrug(tester), 0)
        # If we remove the drugs they are subtracted correctly

    def test_addDrugsCorrectly2(self):
        # @antonoterof
        control = houseModel.HouseModel()
        tester = "cabinet"
        control.setOpenStatus(tester, True)
        maximun = control.getCapacity(tester)
        initialValue = control.getDrug(tester)
        control.addDrug(tester, maximun - initialValue)
        self.assertEqual(control.getDrug(tester), maximun)
        # If we add drugs they are added correctly

    def test_addDrugsCorrectly3(self):
        # @antonoterof
        control = houseModel.HouseModel()
        tester = "cabinet"
        control.setOpenStatus(tester, True)
        maximun = control.getCapacity(tester)
        initialValue = control.getDrug(tester)
        control.addDrug(tester, 0)
        self.assertEqual(control.getDrug(tester), initialValue)
        # If we add nothing no changes are made

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

    def test_positionInGrid1(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        model.removeValue("cabinet")
        model.setPosition(0, 0, model.getAttributeFromDict("cabinet", "symbol"))
        self.assertEqual(
            model.getPosition(0, 0), model.getAttributeFromDict("cabinet", "symbol")
        )

    def test_positionInGrid2(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        model.removeValue("cabinet")
        model.setPosition(0, 0, model.getAttributeFromDict("cabinet", "symbol"))
        self.assertEqual(model.getPositionOf("cabinet"), [0, 0])

    def test_positionInGrid3(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        model.removeValue("cabinet")
        self.assertEqual(model.getPositionOf("cabinet"), False)
