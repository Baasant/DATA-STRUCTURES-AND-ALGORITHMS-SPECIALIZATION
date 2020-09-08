# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []

    # write your code here
    i = 1
    sum_summands = 0
    while sum_summands <= n:
        if (sum_summands + i) <= n:
            summands.append(i)
            sum_summands += i
        else:
            summands[-1] += n - sum_summands
            break
        i = i + 1



    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
