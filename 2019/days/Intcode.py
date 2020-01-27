from enum import Enum


class Computer:
    def __init__(self, program):
        self.program = program.copy()
        self.instruction_pointer = 0
        self.input_1 = None  # phase setting
        self.input_2 = None  # input signal
        self.output_signal = None
        self.has_triggered = None
        self.do_feedback = False
        self.relative_base = 0
        # self.debug_mode = False

    def parse_opcode(self):
        opcode_str = "{:05d}".format(self.program[self.instruction_pointer])
        opcode = Opcode(int(opcode_str[-2:]))
        instructions = Instructions([int(x) for x in opcode_str[:3]])

        return opcode, instructions

    def get_params(self, i, instructions):
        param1, param2 = None, None

        if instructions.first_instruction is Mode.POSITION:
            param1 = self.program[self.program[self.instruction_pointer + 1]]
        elif instructions.first_instruction is Mode.IMMEDIATE:
            param1 = self.program[self.instruction_pointer + 1]

        if i == 1:
            return param1
        elif i == 2:
            if instructions.second_instruction is Mode.POSITION:
                param2 = self.program[self.program[self.instruction_pointer + 2]]
            elif instructions.second_instruction is Mode.IMMEDIATE:
                param2 = self.program[self.instruction_pointer + 2]

            return param1, param2

    def run(self):
        opcode, instructions = self.parse_opcode()

        if opcode is Opcode.FINISH:
            return True

        elif opcode is Opcode.ADD or opcode is Opcode.MULTIPLY:
            overwrite = self.program[self.instruction_pointer +
                                     3]
            param1, param2 = self.get_params(2, instructions)

            if opcode is Opcode.ADD:
                self.program[overwrite] = param1 + param2

            elif opcode is Opcode.MULTIPLY:
                self.program[overwrite] = param1 * param2

            self.instruction_pointer += 4
            return self.run()

        elif opcode is Opcode.STORE:
            overwrite = self.program[self.instruction_pointer +
                                     1]
            self.program[overwrite] = self.input_1 if not self.has_triggered else self.input_2
            self.has_triggered = True
            self.instruction_pointer += 2
            return self.run()

        elif opcode is Opcode.OUTPUT:
            self.output_signal = self.get_params(1, instructions)

            print(self.output_signal)
            self.instruction_pointer += 2

            if self.do_feedback:
                return False

            return self.run()

        elif opcode is Opcode.JUMP_IF_TRUE or opcode is Opcode.JUMP_IF_FALSE:
            param1, param2 = self.get_params(2, instructions)

            if opcode is Opcode.JUMP_IF_TRUE and param1 != 0:
                self.instruction_pointer = param2
                return self.run()

            elif opcode is Opcode.JUMP_IF_FALSE and param1 == 0:
                self.instruction_pointer = param2
                return self.run()

            self.instruction_pointer += 3
            return self.run()

        elif opcode is Opcode.LESS_THAN or opcode is Opcode.EQUALS:
            param1, param2 = self.get_params(2, instructions)
            overwrite = self.program[self.instruction_pointer + 3]

            if opcode is Opcode.LESS_THAN:
                self.program[overwrite] = 1 if param1 < param2 else 0

            elif opcode is Opcode.EQUALS:
                self.program[overwrite] = 1 if param1 == param2 else 0

            self.instruction_pointer += 4
            return self.run()


class Opcode(Enum):
    FINISH = 99
    ADD = 1
    MULTIPLY = 2
    STORE = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8


class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class Instructions:
    def __init__(self, instructions):
        self.first_instruction = self.get_mode(instructions[2])
        self.second_instruction = self.get_mode(instructions[1])
        self.third_instruction = self.get_mode(instructions[0])

    def get_mode(self, instruction):
        if instruction == 0:
            return Mode.POSITION
        elif instruction == 1:
            return Mode.IMMEDIATE
        else:
            raise Exception("not a valid mode")
