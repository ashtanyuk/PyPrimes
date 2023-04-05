import unittest
from primes import isPrime

class TestPrimes(unittest.TestCase):
   def test_1(self):
       res = isPrime(1)
       self.assertEqual(res, False)

   def test_2(self):
       res = isPrime(2)
       self.assertEqual(res, True)

   def test_3(self):
       res = isPrime(3)
       self.assertEqual(res, True)

   def test_4(self):
       res = isPrime(4)
       self.assertEqual(res, False)

# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()