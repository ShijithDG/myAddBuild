import unittest
from addingFunction import add

class TestingFunction(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3,7), 10)
        self.assertEqual(add(-2,2), 0)

if __name__ == '__main__':
    unittest.main()