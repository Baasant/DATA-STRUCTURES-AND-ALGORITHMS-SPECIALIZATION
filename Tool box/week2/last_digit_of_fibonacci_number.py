# python3


def last_digit_of_fibonacci_number_naive(n):
    assert 0 <= n <= 10 ** 7
    f = [0] * 61;
    f = fib(f, 60);

    return f[n % 60];

def fib(f, n):

    # 0th and 1st number of
    # the series are 0 and 1
    f[0] = 0;
    f[1] = 1;

    # Add the previous 2 numbers
    # in the series and store
    # last digit of result
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 10;

    return f;


    #if n <= 1:
     #   return n

    #return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_of_fibonacci_number(n):
    assert 0 <= n <= 10 ** 7
    f = [0] * 61;
    f = fib(f, 60);

    return f[n % 60];

def fib(f, n):

    # 0th and 1st number of
    # the series are 0 and 1
    f[0] = 0;
    f[1] = 1;

    # Add the previous 2 numbers
    # in the series and store
    # last digit of result
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % 10;

    return f;

    #previous = 0
    #current  = 1
    #for _ in range(n - 1):
     #   previous, current = current, previous + current

    #return current % 10





   # type here


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
