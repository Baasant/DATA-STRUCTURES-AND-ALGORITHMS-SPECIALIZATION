# python3
import sys

def compute_operations(n):
    assert 1 <= n <= 10 ** 6

    #try here


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
