import math

def getStudentNumber():
    # This method must return a string of your student number
    # If the number does not match your actual student number
    # You will not get the marks for this lab
	return "012345678"

def sum_exists(n, i, p_list):
    # Returns True if n can be formed from p_list repeated
    # some arbitrary number of times.
    pass


def find_sum(n, i, p_list, sum_list):
    # Returns a list of primes from p_list repeated some
    # arbitrary number of times so that it sums to n
    pass


def sum_exists(n, p_list, i=0):
    if n == 0:
        return True
    if n < 0:
        return False
    if i == len(p_list) - 1:
        return False
    return sum_exists(n-p_list[i], p_list, i) or sum_exists(n, p_list, i+1)



print(sum_exists(17, [2,3,5]))
print(sum_exists(7, [3,5]))