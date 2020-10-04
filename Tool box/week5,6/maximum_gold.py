# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)


    #solution
    value = [[0]*(len(weights)+1) for _ in range(capacity+1)]
    for i in range(1,len(weights)+1):
        for j in range(1,capacity+1):
            value[j][i] = value[j][i-1]
            if weights[i-1] <= j:
                val = value[j-weights[i-1]][i-1] + weights[i-1]
                if val >= value[j][i]:
                    value[j][i] = val
    return value[capacity][len(weights)]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
