# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d




    sp= 0
    last_stop_value = 0
    index = 0
    stops.append(d)
    while index< len(stops):
        if stops[index]-last_stop_value<=m:
            index+=1
            continue
        elif stops[index] - stops[index-1] > m or index == 0:
            return -1
        else:
            last_stop_value = stops[index-1]
            sp+=1
    return sp









if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
