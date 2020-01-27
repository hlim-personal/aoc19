import math


def additional_calc(input):
    trunced = math.trunc(input / 3) - 2
    return trunced


def fuel_reqs():
    sum = 0
    with open("resources/day1.txt") as input:
        modules = input.read().splitlines()
        for x in range(0, len(modules)):
            num = float(modules[x])
            trunced = math.trunc(num / 3) - 2
            sum += trunced
            additional = 0
            while (additional_calc(trunced) > 0):
                additional += additional_calc(trunced)
                trunced = additional_calc(trunced)
            sum += additional

    return sum


print(fuel_reqs())
