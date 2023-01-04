import PySimpleGUI as sg
# import numpy as np
# import matplotlib.pyplot as plt
import funkcje

#!/usr/bin/python
import psycopg2
from config import config



# def connect():
#     """ Connect to the PostgreSQL database server """
#     conn = None
#     try:
#         # read connection parameters
#         params = config()

#         # connect to the PostgreSQL server
#         print('Connecting to the PostgreSQL database...')
#         conn = psycopg2.connect(**params)
		
#         # create a cursor
#         cur = conn.cursor()
        
# 	# execute a statement
#         print('PostgreSQL database version:')
#         cur.execute('SELECT version()')


#         # display the PostgreSQL database server version
#         db_version = cur.fetchone()
#         print(db_version)

        
#     # moj wlasny select
#         print('Moj select: ')
#         cur.execute('SELECT * FROM lab03.uczestnik')
#         # query = cur.fetchone()
#         # print(query)
#         query = cur.fetchall()
#         for el in query:
#             print(el)
#         return query
       
# 	# close the communication with the PostgreSQL
#         cur.close()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()
#             print('Database connection closed.')

def connect():
    """ Funkcja do laczenia uzytkownia z serverem bazy danych postgres"""
    conn = None
    try:
        
        params = config()
        print('Laczenie z baza danych PostgreSQL...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
    # wykorzystane funkcje

        # cur.execute("SELECT * FROM akrobata")
        # out = cur.fetchall()

        # print(out)


	# close the communication with the PostgreSQL
        cur.close()
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return 0


if __name__ == '__main__':
    conn = connect()
    cur = conn.cursor()
    cur.execute("SET search_path TO projekt;")

w, h = 640, 480


sg.theme('DarkGreen3')   

widokDodajFilm = [
            [sg.Button("Dodaj film", pad=(8,10))],
            sg.Text('Tytuł: '), sg.Input('', size=(16,2), key='tytulFilm'),
            sg.Text('Gatunek: '), sg.Input('', size=(10,2), key='gatunekFilm'),
            sg.Text('Rok wydania: '), sg.Input('', size=(4,2), key='rokFilm'),
            ]

widokDodajAktora = [
            [sg.Button("Dodaj aktora:", pad=(8,10))],
            sg.Text('Imię: '), sg.Input('', size=(10,2), key='imieAktor'),
            sg.Text('Nazwisko: '), sg.Input('', size=(10,2), key='nazwiskoAktor'),
            sg.Text('Data urodzenia: rok'), sg.Input('', size=(4,2), key='rokAktor'), sg.Text('miesiąc'), sg.Input('', size=(2,2), key='miesiacAktor'), sg.Text('dzień'), sg.Input('', size=(2,2), key='dzienAktor'),
            ]

layout = [  [sg.Column([[sg.Button('Wyjście' )]], element_justification='right', expand_x=True)],

            widokDodajFilm,
            widokDodajAktora,

            [sg.Button("Przeglądaj elementy", pad=(0,10))],

            [sg.Button("Submit", pad=(0,10))],
            
            [sg.Text("", key='-OUTPUT-', pad=(0,10))],
            [sg.Listbox(values="", size=(100, 5), key='_LISTBOX_')],
            [sg.Listbox(values="", size=(5, 10), pad=(0, 0), no_scrollbar=True, enable_events=True, key='IDS')],
            # [sg.Text(" Nasz obrazek:", key='-TXT-', size=(25, 2), pad=(0, 0), expand_x=True, expand_y=False, visible=False),
            # sg.Text(" Obraz przewidzianego pająka:", key='-TXT2-', size=(25, 2), pad=(0, 0), expand_x=True, expand_y=False, visible=False)],
            ]

# sg.theme_background_color('#FF0000')

window = sg.Window('Kino', layout, size=(1000, 700), finalize=True)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Wyjście':
        break

    if event == "Przeglądaj elementy":
        
        # window['-OUTPUT-'].update(value = " Przeglądaj elementy : ")
        query = connect()
        query2 = ''
        items = ''
        for el in query:
            window['-OUTPUT-'].update(el)
            query2 += str(el)
            items += str(el[0])
            # if query[0] == el:
            #     window['-OUTPUT-'].update(value = el)

        # window['-OUTPUT-'].update(value = query2)
        window['_LISTBOX_'].update(values = query)
        window['IDS'].update(values = items)
        window['-TXT-'].update(visible=True)
        window['-TXT2-'].update(visible=True)
        # sg.popup('test', query[0].split(', ')[0])
  

    if event == 'Dodaj film':
        len = funkcje.filmID(conn)
        # print(len)
        sg.popup('Film', funkcje.dodaj_film(conn, len+1, values['tytulFilm'], values['gatunekFilm'], int(values['rokFilm'])))

    if event == "Submit":
        window['-OUTPUT-'].update(value = " Nasza predykcja: ")
        window['-TXT-'].update(visible=True)
        window['-TXT2-'].update(visible=True) 


window.close()