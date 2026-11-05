import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_rates_at_other_weights(self):
        for weight, zone, expected in (
            (1, "local", 6.5),
            (0.5, "local", 5.75),
            (1, "regional", 9.5),
            (0.5, "regional", 8.75),
        ):
            with self.subTest(weight=weight, zone=zone):
                self.assertEqual(shipping_quote(weight, zone), expected)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")
