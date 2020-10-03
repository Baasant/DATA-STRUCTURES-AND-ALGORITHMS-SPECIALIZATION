# python3
import sys
from collections import defaultdict

def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5
    n=int(len(elements)/2)
    flag = 0
    dic = defaultdict(int)
    for i in elements:
        dic[i]+= 1
    for element in elements:
        if element in dic.keys() and dic[element] > n:
            flag=1
            break
    return flag

    '''''
    n=len(elements)
    count1=0
    count2=0
    first=0
    second=0
    for i in range(0,n):
        if (first==elements[i]):
            count1+=1
        elif (second==elements[i]):
            count2+=1
        elif (count1 == 0):
            count1 += 1
            first = elements[i]
        elif (count2 == 0):
            count2 += 1
            second = elements[i]
        else:
            count1 -= 1
            count2 -= 1
    count1=0
    count2=0
    for i in range(0, n):
        if (elements[i] == first):
            count1 += 1
        elif (elements[i] == second):
            count2 += 1
    if (count1 > n /2):
        return 1
    if (count2 > n /2):
        return 1
    return 0

'''''

if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))
