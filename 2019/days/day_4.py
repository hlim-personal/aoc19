outliers = []


def parse_password(pw):
    digits = [int(n) for n in str(pw)]
    adjacents = {}
    prev_digit = None

    for x in range(len(digits)):
        if prev_digit:
            if prev_digit > digits[x]:
                return False
            elif prev_digit == digits[x]:
                adjacents[prev_digit] += 1
            else:
                adjacents[digits[x]] = 1
        else:
            adjacents[digits[x]] = 1
        prev_digit = digits[x]

    for amount in adjacents:
        if adjacents[amount] == 2:
            outliers.append(pw)
            return


def get_answer(floor, ceil):
    for x in range(floor, ceil):
        parse_password(x)
    print(len(outliers))


get_answer(256310, 732736)
