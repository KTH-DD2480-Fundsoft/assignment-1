import unittest
from set_CMV import set_CMV_4








class TestDecideCMV4(unittest.TestCase):
    def test_cmv_4_should_return_true(self):
        parameters = {
            'qpts' : 4,
            'quads' : 3
        }
        data_points = [(0.1, 0.1), (-0.1, 0.1), (0.1, -0.1), (-0.1, -0.1), (0.1, 0.1)]
        num_points = len(data_points)
        self.assertTrue(set_CMV_4(num_points, data_points, parameters))

    def test_cmv_4_should_return_false(self):
        parameters = {
            'qpts' : 4,
            'quads' : 3
        }
        data_points = [(0.1, 0.1), (0.1, -0.1), (0.1, -0.1), (-0.1, 0.1), (0.1, 0.1)]
        num_points = len(data_points)
        self.assertFalse(set_CMV_4(num_points, data_points, parameters))

    def test_cmv_4_impossible(self):
        parameters = {
            'qpts' : 2,
            'quads' : 3
        }
        data_points = [(0.1, 0.1), (-0.1, 0.1), (0.1, -0.1), (-0.1, -0.1), (0.1, 0.1)]
        num_points = len(data_points)
        self.assertFalse(set_CMV_4(num_points, data_points, parameters))

    def test_cmv_4_last_qpts_points_are_satisfactory(self):
        parameters = {
            'qpts' : 3,
            'quads' : 2
        }
        data_points = [(0.1, 0.1), (0.1, -0.1), (0.1, -0.1), (0.1, -0.1), (0.1, 0.1), (-0.1, -0.1)]
        num_points = len(data_points)
        self.assertTrue(set_CMV_4(num_points, data_points, parameters))

    def test_cmv_4_qpoints_equals_numpoints(self):
        data_points = [(0.1, 0.1), (0.1, -0.1), (0.1, -0.1), (0.1, -0.1), (-0.1, 0.1), (-0.1, -0.1)]
        num_points = len(data_points)
        parameters = {
            'qpts' : num_points,
            'quads' : 3
        }
        self.assertTrue(set_CMV_4(num_points, data_points, parameters))


if __name__ == '__main__':
    unittest.main()