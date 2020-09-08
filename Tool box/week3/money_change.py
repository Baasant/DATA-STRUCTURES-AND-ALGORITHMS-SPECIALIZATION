# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    m=money
    return m//10 + (m%10)//5 + (m%5)
    '''''
    m=money
    result=0
    coins=[10,5,1]
    while m != 0:
        for coin in coins:
            if (m - coin >= 0):
                m -= coin
                result = result+1
                break
    return result

'''''







if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
