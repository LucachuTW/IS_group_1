import unittest
import houseView
import houseModel
import atexit


class helpTestViewer:
    """
    This class exists to help test the viewer
    """

    def setUp(self):
        """
        This runs for every test at the start automatically.

        For all these tests we only need the model and viewer.

        Contributors:
            - @SantiagoRR2004
        """
        self.model = houseModel.HouseModel("environmentBackup.json")
        atexit.unregister(self.model.saveToFile)
        self.view = houseView.HouseView(self.model)

    def tearDown(self):
        """
        This runs for every test at the end automatically.

        It deletes objects to free space up.
        It might not be necessary.

        Contributors:
            - @SantiagoRR2004
        """
        del self.view
        del self.model


class testView(helpTestViewer, unittest.TestCase):
    def test_createsViewer(self):
        """
        Test if the viewer is created.

        This method checks if the viewer is created.

        Contributors:
        - @SantiagoRR2004
        """
        view = self.view
        self.assertIsInstance(view, houseView.HouseView)

    def test_draw(self):
        """
        Test the draw method.

        This method tests the draw method of the HouseView class.

        Contributors:
        - @SantiagoRR2004
        """
        view = self.view
        drawing = view.draw()
        self.assertIsInstance(drawing, list)

    def test_drawWall(self):
        """
        Test the drawAgent method with "wall" parameter.

        This method tests the drawAgent method of the HouseView class with "wall" parameter.

        Contributors:
        - @antonvm2004
        """
        view = self.view
        drawing = view.drawAgent("wall")
        self.assertIsInstance(drawing, dict)

    def test_drawDoor(self):
        """
        Test the drawAgent method with "door" parameter.

        This method tests the drawAgent method of the HouseView class with "door" parameter.

        Contributors:
        - @antonvm2004
        """
        view = self.view
        drawing = view.drawAgent("door")
        self.assertIsInstance(drawing, dict)

    def test_drawCabinet(self):
        """
        Test the drawAgent method with "cabinet" parameter.

        This method tests the drawAgent method of the HouseView class with "cabinet" parameter.

        Contributors:
        - @SantiagoRR2004
        """
        view = self.view
        drawing = view.drawAgent("cabinet")
        self.assertIsInstance(drawing, dict)

    def test_drawOwner(self):
        """
        Test the drawAgent method with "owner" parameter.

        This method tests the drawAgent method of the HouseView class with "owner" parameter.

        Contributors:
        - @antonvm2004
        """
        view = self.view
        drawing = view.drawAgent("owner")
        self.assertIsInstance(drawing, dict)

    def test_drawRobot(self):
        """
        Test the drawAgent method with "robot" parameter.

        This method tests the drawAgent method of the HouseView class with "robot" parameter.

        Contributors:
        - @antonvm2004
        """
        view = self.view
        drawing = view.drawAgent("robot")
        self.assertIsInstance(drawing, dict)

    def test_existsEmptyBox(self):
        """
        Test if the empty box exists in the view.

        This method tests if the empty box exists in the view.

        Contributors:
        - @antonvm2004
        """
        view = self.view
        drawing = view.draw()

        # item number to verify
        itemNumber = 0

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsWall(self):
        """
        Test if the wall exist in the view.

        This method tests if the wall exist in the view.

        Contributors:
        - @antonvm2004
        - @antonoterof
        """
        view = self.view
        drawing = view.draw()

        # item number to verify
        itemNumber = 2

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsDoor(self):
        """
        Test if the door exist in the view.

        This method tests if the door exist in the view.

        Contributors:
        - @antonoterof
        """
        view = self.view
        drawing = view.draw()

        # item number to verify
        itemNumber = 3

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsCabinet(self):
        """
        Test if the cabinet exists in the view.

        This method tests if the cabinet exists in the view.

        Contributors:
        - @antonvm2004
        - @antonoterof
        """
        view = self.view
        drawing = view.draw()

        # item number to verify
        itemNumber = 5

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsOwner(self):
        """
        Test if the owner exists in the view.

        This method tests if the owner exists in the view.

        Contributors:
        - @antonvm2004
        - @antonoterof
        """
        view = self.view
        drawing = view.draw()

        # item number to verify
        itemNumber = 7

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsRobot(self):
        """
        Test if the robot exists in the view.

        This method tests if the robot exists in the view.

        Contributors:
        - @antonvm2004
        - @antonoterof
        """
        view = self.view
        drawing = view.draw()

        # item number to verify
        itemNumber = 11

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)
