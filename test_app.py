import unittest
from app import hello

class TestApp(unittest.Testcase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, Jenkins!")

if __name__ == "__main__":
    unittest.main()
