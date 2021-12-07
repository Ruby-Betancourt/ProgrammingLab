import unittest
from csvfile import CSVFile 

#Testing

class testcsvfile(unittest.TestCase):
  def test_csvfile(self):
    csv_file=CSVFile('sales.txt')
    Expectation = [['01-01-2012','266.0\n'], ['01-02-2012', '145.9\n'], ['01-03-2012', '183.1\n']]
    self.assertEqual(csv_file.get_data(0,3), Expectation)
  
  def test_rightname(self):
    csv_file=CSVFile('sales.txt')
    self.assertEqual(csv_file.name, 'sales.txt')
  
  def test_eccezioni(self):
    csv_file=CSVFile('sales.txt')
    with self.assertRaises(TypeError):
        csv_file.get_data('tre', 3)
      