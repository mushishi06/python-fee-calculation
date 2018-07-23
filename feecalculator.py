"""Main Calculator Classes."""


class FeeCalculator(object):
    """Docstring for FeeCalculator."""

    fees = {}

    def __init__(self):
        """Init."""
        super(FeeCalculator, self).__init__()

        # Term 12 month
        self.fees[12] = {1000: 50, 2000: 90, 3000: 90, 4000: 115, 5000: 100,
                         6000: 120, 7000: 140, 8000: 160, 9000: 180, 10000: 200,
                         11000: 220, 12000: 240, 13000: 260, 14000: 280, 15000: 300,
                         16000: 320, 17000: 340, 18000: 360, 19000: 380, 20000: 400}
        # Term 24 month
        self.fees[24] = {1000: 70, 2000: 100, 3000: 120, 4000: 160, 5000: 200,
                         6000: 240, 7000: 280, 8000: 320, 9000: 360, 10000: 400,
                         11000: 440, 12000: 480, 13000: 520, 14000: 560, 15000: 600,
                         16000: 640, 17000: 680, 18000: 720, 19000: 760, 20000: 800}

    def calculate(self, application):
        """Calculate the appropriate for the application."""
        if application.is_valide:
            return self._calcule_fee(application)
        else:
            print "Error: The provide application is not valide, calculation imposible."
            return None

    def _get_down(self, amount):
        try:
            return int((amount / 1000)) * 1000
        except Exception as e:
            raise e

    def _get_fee(self, term, amount):
        try:
            return self.fees[term][amount]
        except Exception as e:
            raise e

    def _get_limit(self, app):
        lower = self._get_down(app.amount)
        uper = lower + 1000 if lower < 20000 else lower
        lower_fee = self._get_fee(app.term, int(lower))
        uper_fee = self._get_fee(app.term, int(uper))
        fee = self._find_fee(float(uper_fee), float(lower_fee), float(uper), float(lower), float(app.amount))
        return lower_fee, uper_fee, fee

    def _calcule_fee(self, app):
        lower_fee, uper_fee, fee = self._get_limit(app)
        n = round(fee + app.amount)
        while not self._validate_mul_5(n):
            n += 1
        fee = n - app.amount
        return fee

    def _validate_mul_5(self, number):
        return number % 5 == 0

    def _find_fee(self, xa, xb, ya, yb, yc):
        m = (xa - xb) / (ya - yb)
        xc = (yc - yb) * m + xb
        return xc
