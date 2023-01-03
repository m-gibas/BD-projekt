import PySimpleGUI as sg

# layout = [sg.vtop([sg.Listbox(list(range(10)), size=(5,5)), sg.Multiline(size=(25,10))]),
#           [sg.Button('Ok'), sg.Button('Cancel')]]

layout = [
    [
        sg.Column([
            [sg.Text('Książki:'), sg.Button('Dodaj książke'), sg.Button('Edytuj książke'), sg.Button('Usuń książke')],
            [sg.Table(values=[["cos", "cos2", "cos3"], ["cos4"]], headings=["cos", "cos2"],  key='-BOOKS TABLE-', size=(40, 10))],
            # [sg.Text('Wypożyczenia:'), sg.Button('Wypożycz'), sg.Button('Edytuj wypożyczenie'), sg.Button('Usuń wypożyczenie')],
            # [sg.Table(values="", headings="header_rentals",  key='-RENTALS TABLE-', size=(40, 10))],
            # [sg.Text('Czytelnicy:'), sg.Button('Dodaj czytelnika'), sg.Button('Edytuj czytelnika'), sg.Button('Usuń czytelnika'), sg.Text('Kategorie:'), sg.Button('Dodaj kategorie'), sg.Button('Edytuj kategorie'), sg.Button('Usuń kategorie')],
            # [sg.Table(values="get_readers()", headings="header_readers",  key='-READERS TABLE-', size=(40, 10)),
            # sg.Table(values="get_categories()", headings="header_categories",  key='-CATEGORIES TABLE-', size=(40, 10))],
        ])
]]

window = sg.Window('Element Alignment', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break

window.close()