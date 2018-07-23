"""Class For Loan Application."""


class LoanApplication(object):
    """Docstring for LoanApplication."""

    ACCEPTED_TERM = [12, 24]
    AMOUNT_MIN = 1000
    AMOUNT_MAX = 20000

    term = ""
    amount = None
    is_valide = True

    def __init__(self, term, amount):
        """Init and validate input."""
        super(LoanApplication, self).__init__()

        self._validate_term(term)
        self._validate_amount(amount)

    def _validate_term(self, term):
        if term in self.ACCEPTED_TERM:
            self.term = term
        else:
            self.is_valide = False
            print "Error: {} is not a valide term.\nApplication Failed.".format(term)

    def _validate_amount(self, amount):
        if self.AMOUNT_MIN < amount < self.AMOUNT_MAX:
            self.amount = amount
        else:
            self.is_valide = False
            print "Error: {} is not a valide amount. Please chose between 1,000 and 20,000. \nApplication Failed.".format(amount)
