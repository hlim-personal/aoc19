
def compare(a, b):

    word_a = [x for x in a]
    word_b = [x for x in b]

    differences = 0
    index = -1
    for i in range(len(word_a)):
        if word_a[i] != word_b[i]:
            differences += 1
            index = i
        if differences > 1:
            return False

    if differences == 1:
        del word_a[index]
        print("".join(word_a))


def test():

    with open("2018.txt") as file:
        inputs = file.read().strip().splitlines()

        # num_twos, num_threes = 0, 0

        # for line in inputs:
        #     a, b = accumulate(line)
        #     num_twos += a
        #     num_threes += b

        for i in range(0, len(inputs)):
            for j in range(1, len(inputs)):
                compare(inputs[i], inputs[j])


test()
