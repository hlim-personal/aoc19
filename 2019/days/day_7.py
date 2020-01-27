from Intcode import Computer


def get_phase_settings(is_second=False):
    fact_list = [0, 1, 2, 3, 4] if is_second is False else [5, 6, 7, 8, 9]
    fact_lists = []
    for i in fact_list:
        fact_list_1 = fact_list.copy()
        fact_list_1.remove(i)
        output_list_1 = [i]

        for j in fact_list_1:
            fact_list_2 = fact_list_1.copy()
            fact_list_2.remove(j)
            output_list_2 = output_list_1.copy()
            output_list_2.append(j)

            for k in fact_list_2:
                fact_list_3 = fact_list_2.copy()
                fact_list_3.remove(k)
                output_list_3 = output_list_2.copy()
                output_list_3.append(k)

                for m in fact_list_3:
                    fact_list_4 = fact_list_3.copy()
                    fact_list_4.remove(m)
                    output_list_4 = output_list_3.copy()
                    output_list_4.append(m)
                    output_list_4.append(fact_list_4[0])
                    fact_lists.append(output_list_4)

    return fact_lists


def part_a(instructions):

    phase_settings = get_phase_settings()
    best_score = 0
    for i in range(len(phase_settings)):
        phase_setting = phase_settings[i]

        amp_a, amp_b, amp_c, amp_d, amp_e = Computer(instructions), Computer(
            instructions), Computer(instructions), Computer(instructions), Computer(instructions)

        amp_a.input_1 = phase_setting[0]
        amp_b.input_1 = phase_setting[1]
        amp_c.input_1 = phase_setting[2]
        amp_d.input_1 = phase_setting[3]
        amp_e.input_1 = phase_setting[4]

        amp_a.input_2 = 0
        amp_a.run()

        amp_b.input_2 = amp_a.output_signal
        amp_b.run()

        amp_c.input_2 = amp_b.output_signal
        amp_c.run()

        amp_d.input_2 = amp_c.output_signal
        amp_d.run()

        amp_e.input_2 = amp_d.output_signal
        amp_e.run()

        if amp_e.output_signal > best_score:
            best_score = amp_e.output_signal

    print("Best score: ", best_score)


def part_b(instructions):

    phase_settings = get_phase_settings(True)
    best_score = 0
    for i in range(len(phase_settings)):
        phase_setting = phase_settings[i]

        amp_a, amp_b, amp_c, amp_d, amp_e = Computer(instructions), Computer(
            instructions), Computer(instructions), Computer(instructions), Computer(instructions)

        amp_a.input_1 = phase_setting[0]
        amp_a.do_feedback = True
        amp_b.input_1 = phase_setting[1]
        amp_b.do_feedback = True
        amp_c.input_1 = phase_setting[2]
        amp_c.do_feedback = True
        amp_d.input_1 = phase_setting[3]
        amp_d.do_feedback = True
        amp_e.input_1 = phase_setting[4]
        amp_e.do_feedback = True

        initialised = False

        while True:
            amp_a.input_2 = 0 if not initialised else amp_e.output_signal
            amp_a.run()
            initialised = True

            amp_b.input_2 = amp_a.output_signal
            amp_b.run()

            amp_c.input_2 = amp_b.output_signal
            amp_c.run()

            amp_d.input_2 = amp_c.output_signal
            amp_d.run()

            amp_e.input_2 = amp_d.output_signal
            is_complete = amp_e.run()

            if is_complete:
                break

            if amp_e.output_signal > best_score:
                best_score = amp_e.output_signal

    print("Best score: ", best_score)


def __main__():
    with open("2019/resources/txt/day7.txt") as txt:
        instructions = txt.read()
        instructions = instructions.split(",")
        instructions = [int(x) for x in instructions]

        part_a(instructions)
        part_b(instructions)


__main__()
