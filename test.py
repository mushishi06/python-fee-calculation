import unittest

from feecalculator import FeeCalculator

from loanapplication import LoanApplication


class Test24Term(unittest.TestCase):
    calculator = FeeCalculator()
    application = LoanApplication(24, 2750)

    def test_boundary_fee(self):
        lower_fee, uper_fee, fee = self.calculator._get_limit(self.application)
        self.assertEqual(lower_fee, 100)
        self.assertEqual(uper_fee, 120)

    def test_fee(self):
        self.assertEqual(self.calculator.calculate(self.application), 115)


class Test12Term(unittest.TestCase):
    calculator = FeeCalculator()
    application = LoanApplication(12, 13500)

    def test_boundary_fee(self):
        lower_fee, uper_fee, fee = self.calculator._get_limit(self.application)
        self.assertEqual(lower_fee, 260)
        self.assertEqual(uper_fee, 280)

    def test_fee(self):
        self.assertEqual(self.calculator.calculate(self.application), 270)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(Test24Term)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(Test12Term)
    unittest.TextTestRunner(verbosity=2).run(suite)
