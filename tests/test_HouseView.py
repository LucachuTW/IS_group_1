import unittest
import houseView
import houseModel


class testing(unittest.TestCase):
    def test_createsViewer(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getView()
        self.assertIsInstance(control, houseView.HouseView)
