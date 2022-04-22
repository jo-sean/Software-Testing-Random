# Name: Sean Perez
# Date: 4.22.22
# CS 362 - HW3


from credit_card_validator import credit_card_validator
import random
import string
import unittest


class TestCase(unittest.TestCase):
    """Unittest to find 6 bugs in the credit_card_validator func"""
    pass


def build_test_func(expected, test_case, func_under_test, message):
    """Unittest to find 6 bugs in the credit_card_validator func"""

    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result, message.format(test_case, expected, result))
    return test


def generate_testcases_visa(tests_to_generate=100):
    """Creates number of unit tests and """
    for i in range(tests_to_generate):
        expected = True
        # List of edge case lengths
        edge_cases = [7, 8, 9, 19, 20, 21]
        # 50% chance of generating an edge case
        odds = random.randint(0, 1)

        if odds == 1:
            length = random.choice(edge_cases)
        else:
            # Random length
            length = random.randint(0, 30)

        # Random number of lower case
        low = random.randint(0, length)
        # Random number of upper case
        up = random.randint(0, length - low)
        # Random number of numbers
        dig = random.randint(0, length - low - up)
        # Random number of symbols
        sym = random.randint(0, length - low - up - dig)
        # Determine final length of string
        length = low + up + dig + sym

        # Set expected result based on specification
        if length < 8 or length > 20:
            expected = False
        if low < 1 or up < 1 or dig < 1 or sym < 1:
            expected = False
        # Generate password
        pwd = gen_pass(length, low, up, dig, sym)

        # Build test function
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, pwd, credit_card_validator, message)
        setattr(TestCase, 'test_{}'.format(pwd), new_test)


def generate_testcases_mc(tests_to_generate=100):
    """Creates number of unit tests and """
    for i in range(tests_to_generate):
        expected = True
        # List of edge case lengths
        edge_cases = [7, 8, 9, 19, 20, 21]
        # 50% chance of generating an edge case
        odds = random.randint(0, 1)

        if odds == 1:
            length = random.choice(edge_cases)
        else:
            # Random length
            length = random.randint(0, 30)

        # Random number of lower case
        low = random.randint(0, length)
        # Random number of upper case
        up = random.randint(0, length - low)
        # Random number of numbers
        dig = random.randint(0, length - low - up)
        # Random number of symbols
        sym = random.randint(0, length - low - up - dig)
        # Determine final length of string
        length = low + up + dig + sym

        # Set expected result based on specification
        if length < 8 or length > 20:
            expected = False
        if low < 1 or up < 1 or dig < 1 or sym < 1:
            expected = False
        # Generate password
        pwd = gen_pass(length, low, up, dig, sym)

        # Build test function
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, pwd, credit_card_validator, message)
        setattr(TestCase, 'test_{}'.format(pwd), new_test)


def generate_testcases_amex(tests_to_generate=100):
    """Creates number of unit tests and """
    for i in range(tests_to_generate):
        expected = True
        # List of edge case lengths
        edge_cases = [7, 8, 9, 19, 20, 21]
        # 50% chance of generating an edge case
        odds = random.randint(0, 1)

        if odds == 1:
            length = random.choice(edge_cases)
        else:
            # Random length
            length = random.randint(0, 30)

        # Random number of lower case
        low = random.randint(0, length)
        # Random number of upper case
        up = random.randint(0, length - low)
        # Random number of numbers
        dig = random.randint(0, length - low - up)
        # Random number of symbols
        sym = random.randint(0, length - low - up - dig)
        # Determine final length of string
        length = low + up + dig + sym

        # Set expected result based on specification
        if length < 8 or length > 20:
            expected = False
        if low < 1 or up < 1 or dig < 1 or sym < 1:
            expected = False
        # Generate password
        pwd = gen_pass(length, low, up, dig, sym)

        # Build test function
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, pwd, credit_card_validator, message)
        setattr(TestCase, 'test_{}'.format(pwd), new_test)


def gen_pass(length=8, low=1, up=1, dig=1, sym=1):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = '~`!@#$%^&*()_+-='
    all_pos = lower_case + upper_case + digits + symbols

    pwd = ''
    pwd = pwd + ''.join(random.choice(lower_case) for i in range(low))
    pwd = pwd + ''.join(random.choice(upper_case) for i in range(up))
    pwd = pwd + ''.join(random.choice(digits) for i in range(dig))
    pwd = pwd + ''.join(random.choice(symbols) for i in range(sym))
    pwd = pwd + ''.join(random.choice(all_pos) for i in range(length - len(pwd)))

    return ''.join(random.sample(pwd, len(pwd)))


if __name__ == '__main__':
    generate_testcases_visa()
    generate_testcases_mc()
    generate_testcases_amex()
    unittest.main(verbosity=2)
