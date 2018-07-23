"""Exemple code."""

from feecalculator import FeeCalculator

from loanapplication import LoanApplication

calculator = FeeCalculator()
application = LoanApplication(24, 2750)

fee = calculator.calculate(application)
print "fee = ", fee
# Output fee = 115.0
