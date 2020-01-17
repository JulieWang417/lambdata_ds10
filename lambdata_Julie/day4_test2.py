from calculator import Count
import unittest


class TestCount(unittest.TestCase):

    def setUp(self):
        print("test start")

    # add
    def test_add(self):
        self.Count = Count(2, 3)
        self.assertEqual(self.Count.add(), 5)

    # subtract
    def test_sub(self):
        self.Count = Count(6, 3)
        self.assertEqual(self.Count.sub(), 3)

    # multiple
    def test_mul(self):
        self.Count = Count(6, 3)
        self.assertEqual(self.Count.mul(), 18)

    # divide
    def test_div(self):
        self.Count = Count(6, 3)
        self.assertEqual(self.Count.div(), 2)

    # teardown
    def tearDown(self):
        print("test end")


if __name__ == "__main__":
    # testsuite
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add"))
    suite.addTest(TestCount("test_sub"))
    suite.addTest(TestCount("test_mul"))
    suite.addTest(TestCount("test_div"))


# test
    runner = unittest.TextTestRunner()
    runner.run(suite)
