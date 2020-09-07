# python3
import math
import timeit
import time

def fibonacci_number_naive(n):

    assert 0 <= n <= 45
    if n <= 1:
        return n
    m=(math.sqrt(5)+1)/2
    return round(math.pow(m,n)/math.sqrt(5))




    #type here


def fibonacci_number(n):
    assert 0 <= n <= 45
    if n <= 1:
        return n
    m=(math.sqrt(5)+1)/2
    return round(math.pow(m,n)/math.sqrt(5))



if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
