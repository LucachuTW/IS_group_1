import unittest
import houseView
import houseModel


class testing(unittest.TestCase):

    def test_createsViewer(self):
        # @SantiagoRR2004
        view = houseModel.HouseModel().getView()
        self.assertIsInstance(view, houseView.HouseView)
        # Check that houseView is instantiated

    def test_draw(self):
        # @SantiagoRR2004
        view = houseModel.HouseModel().getView()
        drawing = view.draw()
        self.assertIsInstance(drawing, list)

    def test_drawWalls(self):
        # @antonvm2004
        view = houseModel.HouseModel().getView()
        drawing = view.drawAgent("walls")
        self.assertIsInstance(drawing, dict)
    
    def test_drawDoors(self):
        # @antonvm2004
        view = houseModel.HouseModel().getView()
        drawing = view.drawAgent("doors")
        self.assertIsInstance(drawing, dict)
    
    def test_drawCabinet(self):
        # @SantiagoRR2004
        view = houseModel.HouseModel().getView()
        drawing = view.drawAgent("cabinet")
        self.assertIsInstance(drawing, dict)
       
    def test_drawOwner(self):
        # @antonvm2004
        view = houseModel.HouseModel().getView()
        drawing = view.drawAgent("owner")
        self.assertIsInstance(drawing, dict)
    
    def test_drawRobot(self):
        # @antonvm2004
        view = houseModel.HouseModel().getView()
        drawing = view.drawAgent("robot")
        self.assertIsInstance(drawing, dict)

    def test_exists_elements_valid(self):
        # @antonvm2004
        # Modified by @antonoterof
        view = houseModel.HouseModel().getView()
        drawing = view.draw()

        # Allowed elements in the list
        allowed_elements = ["0", "2", "3", "5", "7", "11"]

        # Verify that all elements in all inner lists are "0", "2", "3", "5", "7", "11"
        self.assertTrue(all(element in allowed_elements for inner_list in drawing for element in inner_list))

    def test_existsEmptyBox(self):
        # @antonvm2004
        view = houseModel.HouseModel().getView()
        drawing = view.draw()

        # item number to verify
        itemNumber = "0"

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsWalls(self):
        # @antonvm2004
        # Modified by @antonoterof
        view = houseModel.HouseModel().getView()
        drawing = view.draw()

        # item number to verify
        itemNumber = "2"

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsDoors(self):
        # @antonoterof
        view = houseModel.HouseModel().getView()
        drawing = view.draw()

        # item number to verify
        itemNumber = "3"

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsCabinet(self):
        # @antonvm2004
        # Modified by @antonoterof
        view = houseModel.HouseModel().getView()
        drawing = view.draw()

        # item number to verify
        itemNumber = "5"

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsOwner(self):
        # @antonvm2004
        # Modified by @antonoterof
        view = houseModel.HouseModel().getView()
        drawing = view.draw()

        # item number to verify
        itemNumber = "7"

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsRobot(self):
        # @antonvm2004
        # Modified by antón OF
        view = houseModel.HouseModel().getView()
        drawing = view.draw()

        # item number to verify
        itemNumber = "11"

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)