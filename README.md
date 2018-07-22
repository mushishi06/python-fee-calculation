# Python Fee Calculation

Implement a FeeCalculator class such that it fulfills the fee structure below. The
fee structure does not follow a formula.

Values in between the breakpoints should be interpolated linearly between the lower bound and upper bound that they fall between.

The fee should then be "rounded" such that (fee + loan amount) is an exact multiple of 5.

The minimum amount for a loan is £1,000, and the maximum is £20,000.

You can assume values will always be within this range but they may be any value up to 2 decimal places. 

The term can be either 12 or 24 (number of months),
you can also assume values will always be within this set.

Provide a test suite verifying your solution, use any testing framework you feel
comfortable with. Use any libraries (or none) you feel add value to your solution.


# Installation

A database or any other external dependency is not required for this test.

Example:
```python
from loanapplication import LoanApplication
from feecalculator import FeeCalculator

calculator = FeeCalculator()
application = LoanApplication(24, 2750)

fee = calculator.calculate(application)
# fee = 115.0
```
# Fee Structure

### Term Fees
Loan Amount | Fees Term 12 |  Fees Term 24
------------ | ------------- | -------------
£1000: | £50 | £70
£2000: | £90 | £100
£3000: | £90 | £120
£4000: | £115 | £160
£5000: | £100 | £200
£6000: | £120 | £240
£7000: | £140 | £280
£8000: | £160 | £320
£9000: | £180 | £360
£10000: | £200 | £400
£11000: | £220 | £440
£12000: | £240 | £480
£13000: | £260 | £520
£14000: | £280 | £560
£15000: | £300 | £600
£16000: | £320 | £640
£17000: | £340 | £680
£18000: | £360 | £720
£19000: | £380 | £760
£20000: | £400 | £800
