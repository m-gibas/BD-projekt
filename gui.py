import PySimpleGUI as sg
# import numpy as np
# import matplotlib.pyplot as plt

#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')


        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        
    # moj wlasny select
        print('Moj select: ')
        cur.execute('SELECT * FROM lab03.uczestnik')
        # query = cur.fetchone()
        # print(query)
        query = cur.fetchall()
        for el in query:
            print(el)
        return query
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')





w, h = 640, 480


sg.theme('DarkGreen3')   


layout = [  [sg.Column([[sg.Button('Wyjście' )]], element_justification='right', expand_x=True)],
            [sg.Button("Przeglądaj elementy", pad=(0,10))],
            [sg.Button("Dodaj element", pad=(0,10))],
            [sg.Button("Submit", pad=(0,10))],

            [sg.Text("", key='-OUTPUT-', pad=(0,10))],
            [sg.Listbox(values="", size=(100, 5), key='_LISTBOX_')],
            [sg.Listbox(values="", size=(5, 10), pad=(0, 0), no_scrollbar=True, enable_events=True, key='IDS')],
            [sg.Text(" Nasz obrazek:", key='-TXT-', size=(25, 2), pad=(0, 0), expand_x=True, expand_y=False, visible=False),
            sg.Text(" Obraz przewidzianego pająka:", key='-TXT2-', size=(25, 2), pad=(0, 0), expand_x=True, expand_y=False, visible=False)],
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
  
    if event == "Dodaj element":
        window['-OUTPUT-'].update(value = " Dodaj element : ")
        window['-TXT-'].update(visible=True)
        window['-TXT2-'].update(visible=True)

    if event == "Submit":
        window['-OUTPUT-'].update(value = " Nasza predykcja: ")
        window['-TXT-'].update(visible=True)
        window['-TXT2-'].update(visible=True) 


window.close()