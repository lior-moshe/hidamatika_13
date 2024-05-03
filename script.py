# Online Python - IDE, Editor, Compiler, Interpreter

def get_serie_starting_from_number(starting_number: int):
    caculated_serie = [starting_number]
    for i in range(4):
        next_number = calculate_next_num(caculated_serie[-1])
        caculated_serie.append(next_number)

    return caculated_serie


def calculate_next_num(current_num: int):
    current_num_as_str = str(current_num)
    current_index = 0
    result = []
    while current_index < len(current_num_as_str):
        current_char = current_num_as_str[current_index]
        reps = get_number_of_repetitions(current_num_as_str[current_index:])
        result += [str(reps), current_char]
        current_index += reps

    result = "".join(result)
    result = int(result)
    return result


def get_number_of_repetitions(number: str):
    index = 0
    while index < len(number) and number[index] == number[0]:
        index += 1

    return index


def is_serie_3_down_1_up(serie_of_numbers: list):
    if serie_of_numbers[0] <= serie_of_numbers[1]:
        return False
    if serie_of_numbers[1] <= serie_of_numbers[2]:
        return False
    if serie_of_numbers[2] <= serie_of_numbers[3]:
        return False
    if serie_of_numbers[3] >= serie_of_numbers[4]:
        return False
    return True


if __name__ == '__main__':

    ammount_of_numbers = 100000000

    for i in range(ammount_of_numbers):
        serie = get_serie_starting_from_number(i)
        print(f"Testing serie: {serie}")
        if is_serie_3_down_1_up(serie):
            print(f"Success: {serie}")
            break

        if i == ammount_of_numbers-1:
            print('Failure... Have not find anything')
