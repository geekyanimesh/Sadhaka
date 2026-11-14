
import unittest

from code_classes import add,divide, BankAccount

class TestCalculator(unittest.TestCase):

    def test_add(self):
        result=add(10,20)

        self.assertEqual(result,30)

    def test_divide_by_zero(self):

        with self.assertRaises(ZeroDivisionError):
            divide(10,0)

if __name__=="__main__":
    unittest.main()


# assertEqual(a, b)	    Checks whether a equals b.      self.assertEqual(10 + 20, 30)
# assertNotEqual(a, b)	Checks whether a differs from b.        
# assertTrue(x)	        Checks whether x is truthy.     self.assertTrue(10 > 5)
# assertFalse(x)	    Checks whether x is falsy.      self.assertFalse(10 < 5)
# assertIs(a, b)	    Checks whether both refer to the same object.   
# assertIsNone(x)	    Checks whether x is None.
# assertIn(a, b)	    Checks whether a exists inside b.       self.assertIn("Python", ["Java", "Python", "C++"])
# assertRaises()	    Checks whether an expected exception is raised.     


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account=BankAccount(1000)

    def test_deposite(self):
        self.account.deposit(500)
        self.assertEqual(self.account.amount,1500)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.amount, 1500)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.amount, 800)




