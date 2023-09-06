#Process of Handling Errors

#try:
    # Run this code
#except:
    # Execute this code if there this exception
#else:
    #No exceptions? Run this code.
#finally:
    #Always run this code.

#x = 10
#if x > 5:
#    raise Exception('x should not exceed 5. The value for x is {}'.format(x))

import sys


def linux_assertion():
    assert ('linux' in sys.platform), "This code runs on Linux only."

try:
    linux_assertion()
    with open('tdo.txt') as text:
        read_data = text.readlines()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as assertion_error:
    print(assertion_error)
    print('linux_assertion function was not executed')
    print()

try:
    file = open('file.log')
except FileNotFoundError as fnf_error:
    print(fnf_error)
    print('code run sucessfully')