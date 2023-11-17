import unittest
import houseEnv
import houseModel


class testing(unittest.TestCase):
    def test_createsController(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        self.assertIsInstance(control, houseEnv.HouseEnv)
