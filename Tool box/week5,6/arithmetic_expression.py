# python3
import re

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
def min_and_max(M, m, ops, i, j):
    # it seems that we cannot import math.inf here
    minimum = 1000
    maximum = -1000

    for k in range(i, j):
        a = evalt(M[i][k], M[k + 1][j], ops[k])
        b = evalt(M[i][k], m[k + 1][j], ops[k])
        c = evalt(m[i][k], M[k + 1][j], ops[k])
        d = evalt(m[i][k], m[k + 1][j], ops[k])

        minimum = min(minimum, a, b, c, d)
        maximum = max(maximum, a, b, c, d)
    return minimum, maximum




def find_maximum_value(dataset):
    assert 1 <= len(dataset) <= 29

    digits = list(int(digit) for digit in re.findall(r"(\d+)+", dataset))
    operations = re.findall(r"([\+|\-|\\|\*])+", dataset)

    m = []
    M = []
    n = len(digits)
    for i in range(0, n):
        m.append(list(0 for j in digits))
        M.append(list(0 for j in digits))
    for i in range(0, len(m)):
        m[i][i] = digits[i]
        M[i][i] = digits[i]

    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            res = min_and_max(M, m, operations, i, j)
            m[i][j], M[i][j] = res

    return M[0][len(digits) - 1]



if __name__ == "__main__":
    print(find_maximum_value(input()))
