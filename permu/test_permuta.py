import unittest
from permuta import Permutation


class TestPermu(unittest.TestCase):

    def test_npr(self):
        pM=Permutation()
        self.assertEqual(pM.npr(10,4),5040,"should be 5040")

    def test_one(self):
            pM=Permutation()
            self.assertEqual(pM.npr(5,2),20,"should be 20")

    def test_two(self):
        pM=Permutation()
        self.assertEqual(pM.npr(9,3),504,"should be 504")


    def test_three(self):
        pM=Permutation()
        self.assertEqual(pM.npr(5,3),60,"should be 60")

if __name__=="__main__":
    unittest.main()