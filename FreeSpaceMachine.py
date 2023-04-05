# функция отделения от написаной строки пробела и запоминание его позиции
def free_space_operation(i, positions):
    temp_input = '_'
    position = i
    positions.append(i)
    return temp_input, position, positions