import unittest
import houseModel


class testing(unittest.TestCase):
    def test_addDrug(self):
        """
        Test if the drug can be added.

        This method checks if a specified quantity of drug can be added to a specified element in the model.

        Contributors:
            - @SantiagoRR2004
        """
        control = houseModel.HouseModel()
        number = control.getDrug("cabinet")
        control.addDrug("cabinet", 3)
        self.assertEqual(control.getDrug("cabinet"), number + 3)

    def test_addDrugsCorrectly1(self):
        """
        Test if drugs can be subtracted correctly.

        This method checks if drugs can be subtracted correctly from a specified element in the model.

        Contributors:
            - @antonoterof
        """
        control = houseModel.HouseModel()
        tester = "cabinet"
        control.setOpenStatus(tester, True)
        maximun = control.getCapacity(tester)
        initialValue = control.getDrug(tester)
        control.addDrug(tester, -initialValue)
        self.assertEqual(control.getDrug(tester), 0)

    def test_addDrugsCorrectly2(self):
        """
        Test if drugs can be added correctly.

        This method checks if drugs can be added correctly to a specified element in the model.

        Contributors:
            - @antonoterof
        """
        control = houseModel.HouseModel()
        tester = "cabinet"
        control.setOpenStatus(tester, True)
        maximun = control.getCapacity(tester)
        initialValue = control.getDrug(tester)
        control.addDrug(tester, maximun - initialValue)
        self.assertEqual(control.getDrug(tester), maximun)

    def test_addDrugsCorrectly3(self):
        """
        Test if no changes are made when adding nothing.

        This method checks if no changes are made to a specified element in the model when adding nothing.

        Contributors:
            - @antonoterof
        """
        control = houseModel.HouseModel()
        tester = "cabinet"
        control.setOpenStatus(tester, True)
        maximun = control.getCapacity(tester)
        initialValue = control.getDrug(tester)
        control.addDrug(tester, 0)
        self.assertEqual(control.getDrug(tester), initialValue)

    def test_ChangePosition(self):
        """
        Test if position can be changed correctly.

        This method checks if the position of an element in the model can be changed correctly.

        Contributors:
            - @SantiagoRR2004
        """
        model = houseModel.HouseModel()
        oX, oY, dX, dY = 0, 0, 3, 6
        value = model.getPosition(oX, oY)
        model.changePosition(oX, oY, dX, dY)
        self.assertEqual(value, model.getPosition(dX, dY))

    def test_getCabinetStatus(self):
        """
        Test if the status of the cabinet can be accessed correctly.

        This method checks if the status of the cabinet in the model can be accessed correctly.

        Contributors:
            - @SantiagoRR2004
        """
        model = houseModel.HouseModel()
        status = model.getOpenStatus("cabinet")
        self.assertEqual(type(status), bool)

    def test_openCabinet(self):
        """
        Test if the cabinet can be opened correctly.

        This method checks if the cabinet in the model can be opened correctly.

        Contributors:
            - @SantiagoRR2004
        """
        model = houseModel.HouseModel()
        model.setOpenStatus("cabinet", True)
        self.assertEqual(model.getOpenStatus("cabinet"), True)

    def test_closeCabinet(self):
        """
        Test if the cabinet can be closed correctly.

        This method checks if the cabinet in the model can be closed correctly.

        Contributors:
            - @SantiagoRR2004
        """
        model = houseModel.HouseModel()
        model.setOpenStatus("cabinet", False)
        self.assertEqual(model.getOpenStatus("cabinet"), False)

    def test_getCabinetCapacity(self):
        """
        Test if the capacity of the cabinet can be accessed correctly.

        This method checks if the capacity of the cabinet in the model can be accessed correctly.

        Contributors:
            - @SantiagoRR2004
        """
        model = houseModel.HouseModel()
        number = model.getCapacity("cabinet")
        self.assertEqual(type(number), int)

    def test_positionInGrid1(self):
        """
        Test if the position in the grid can be set correctly.

        This method checks if the position of an element in the grid of the model can be set correctly.

        Contributors:
            - @SantiagoRR2004
        """
        model = houseModel.HouseModel()
        model.removeValue("cabinet")
        model.setPosition(0, 0, model.getAttributeFromDict("cabinet", "symbol"))
        self.assertEqual(
            model.getPosition(0, 0), model.getAttributeFromDict("cabinet", "symbol")
        )

    def test_positionInGrid2(self):
        """
        Test if the position of an element in the grid can be accessed correctly.

        This method checks if the position of an element in the grid of the model can be accessed correctly.

        Contributors:
            - @SantiagoRR2004
        """
        model = houseModel.HouseModel()
        model.removeValue("cabinet")
        model.setPosition(0, 0, model.getAttributeFromDict("cabinet", "symbol"))
        self.assertEqual(model.getPositionOf("cabinet"), [0, 0])

    def test_positionInGrid3(self):
        """
        Test if the position of a non-existent element in the grid returns False.

        This method checks if the position of a non-existent element in the grid of the model returns False.

        Contributors:
            - @SantiagoRR2004
        """
        model = houseModel.HouseModel()
        model.removeValue("cabinet")
        self.assertEqual(model.getPositionOf("cabinet"), False)

    def test_checkIfPrime(self):
        """
        Test if a number can be checked for primality correctly.

        This method checks if a number can be checked for primality correctly in the model.

        Contributors:
            - @SantiagoRR2004
        """
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
        """
        Test if the prime factorization of a number can be calculated correctly.

        This method checks if the prime factorization of a number can be calculated correctly in the model.

        Contributors:
            - @SantiagoRR2004
        """
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
        Test if all the elements in the grid are valid.

        This method tests if all the elements in the grid of the model are valid.

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
    
    def test_doorStatus1(self):
        """
        This method tests if the door can be opened and closed without problems

        Contributors:
            - @antonoterof
        """
        model = houseModel.HouseModel()
        door_locations = model.getAttributeFromDict("door", "subset")
        locationDoor = door_locations[0]["location"]
        model.openDoor(locationDoor)
        self.assertTrue(model.getDoorStatus(locationDoor) == True)
        model.closeDoor(locationDoor)
        self.assertTrue(model.getDoorStatus(locationDoor) == False)
        
    def test_doorStatus2(self):
        """
        This method tests if you want to open a door that is already open, that nothing happens

        Contributors:
            - @antonoterof
        """
        model = houseModel.HouseModel()
        door_locations = model.getAttributeFromDict("door", "subset")
        locationDoor = door_locations[0]["location"]
        model.openDoor(locationDoor)
        model.openDoor(locationDoor)
        self.assertTrue(model.getDoorStatus(locationDoor) == True)
        model.closeDoor(locationDoor)
        self.assertTrue(model.getDoorStatus(locationDoor) == False)
             
    def test_doorStatus3(self):
        """
        This method tests if you want to close a door that is already close, that nothing happens

        Contributors:
            - @antonoterof
        """
        model = houseModel.HouseModel()
        door_locations = model.getAttributeFromDict("door", "subset")
        locationDoor = door_locations[0]["location"]
        model.openDoor(locationDoor)
        model.closeDoor(locationDoor)
        model.closeDoor(locationDoor)
        self.assertTrue(model.getDoorStatus(locationDoor) == False)
            