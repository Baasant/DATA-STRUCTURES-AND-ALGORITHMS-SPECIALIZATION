# python3

from sys import stdin
import sys
import unittest
# capacity :the capacity of the bag
import sys
from collections import namedtuple

Item = namedtuple("Item", "value weight")

def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    values=prices
    value = 0
    maxim = 0
    lst = list()
    idx = 0
    while capacity>0:
        maxim = 0
        for i in range(len(weights)):
            if values[i]/weights[i]>=maxim and not(i in lst):
                maxim = values[i]/weights[i]
                idx  = i

        ic = min(weights[idx ],capacity)
        capacity -= ic

        value += ic*maxim
        lst.append(idx )


    return value

'''''
    price=0
    maxim=0
    idx=0
    taken=0
    idx_list=[]
    while capacity>0:
        for i in range(len(weights)):
            if (prices[i]/weights[i])>maxim and i not in idx_list:
                maxim=prices[i]/weights[i]
        idx=i
        idx_list.append(i)
        taken=min(capacity,weights[idx])
        capacity-=taken
        price+=taken*maxim
    return price

'''''


# Base case redundant, but added for clarity









if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
