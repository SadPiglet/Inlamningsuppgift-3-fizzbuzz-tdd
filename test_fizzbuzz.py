import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
  def test_regular_number(self):
    self.assertEqual(fizzbuzz(1), 1)

  def test_fizz_for_multiples_of_three(self):
    self.assertEqual(fizzbuzz(3), "Fizz")

if __name__ == '__main__':
  unittest.main()