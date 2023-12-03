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
        # Check the status of the cabinet

    def test_openCabinet(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        model.setOpenStatus("cabinet", True)
        self.assertEqual(model.getOpenStatus("cabinet"), True)
        # Check that the cabinet can be opened

    def test_closeCabinet(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        model.setOpenStatus("cabinet", False)
        self.assertEqual(model.getOpenStatus("cabinet"), False)
        # Check that the cabinet can be closed

    def test_getCabinetCapacity(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        number = model.getCapacity("cabinet")
        self.assertEqual(type(number), int)
        # Check that the capacity can be accesed

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

    def test_checkIfPrime(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        numbers = {
            1: False,
            2: True,
            3: True,
            4: False,
            5: True,
            39: False,
            193: True,
            99: False,
        }
        for key, value in numbers.items():
            self.assertEqual(model.checkIfPrime(key), value)

    def test_checkPrimeFactorization(self):
        # @SantiagoRR2004
        model = houseModel.HouseModel()
        numbers = {
            2: [2],
            3: [3],
            4: [2, 2],
            5: [5],
            6: [2, 3],
            10: [2, 5],
            35: [5, 7],
            77: [7, 11],
        }
        for key, value in numbers.items():
            self.assertEqual(model.PrimeFactorization(key), value)

    def test_checkIfElementsAreValid(self):
        """
        We test if all the elements in the grid are valid

        Contributors:
            - @antonvm2004
            - @antonoterof
            - @SantiagoRR2004
        """
        model = houseModel.HouseModel()
        grid = model.getAttribute("grid")

        # Allowed elements in the list
        allowed_elements = [x for x in model.getAttribute("Symbols").values()]

        # We add the values that two objects share the same spot
        for i in range(len(allowed_elements)):
            for j in range(i + 1, len(allowed_elements)):
                allowed_elements.append(allowed_elements[i] * allowed_elements[j])
 
        allowed_elements.append(0)

        self.assertTrue(
            all(
                element in allowed_elements
                for inner_list in grid
                for element in inner_list
            )
        )
