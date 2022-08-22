import unittest
from movie import Movie

class TestUnitMovie(unittest.TestCase):
    def test_init_movie(self):
        m=Movie("Testtitle","TestDirec",3.14)
        self.assertEqual(m.title,"Testtitle","Should be Testtitle")
        self.assertEqual(m.director,"TestDirec","Should be TestDirec")
    def test_getrating(self):
        m=Movie("Testtitle","TestDirec",3.14)
        self.assertEqual(m.getrating,3.14,"Should be 3.14")

    def test_setrating(self):
        m=Movie("Testtitle","TestDirec",3.14)
        m.setrating=3.44
        self.assertEqual(m.getrating,3.44,"Should be 3.44")


if __name__=="__main__":
    unittest.main()