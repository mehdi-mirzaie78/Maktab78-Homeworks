import unittest
from Subway.models.card import *


class TestCard(unittest.TestCase):
    def setUp(self):
        self.single1 = Card('single_trip')
        self.credit1 = Card('credit', 1000)
        self.term1 = Card('term', 320, datetime(2022, 9, 10))

    def test_create(self):
        self.assertEqual(self.single1.name, 'single_trip')
        self.assertEqual(self.single1.charge, 10)
        self.assertEqual(self.single1.expiration_date, None)
        self.assertEqual(self.single1.__repr__(), f"card {self.single1.name} - charge: {self.single1.charge}")

        self.assertEqual(self.credit1.name, 'credit')
        self.assertEqual(self.credit1.charge, 1000)
        self.assertEqual(self.credit1.expiration_date, None)

        self.assertEqual(self.term1.name, 'term')
        self.assertEqual(self.term1.charge, 320)
        self.assertEqual(self.term1.expiration_date, datetime(2022, 9, 10))

    def test_name(self):
        self.assertTrue(self.single1.name in self.single1.__class__.CARDS)
        self.assertIsInstance(self.single1.name, str)
        self.assertRaises(TypeError, Card, 2)
        self.assertRaises(CardError, Card, 'card')

        self.assertTrue(self.term1.name in self.term1.__class__.CARDS)
        self.assertIsInstance(self.term1.name, str)
        self.assertRaises(TypeError, Card, True, 320, datetime(2022, 9, 10))
        self.assertRaises(CardError, Card, 'Term')

    def test_charge(self):
        self.assertIsInstance(self.credit1.charge, int)
        self.assertTrue(self.credit1.charge > 0)
        self.assertRaises(ChargeError, Card, 'credit', -234)
        self.assertRaises(TypeError, Card, 'credit', 'hello')

        self.assertIsInstance(self.term1.charge, int)
        self.assertTrue(self.term1.charge > 0)
        self.assertRaises(ChargeError, Card, 'term', -23)
        self.assertRaises(TypeError, Card, 'term', None)

    def test_expiration_date(self):
        self.assertIsInstance(self.term1.expiration_date, datetime)
        self.assertTrue(self.term1.expiration_date > datetime.today())
        self.assertRaises(TypeError, Card, 'term', 320, 2022)
        self.assertRaises(TypeError, Card, 'term', 320, True)
        self.assertRaises(DateError, Card, 'term', 320, datetime(2022, 7, 29))

    def test_pay(self):
        self.single1.pay()
        self.assertTrue(self.single1.charge == 0)
        self.assertRaises(ChargeError, self.single1.pay)

        self.term1.pay()
        self.assertTrue(self.term1.charge == 310)
        self.assertRaises(ChargeError, self.term1.pay, 320)

        self.credit1.pay()
        self.assertEqual(self.credit1.charge, 990)
        self.assertRaises(ChargeError, self.credit1.pay, 1000)


if __name__ == '__main__':
    unittest.main()
