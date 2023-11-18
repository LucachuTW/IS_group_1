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

    def test_existsWall(self):
        # @antonoterof
        model = houseModel.HouseModel()
        exists = model.existsWall()
        self.assertEqual(exists, "1")

    def test_existsCabinet(self):
        # @antonoterof
        model = houseModel.HouseModel()
        exists = model.existsCabinet()
        self.assertEqual(exists, "3")
