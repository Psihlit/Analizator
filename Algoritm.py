from OperationMachine import operation_machine
from NumberMachine import number_machine
from AlphabetMachine import alphabet_machine
from FreeSpaceMachine import free_space_operation
from WrongSymbolMachine import wrong_symbol_operation

# region набор алфавитов
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
help_numbers = [',', '.']
operations = ['*', '/', '+', '-', '=']
help_operations = ['(', ')']
# endregion


def do_analysis(string):
    positions = []
    result_list = []
    # цикл по длине строки, с проверкой на каждый входящий в нее элемент
    # при заходе в часть цикла по логическому обращению, вызывается та или иная функция
    for i in range(len(string)):
        if i not in positions:
            if string[i] in alphabet:
                temp_input, i, position_start, position_end, positions = alphabet_machine(string, i, positions)
                if position_end - position_start == 0:
                    result = [f'{temp_input}', f'{position_start}', 'Обозначение переменной']
                else:
                    result = [f'{temp_input}', f'{position_start}-{position_end}', 'Обозначение переменной']
                result_list.append(result)
                if i == len(string):
                    break
            if string[i] in numbers:
                temp_input, i, position_start, position_end, positions = number_machine(string, i, positions)
                if position_end - position_start == 0:
                    result = [f'{temp_input}', f'{position_start}', 'Обозначение числа']
                else:
                    result = [f'{temp_input}', f'{position_start}-{position_end}', 'Обозначение числа']
                result_list.append(result)
                if i == len(string):
                    break
            if string[i] in operations:
                temp_input, i, position_start, position_end, positions = operation_machine(string, i, positions)
                if position_end - position_start == 0:
                    result = [f'{temp_input}', f'{position_start}', 'Обозначение операции']
                else:
                    result = [f'{temp_input}', f'{position_start}-{position_end}', 'Обозначение операции']
                result_list.append(result)
                if i == len(string):
                    break
            if string[i] == " ":
                temp_input, position, positions = free_space_operation(i, positions)
                result = [f'{temp_input}', f'{position}', 'Пробел']
                result_list.append(result)
            if string[i] != " " and (
                    string[i] not in alphabet or string[i] not in numbers or string[i] not in help_numbers or string[
                i] not in operations or string[i] not in help_operations):
                temp_input, position, positions = wrong_symbol_operation(string, i, positions)
                result = [f'{temp_input}', f'{position}', 'Неизвестный символ']
                result_list.append(result)
        else:
            pass
    return result_list
