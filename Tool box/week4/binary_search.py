# python3
import math

def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1

def binary_searchx(a, x, left, right):
    r = -1
    if left <= right:
        mid = int((left + right)/2)
        if x > a[mid]:
            left = mid + 1
            r = binary_searchx(a, x, left, right)
        elif x < a[mid]:
            right = mid - 1
            r = binary_searchx(a, x, left, right)
        else:
            r = mid
    return r

def binary_search(keys, query):
    assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4
    a, x, left, right=keys,query,0,len(keys)-1
    return binary_searchx(a, x, left, right)




    # write your code here





if __name__ == '__main__':
    input_keys = list(map(int, input().split()))[1:]
    input_queries = list(map(int, input().split()))[1:]

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
