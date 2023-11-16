import unittest
import houseEnv


class testing(unittest.TestCase):
    def test_env_2(self):
        a = houseEnv.HouseEnv()
        self.assertEqual(5, 5)
