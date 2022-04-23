# Name: Sean Perez
# Date: 4.22.22
# CS 362 - HW3


from credit_card_validator import credit_card_validator
import random
import unittest


########################################################################
# Contents below are from Michael McLoughlin's Luhn Module
########################################################################
# The MIT License (MIT)
#
# Copyright (c) 2015 Michael McLoughlin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

def checksum(string):
    """
    Compute the Luhn checksum for the provided string of digits. Note this
    assumes the check digit is in place.
    """
    digits = list(map(int, string))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10


def verify(string):
    """
    Check if the provided string of digits satisfies the Luhn checksum.
    >>> verify('356938035643809')
    True
    >>> verify('534618613411236')
    False
    """
    return checksum(string) == 0


def generate(string):
    """
    Generate the Luhn check digit to append to the provided string.
    >>> generate('35693803564380')
    9
    >>> generate('53461861341123')
    4
    """
    check = checksum(string + '0')
    return 10 - check % 10


def append(string):
    """
    Append Luhn check digit to the end of the provided string.
    >>> append('53461861341123')
    '534618613411234'
    """
    return string + str(generate(string))
########################################################################
# Contents above are from Michael McLoughlin's Luhn Module
########################################################################


class TestCase(unittest.TestCase):
    """Unittest to find 6 bugs in the credit_card_validator func"""
    pass


def build_test_func(expected, test_case, func_under_test, message):
    """Unittest to find 6 bugs in the credit_card_validator func"""

    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result, message.format(test_case, expected, result))
    return test


def gen_credit_num(length, prefix, checks, range=None):
    # If not doing check, increments length to account for lack of new digit
    if checks == 0:
        if length > 0:
            length += 1

    # Create a range of values
    min_val = 10 ** length
    max_val = (min_val * 10) - 1

    # Adds prefix and string of random numbers in the range
    cred_num = prefix + str(random.randint(min_val, max_val))

    # If no check, just returns num. If check, returns appended checksum value
    if checks == 0:
        return cred_num
    else:
        return append(cred_num)


def generate_testcases_visa(tests_to_generate=133333):
    """Creates 100 random unit tests for visa credit card numbers"""

    for i in range(tests_to_generate):
        expected = False

        # List of edge case prefix
        prefixes = [3, 4, 5]
        # List of edge case lengths
        lengths = [0, 12, 13, 14]

        # Randomly picks prefix and length
        prefix = random.choice(prefixes)
        length = random.choice(lengths)

        # 50% chance of generating check_sum or not
        check_sum = random.randint(0, 1)

        # Set expected result based on specification for Visa
        if prefix == 4 and length == 13 and check_sum == 1:
            expected = True

        # Generate credit card number
        pwd = gen_credit_num(length, str(prefix), check_sum)

        # Build test function
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, pwd, credit_card_validator, message)
        setattr(TestCase, 'test_{}'.format(pwd), new_test)


def generate_testcases_mc(tests_to_generate=133333):
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

        # Set expected result based on specification for MC
        if (51 >= prefix >= 55 or 2221 >= prefix >= 2720) and length == 13 and check_sum == 1:
            expected = True

        # Generate password
        pwd = gen_credit_num(length, str(prefix), check_sum)

        # Build test function
        message = 'Test case: {}, Expected: {}, Result: {}'
        new_test = build_test_func(expected, pwd, credit_card_validator, message)
        setattr(TestCase, 'test_{}'.format(pwd), new_test)


def generate_testcases_amex(tests_to_generate=133333):
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

        # Set expected result based on specification for Amex
        if (prefix == 34 or prefix == 37) and length == 12 and check_sum == 1:
            expected = True

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
