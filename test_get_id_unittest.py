import unittest
from src import WindowCalculator

class TestGetId(unittest.TestCase):
  
  def test_get_id(self):
    self.assertEqual(WindowCalculator.get_window_id(4,10), 3, "Should be 3")
    self.assertEqual(WindowCalculator.get_window_id(4,1), 0, "Should be 3")
    
    
if __name__ == '__main__':
    unittest.main()
    