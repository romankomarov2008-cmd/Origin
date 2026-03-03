def power_of_5:
	if n <= 0:
		return False
	while n % 5 == 0:
		n //=5
	return n == 1

def factorial(n):
	if n ==0 or n == 1:
		return 1
	else:
		return factorial(n - 1) * n
	print(factorial(5)

import math

def is_prime(n):
	if n < 2:
		return False
	else:
		for i in range(2, int(math.sqrt(n) + 1):
			if n % i == 0:
				return False
			else:
				return True
