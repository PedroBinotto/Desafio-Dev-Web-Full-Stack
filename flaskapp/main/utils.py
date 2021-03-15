from math import sqrt
from itertools import count, islice

def is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n)-1)))

def calculate(n1, n2):
	return [i for i in range(n1, n2 + 1) if is_prime(i)]

