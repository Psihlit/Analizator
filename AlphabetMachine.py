# функция отделения от написаной строки переменной (буква(ы) + цифра(ы)) и запоминание позиции этой переменной
def alphabet_machine(string, i, positions):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    temp_input = ''
    position_start = i
    counter = 0
    while string[i] in alphabet or string[i] in numbers:
        temp_input += string[i]
        counter += 1
        positions.append(i)
        i += 1
        if i == len(string):
            break
    position_end = position_start + counter - 1
    return temp_input, i, position_start, position_end, positions
