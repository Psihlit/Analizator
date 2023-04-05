# функция отделения от написаной строки числа (цифра(ы) + разделяющий знак (",",".") и запоминание позиции этого числа
def number_machine(string, i, positions):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    help_numbers = [',', '.']
    temp_input = ''
    position_start = i
    counter = 0
    while string[i] in numbers or string[i] in help_numbers:
        temp_input += string[i]
        counter += 1
        positions.append(i)
        i += 1
        if i == len(string):
            break
    position_end = position_start + counter - 1
    return temp_input, i, position_start, position_end, positions
