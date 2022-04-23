# Name: Sean Perez
# Date: 4.22.22
# CS 362 - HW3


from credit_card_validator import credit_card_validator
import random
import unittest


class TestCase(unittest.TestCase):
    """Unittest to find 5 bugs in the credit_card_validator func"""
    pass


def generate_testcases_visa(tests_to_generate=200000):
    """Creates 100000 random unit tests for visa credit card numbers"""

    for i in range(tests_to_generate):

        prefix = '4'

        # List of edge case lengths
        lengths = [13, 14, 15]

        # Randomly picks length
        length = random.choice(lengths)

        min_val = (40 ** length)
        max_val = (min_val * 10) - 1

        prefix_num = prefix + str(random.randint(min_val, max_val))

        credit_card_validator(prefix_num)


def generate_testcases_mc_1(tests_to_generate=200000):
    """Creates 100000 random unit tests for mastercard credit card numbers"""

    for i in range(tests_to_generate):

        # List of edge case prefix
        prefixes = [50, 51, 52, 54, 55, 56]
        # List of edge case lengths
        lengths = [12, 13, 14]

        # Randomly picks prefix and length
        prefix = str(random.choice(prefixes))
        length = random.choice(lengths)

        min_val = (int(prefix) ** length)
        max_val = (min_val * 10) - 1

        prefix_num = prefix + str(random.randint(min_val, max_val))

        credit_card_validator(prefix_num)


def generate_testcases_mc_2(tests_to_generate=200000):
    """Creates 100000 random unit tests for mastercard credit card numbers"""

    for i in range(tests_to_generate):

        # List of edge case prefix
        prefixes = [2220, 2221, 2222, 2719, 2720, 2721]
        # List of edge case lengths
        lengths = [10, 11, 12]

        # Randomly picks prefix and length
        prefix = str(random.choice(prefixes))
        length = random.choice(lengths)

        min_val = (int(prefix) ** length)
        max_val = (min_val * 10) - 1

        prefix_num = prefix + str(random.randint(min_val, max_val))

        credit_card_validator(prefix_num)


def generate_testcases_amex(tests_to_generate=200000):
    """Creates 100000 random unit tests for amex credit card numbers"""

    for i in range(tests_to_generate):

        # List of edge case prefix
        prefixes = [33, 34, 35, 36, 37, 38, 39]
        # List of edge case lengths
        lengths = [11, 12, 13]

        # Randomly picks prefix and length
        prefix = str(random.choice(prefixes))
        length = random.choice(lengths)

        min_val = (int(prefix) ** length)
        max_val = (min_val * 10) - 1

        prefix_num = prefix + str(random.randint(min_val, max_val))

        credit_card_validator(prefix_num)


if __name__ == '__main__':
    generate_testcases_visa()
    generate_testcases_mc_1()
    generate_testcases_mc_2()
    generate_testcases_amex()
    unittest.main(verbosity=2)
