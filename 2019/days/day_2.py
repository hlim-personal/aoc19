from Intcode import Computer


def __main__():
    with open("2019/resources/txt/day2.txt") as txt:
        instructions = txt.read()
        instructions = instructions.split(',')
        for i in range(len(instructions)):
            instructions[i] = int(instructions[i])

        # part one
        instructions[1] = 12
        instructions[2] = 2

        comp1 = Computer(instructions)
        comp1.run()
        print(comp1.program[0])

        # part two
        for x in range(100):
            for y in range(100):
                instructions[1] = x
                instructions[2] = y

                comp2 = Computer(instructions)
                comp2.run()

                if comp2.program[0] == 19690720:
                    print(x, y)
                    break


__main__()
