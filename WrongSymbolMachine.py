# функция отделения от написаной строки неопознанного символа и запоминание его позиции
def wrong_symbol_operation(string, i, positions):
    temp_input = string[i]
    position = i
    positions.append(i)
    return temp_input, position, positions