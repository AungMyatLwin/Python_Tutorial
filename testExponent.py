import unittest
from exponent import ExponentClass

class TestExponent(unittest.TestCase):
    def testExpo(self):
        EC=ExponentClass()
        self.assertEqual(EC.expo(number=2,exponent=10),1024,"should be 1024")


if __name__=="__main__":
    unittest.main()