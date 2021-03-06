import unittest

# decorator for time
from Tools.Timeout import timeout

# individual student copied file, put all the functions you are testing 
from Test import greet, bye

# Unit Test Class
class Test_Sample(unittest.TestCase):
    
    # Test the greet function
    @timeout()
    def test_greet(self):
        self.assertEqual(greet("Saad"), "Hello, Saad!", "Testing Greet")

    # Test the bye function
    @timeout()
    def test_bye(self):
        self.assertEqual(bye(), "Good Bye!", "Testing Bye")


if __name__ == '__main__':
    unittest.main()