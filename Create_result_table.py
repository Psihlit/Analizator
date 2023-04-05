import PySimpleGUI as sg


# функция создания окна с таблицей вывода анализа
def create(result_array, headings):
    result_window_layout = [
        [sg.Table(values=result_array, headings=headings, max_col_width=35,
                  auto_size_columns=True,
                  display_row_numbers=False,
                  justification='right',
                  num_rows=10,
                  key='-TABLE-',
                  row_height=35)]
    ]

    result_window = sg.Window("Result", result_window_layout, modal=True)

    while True:
        event, values = result_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        result_window.close()
