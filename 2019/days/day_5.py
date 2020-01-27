from Intcode import Computer


def __main__():
    with open("2019/resources/txt/day5.txt") as txt:
        instructions = txt.read()
        instructions = instructions.split(',')
        instructions = [int(x) for x in instructions]

        # part 1
        comp1 = Computer(instructions)
        comp1.input_1 = 1
        comp1.run()

        # part 2
        comp2 = Computer(instructions)
        comp2.input_1 = 5
        comp2.run()


__main__()
