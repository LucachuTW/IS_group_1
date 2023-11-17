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
        drawing = view.drawAgent("Cabinet")
        self.assertIsInstance(drawing, dict)
