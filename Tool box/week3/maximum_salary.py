# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest

def is_greater(digit, max_digit):
    return digit + max_digit > max_digit + digit

def largest_number(numbers):
    test_list=numbers
    res = int(max((''.join(i) for i in permutations(str(i)
                     for i in test_list)), key = int))
    return res

    '''''
    #numbers=[21,2]
    str_num = [str(number) for number in numbers]
    a_string = "".join(str_num)
    #print(a_string-2)

    m=[int(i) for i in a_string ]
    #print(m)
    m.sort(reverse=True)
    #print(m)
    x = int("".join(map(str, m)))
    return x
'''''





if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
