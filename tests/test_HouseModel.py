import unittest
import houseModel


class testing(unittest.TestCase):
    def test_env_2(self):
        a = houseModel.HouseModel()
        self.assertEqual(5, 5)
