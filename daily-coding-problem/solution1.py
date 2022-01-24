# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

def do_any_two_numbers_add_up_to_k(numbers_list, k):
    numbers_set = set(numbers_list) # faster verification
    for number in numbers_set:
        if (k - number in numbers_set): # not necessarily two distinct numbers, according to the requirement
            return True
    return False
