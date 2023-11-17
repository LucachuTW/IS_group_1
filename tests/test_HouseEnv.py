import unittest
import houseEnv
import houseModel


class testing(unittest.TestCase):
    def test_correctRelationship(self):
        # @SantiagoRR2004
        control = houseModel.HouseModel().getController()
        control2 = control.getModel().getController()
        self.assertEqual(control, control2)
