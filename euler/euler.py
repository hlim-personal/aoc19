def is_evenly_divisible(number, ceil):
    for n in range(1, ceil + 1):
        if number % n != 0:
            return False
    return True


def find_smallest():
    i = 10000
    while True:
        if is_evenly_divisible(i, 20):
            print(i)
            break
        i += 1


find_smallest()
