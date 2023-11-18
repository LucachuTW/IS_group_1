import unittest
import houseView
import houseModel


class testing(unittest.TestCase):
    def test_createsViewer(self):
        # @SantiagoRR2004
        view = houseModel.HouseModel().getView()
        self.assertIsInstance(view, houseView.HouseView)

    def test_draw(self):
        # @SantiagoRR2004
        view = houseModel.HouseModel().getView()
        drawing = view.draw()
        self.assertIsInstance(drawing, list)

    def test_drawCabinet(self):
        # @SantiagoRR2004
        view = houseModel.HouseModel().getView()
        drawing = view.drawAgent("cabinet")
        self.assertIsInstance(drawing, dict)
    
    def test_exists_elements_valid(self):
        # @antonvm2004
        view = houseModel.HouseModel().getView()
        drawing = view.draw()

        # Allowed elements in the list
        allowed_elements = ["0", "1", "2", "3", "4", "5"]

        # Verify that all elements in all inner lists are "0", "1", "2", "3", "4", "5"
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
        view = houseModel.HouseModel().getView()
        drawing = view.draw()

        # item number to verify
        itemNumber = "1"

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsCabinet(self):
        # @antonvm2004
        view = houseModel.HouseModel().getView()
        drawing = view.draw()

        # item number to verify
        itemNumber = "3"

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsOwner(self):
        # @antonvm2004
        view = houseModel.HouseModel().getView()
        drawing = view.draw()

        # item number to verify
        itemNumber = "4"

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)

    def test_existsRobot(self):
        # @antonvm2004
        view = houseModel.HouseModel().getView()
        drawing = view.draw()

        # item number to verify
        itemNumber = "5"

        # verify that the element is in the view
        self.assertTrue(any(itemNumber in lista_interna for lista_interna in drawing))
        self.assertTrue(drawing)