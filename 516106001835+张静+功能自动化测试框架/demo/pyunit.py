import unittest
import sys
import case
import getfile




class TestAdd(unittest.TestCase):
    def setUp(self):
        print("Start test")
    def tearDown(self):
        print("End test")
    def test_add(self):
        # j = Count(2,3)
        path = sys.path[0]
        pathName = path + '/answer14.txt'
        getFile = getfile.GetFile()
        answers = getFile.getAnswer(pathName)
        primePath = case.PrimePath()
        print(self.assertEqual(primePath.GetResult(), answers))
        

if __name__ == "__main__":
    unittest.main()
