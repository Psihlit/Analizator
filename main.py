import PySimpleGUI as sg
from Algoritm import do_analysis
from Create_result_table import create

# создание интерфеса
headings = ['Элемент', 'Позиция', 'Комментарий']

layout = [
    [sg.Text("Введи строку для анализа:"), sg.Input(key='-INPUT_STRING-', do_not_clear=True, size=(20, 1))],
    [sg.Button('Анализировать'), sg.Exit('Выход')]
]

window = sg.Window('Analizator', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Выход'):
        break
    elif event == 'Анализировать':
        string = values['-INPUT_STRING-']
        create(do_analysis(string), headings)
