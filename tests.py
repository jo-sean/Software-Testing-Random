# Name: Sean Perez
# Date: 4.22.22
# CS 362 - HW3


from credit_card_validator import credit_card_validator
import random
import unittest
import luhn


class TestCase(unittest.TestCase):
    """Unittest to find 6 bugs in the credit_card_validator func"""
    pass


def build_test_func(expected, test_case, func_under_test, message):
    """Unittest to find 6 bugs in the credit_card_validator func"""

    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result, message.format(test_case, expected, result))
    return test


def gen_credit_num(length, prefix, checks):
    if checks == 0:
        length += 1

    min_val = 10 ** length
    max_val = (min_val * 10) - 1

    # Adds prefix and string of random numbers in the range
    cred_num = prefix + str(random.randint(min_val, max_val))

    if checks == 0:
        return cred_num
    else:
        return luhn.append(cred_num)


def generate_testcases_visa(tests_to_generate=100):
    """Creates 100 random unit tests for visa credit card numbers"""

    for i in range(tests_to_generate):
        expected = True

        # List of edge case prefix
        prefixes = [3, 4, 5]
        # List of edge case lengths
        lengths = [12, 13, 14]

        # Randomly picks prefix and length
        prefix = random.choice(prefixes)
        length = random.choice(lengths)

        # 50% chance of generating check_sum or not
        check_sum = random.randint(0, 1)

        # Set expected result based on specification
        if length < 16 or length > 16:
            expected = False

        if prefix < 4 or prefix < 4 or check_sum == 0:
            expected = False

        # Generate password
        pwd = gen_credit_num(length, str(prefix), check_sum)

        # Build test function
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, pwd, credit_card_validator, message)
        setattr(TestCase, 'test_{}'.format(pwd), new_test)


def generate_testcases_mc(tests_to_generate=100):
    """Creates 100 random unit tests for mastercard credit card numbers"""

    for i in range(tests_to_generate):
        expected = True

        # List of edge case prefix
        prefixes = [50, 51, 52, 54, 55, 56, 2220, 2221, 2222, 2719, 2720, 2721]
        # List of edge case lengths
        lengths = [12, 13, 14]

        # Randomly picks prefix and length
        prefix = random.choice(prefixes)
        length = random.choice(lengths)

        # 50% chance of generating check_sum or not
        check_sum = random.randint(0, 1)

        # Set expected result based on specification
        if length < 16 or length > 16:
            expected = False

        if prefix < 4 or prefix < 4 or check_sum == 0:
            expected = False

        # Generate password
        pwd = gen_credit_num(length, str(prefix), check_sum)

        # Build test function
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, pwd, credit_card_validator, message)
        setattr(TestCase, 'test_{}'.format(pwd), new_test)


def generate_testcases_amex(tests_to_generate=100):
    """Creates 100 random unit tests for amex credit card numbers"""

    for i in range(tests_to_generate):
        expected = True

        # List of edge case prefix
        prefixes = [33, 34, 35, 36, 37, 38]
        # List of edge case lengths
        lengths = [11, 12, 13]

        # Randomly picks prefix and length
        prefix = random.choice(prefixes)
        length = random.choice(lengths)

        # 50% chance of generating check_sum or not
        check_sum = random.randint(0, 1)

        # Set expected result based on specification
        if length < 16 or length > 16:
            expected = False

        if prefix < 4 or prefix < 4 or check_sum == 0:
            expected = False

        # Generate password
        pwd = gen_credit_num(length, str(prefix), check_sum)

        # Build test function
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, pwd, credit_card_validator, message)
        setattr(TestCase, 'test_{}'.format(pwd), new_test)


if __name__ == '__main__':
    generate_testcases_visa()
    generate_testcases_mc()
    generate_testcases_amex()
    unittest.main(verbosity=2)
