"""Module providing functions for manipulating integer lists."""

print('assign3.py')

def sum_int_list(arg_list):
    '''
    Accepts: a list of integers (arg_list)
    Returns: an integer which is the sum of all items in the list
    '''
    return sum(arg_list)

def power_int_list(arg_list, n):
    '''
    Accepts: a list of integers (arg_list) and an integer (n)
    Returns: a list of integers raised to (n) power
    '''
    return [x ** n for x in arg_list]

def power_sum_int_list(arg_list, n):
    '''
    Accepts: a list of integers (arg_list) and an integer (n)
    Returns: an integer which is all items raised to (n) power, summed together
    '''
    powered_list = power_int_list(arg_list, n)
    return sum(powered_list)

# Test the functions
test_list = [3, 7, 1]
n = 5

result_sum = sum_int_list(test_list)
result_pow = power_int_list(test_list, n)
result_pow_sum = power_sum_int_list(test_list, n)

print('Result of sum_int_list: {}'.format(result_sum))
print('Result of power_int_list: {}'.format(result_pow))
print('Result of power_sum_int_list: {}'.format(result_pow_sum))