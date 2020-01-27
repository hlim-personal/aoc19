from Intcode import Computer


def __main__():
    with open("2019/resources/txt/day9.txt") as txt:
        instructions = txt.read()
        instructions = instructions.split(',')
        instructions = [int(x) for x in instructions]

        computer = Computer(instructions)
        # computer.input_1 = 1
        computer.run()
        # print(computer.program)


__main__()
