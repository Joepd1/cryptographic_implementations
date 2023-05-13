import math
import random
import time


def bits(b):
    # vul aan
    # Aflopend
    bits = []
    exp = math.floor(math.log2(b))

    while (exp >=0):
        if 2 ** exp <= b:
            bits.append(1)
            b -= 2 ** exp
        else:
            bits.append(0)
        exp -= 1

    return bits

def xs_binary(a, b, m):
    factors = []
    result = a
    binary_b = bits(b)

    for i in range(len(binary_b)-1, -1, -1):
        if binary_b[i] == 1:
            factors.append(result)
        result = result ** 2 % m

    return multiply_and_mod_array(factors, m)

def multiply_and_mod_array(array, mod):
    result = 1
    for number in array:
        result *= number
        result = result % mod
    return result

print(xs_binary(21,5117, 7747))
import matplotlib.pyplot as plt
import numpy as np
import random
import time

# genereer willekeurige getallen
a = random.randint(1, 5*10**5)
b = random.randint(1, 5*10**5)
m = random.randint(1, 5*10**5)

# test methodes op getallen
times_simple_implementation = []
times_pow_implementation = []
times_xsbinary_implementation = []

for i in range(100):
    # simple method
    start_time = time.time()
    a**b % m
    end_time = time.time()
    times_simple_implementation.append(end_time-start_time)

    # using pow()
    start_time = time.time()
    pow(a,b,m)
    end_time = time.time()
    times_pow_implementation.append(end_time-start_time)

    # using xs binary algoritm
    start_time = time.time()
    xs_binary(a,b,m)
    end_time = time.time()
    times_xsbinary_implementation.append(end_time-start_time)


# plot resultaten
fig, ax = plt.subplots()
ax.set_yscale('log')
ax.set_xlabel('Methodes')
ax.set_ylabel('Tijd (s, log)')

# naı̈ve implementatie,  ingebouwde implementatie en eigen modulaire exponentiatie
dataY_as = [sum(times_simple_implementation) /100, sum(times_pow_implementation) /100, sum(times_xsbinary_implementation)/100]
ax.bar(['naı̈ve implementatie', 'pow', 'modulaire exponentiatie'], dataY_as)
plt.show()