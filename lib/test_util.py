import unittest
import util


class TestUtil(unittest.TestCase):
    def test_intersect(self):
        a = [1, 2, 3]
        b = [1, 3, 4, 5]
        c = [1, 3]
        c2 = util.intersect(a, b)
        self.assertEqual(set(c), set(c2))

    def test_info(self):
        print(util.info.__doc__)
        print(util.info('tsring'))
