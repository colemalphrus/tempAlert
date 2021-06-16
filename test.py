import unittest
from src.utils import rule_parser, rule_validator, following_rules


class UtilsTest(unittest.TestCase):

    def test_string_parser(self):
        val = 'temp, >, 31'
        ans = ['temp', '>', 31]
        val2 = 'temp, <, 20, or, temp, >, 30'
        ans2 = ['temp', '<', 20, 'or', 'temp', '>', 30]
        self.assertEqual(ans,  rule_parser(val))
        self.assertEqual(ans2, rule_parser(val2))

    def test_rule_validator(self):
        val = 'temp, >, 31'
        val2 = 'temp, <, 20, or, temp, >, 30'
        val3 = 'temp, <, 20, >, temp, >, 30'
        self.assertTrue(rule_validator(val))
        self.assertTrue(rule_validator(val2))
        self.assertFalse(rule_validator(val3))

    def test_rule_function(self):
        val = 'temp, >, 31'
        val2 = 'temp, <, 20, or, temp, >, 30'
        val3 = 'temp, <, 20, or, temp, >, 30'
        self.assertTrue(following_rules(val, 30, 'c'))
        self.assertTrue(following_rules(val2, 24, 'c'))
        self.assertFalse(following_rules(val3, 45, 'c'))


if __name__ == '__main__':
    unittest.main()
