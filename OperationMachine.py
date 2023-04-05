# функция отделения от написаной строки операнда запоминание его позиции
def operation_machine(string, i, positions):
    operations = ['*', '/', '+', '-', '=']
    help_operations = ['(', ')']
    temp_input = ''
    position_start = i
    counter = 0
    while string[i] in operations or string[i] in help_operations:
        temp_input += string[i]
        counter += 1
        positions.append(i)
        i += 1
        if i == len(string):
            break
    position_end = position_start + counter - 1
    return temp_input, i, position_start, position_end, positions
