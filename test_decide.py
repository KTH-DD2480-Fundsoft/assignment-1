import unittest
from set_CMV import set_CMV_4








class TestDecide(unittest.TestCase):
    def test_cmv_4(self):
        parameters = {
            'qpts' : 4,
            'quads' : 3
        }
        data_points = [(0.1, 0.1), (-0.1, 0.1), (0.1, -0.1), (-0.1, -0.1), (0.1, 0.1)]
        num_points = len(data_points)
        self.assertTrue(set_CMV_4(num_points, data_points, parameters), "4 consecutive points occupy 4 quadrants")

    def test_cmv_4(self):
        parameters = {
            'qpts' : 4,
            'quads' : 3
        }
        data_points = [(0.1, 0.1), (0.1, -0.1), (0.1, -0.1), (-0.1, 0.1), (0.1, 0.1)]
        num_points = len(data_points)
        self.assertFalse(set_CMV_4(num_points, data_points, parameters), "No 4 consecutive points occupy 4 quadrants")

    def test_cmv_4(self):
        parameters = {
            'qpts' : 2,
            'quads' : 3
        }
        data_points = [(0.1, 0.1), (-0.1, 0.1), (0.1, -0.1), (-0.1, -0.1), (0.1, 0.1)]
        num_points = len(data_points)
        self.assertFalse(set_CMV_4(num_points, data_points, parameters), "Impossible since quads > qpts")

    def test_cmv_4(self):
        parameters = {
            'qpts' : 3,
            'quads' : 2
        }
        data_points = [(0.1, 0.1), (0.1, -0.1), (0.1, -0.1), (0.1, -0.1), (0.1, 0.1), (-0.1, -0.1)]
        num_points = len(data_points)
        self.assertTrue(set_CMV_4(num_points, data_points, parameters), "The qpts last points occupy more than 2 quadrants")

    def test_cmv_4(self):
        data_points = [(0.1, 0.1), (0.1, -0.1), (0.1, -0.1), (0.1, -0.1), (-0.1, 0.1), (-0.1, -0.1)]
        num_points = len(data_points)
        parameters = {
            'qpts' : num_points,
            'quads' : 3
        }
        self.assertTrue(set_CMV_4(num_points, data_points, parameters), "qpts = num_points, all 4 quadrants are occupied")


if __name__ == '__main__':
    unittest.main()