# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    m=money
    coins = [1, 3, 4]

    min_number_of_coins = [None] * (m + 1)

    min_number_of_coins[0] = 0

    for i in range(1, m + 1):
        min_number_of_coins[i] = 100000
        for whole_coin in coins:
            if i >= whole_coin:
                tmp = min_number_of_coins[i - whole_coin] + 1
                if tmp < min_number_of_coins[i]:
                    min_number_of_coins[i] = tmp
            else:
                break

    return min_number_of_coins[m]



if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
