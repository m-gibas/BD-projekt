import PySimpleGUI as sg
import funkcje
from config import connect, disconnect

# połączenie z bazą i nadanie odpowiedniej ścieżki
if __name__ == '__main__':
    conn = connect()
    cur = conn.cursor()
    cur.execute("SET search_path TO projekt;")

# rodzaj wyglądu aplikacji
sg.theme('DarkGreen3')   

# wszystkie potrzebne widoki aplikacji
widokLogowanie = [[
            [sg.Text('Login: '), sg.Input('', size=(12,2), pad=(10,10), key='login'),
            sg.Text('Hasło: '), sg.Input('', size=(12,2), key='haslo'),],
            [sg.Button("Logowanie", pad=(8,10), key='logowanie'),
            sg.Button("Rejestracja", pad=(8,10), key='rejestracja'),]
            ]]
            
widokDodajKino = [[
            sg.Button("Dodaj", pad=(8,10), key='dodajKino'),
            sg.Text('Nazwa: '), sg.Input('', size=(12,2), key='nazwaKino'),
            sg.Text('Miasto: '), sg.Input('', size=(12,2), key='miastoKino'),
            sg.Text('Kod pocztowy: '), sg.Input('', size=(6,2), key='kodKino'),
            sg.Text('Ulica: '), sg.Input('', size=(12,2), key='ulicaKino'),
            sg.Text('Numer budynku: '), sg.Input('', size=(3,2), key='numerKino'),
            ]]

widokDodajFilm = [[
            sg.Button("Dodaj", pad=(8,10), key='dodajFilm'),
            sg.Text('ID reżysera: '), sg.Input('', size=(3,2), key='idRezyserFilm'),
            sg.Text('Tytuł: '), sg.Input('', size=(16,2), key='tytulFilm'),
            sg.Text('Gatunek: '), sg.Input('', size=(10,2), key='gatunekFilm'),
            sg.Text('Rok wydania: '), sg.Input('', size=(4,2), key='rokFilm'),
            ]]

widokDodajAktora = [[
            sg.Button("Dodaj", pad=(8,10), key='dodajAktora'),
            sg.Text('Imię: '), sg.Input('', size=(10,2), key='imieAktor'),
            sg.Text('Nazwisko: '), sg.Input('', size=(10,2), key='nazwiskoAktor'),
            sg.Text('Data urodzenia (w formacie \'YYYY-MM-DD\'): '), sg.Input('', size=(10,2), key='dataAktor'),
            ]]

widokDodajRezysera = [[
            sg.Button("Dodaj", pad=(8,10), key='dodajRezysera'),
            sg.Text('Imię: '), sg.Input('', size=(10,2), key='imieRezyser'),
            sg.Text('Nazwisko: '), sg.Input('', size=(10,2), key='nazwiskoRezyser'),
            sg.Text('Data urodzenia (w formacie \'YYYY-MM-DD\'): '), sg.Input('', size=(10,2), key='dataRezyser'),
            ]]

widokDodajAktoraDoFilmu = [[
            sg.Button("Przypisz", pad=(8,10), key='dodajAktoraDoFilmu'),
            sg.Text('ID aktora: '), sg.Input('', size=(3,2), key='idAktor'),
            sg.Text('ID filmu: '), sg.Input('', size=(3,2), key='idFilm'),
            ]]

widokDodajSeans = [[
            sg.Button("Przypisz", pad=(8,10), key='dodajSeans'),
            sg.Text('ID kina: '), sg.Input('', size=(3,2), key='idKinoSeans'),
            sg.Text('ID filmu: '), sg.Input('', size=(3,2), key='idFilmSeans'),
            sg.Text('Data wydarzenia (w formacie \'YYYY-MM-DD\'): '), sg.Input('', size=(10,2), key='dataSeans'),
            sg.Text('Godzina wydarzenia (w formacie \'HH:MM\'): '), sg.Input('', size=(5,2), key='godzinaSeans'),
            ]]



# funkcja do pokazywania okna z wartościami tabel (danymi)
def otworz_liste(nazwy, wartosci):
    layout = [
        [sg.Table(values=wartosci, headings=nazwy, key='lista')],
        ]
    window = sg.Window("Lista", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Wyjście" or event == sg.WIN_CLOSED:
            break
    window.close()

# funkcja do pokazywania okna z raportami
def otworz_liste2(arr):
    layout = [
        [sg.Table(values=arr[1], headings=arr[0], key='lista')],
        [sg.Table(values=arr[3], headings=arr[2], key='lista')],
        ]
    window = sg.Window("Lista", layout, modal=True)
    while True:
        event, values = window.read()
        if event == "Wyjście" or event == sg.WIN_CLOSED:
            break
    window.close()


# główny widok posiadający wszystkie potrzebne podwidoki 
layout = [  [sg.Column([[sg.Button('Wyjście' )]], element_justification='right', expand_x=True)],

            [sg.Frame('Dodaj kino', widokDodajKino, title_color='chocolate2', border_width=5)],
            [sg.Frame('Dodaj film', widokDodajFilm, title_color='chocolate2', border_width=5)],
            [sg.Frame('Dodaj aktora', widokDodajAktora, title_color='chocolate2', border_width=5)],
            [sg.Frame('Dodaj reżysera', widokDodajRezysera, title_color='chocolate2', border_width=5)],
            [sg.Frame('Przypisz aktora do filmu', widokDodajAktoraDoFilmu, title_color='chocolate2', border_width=5),
            sg.Button("Pokaż kina", pad=(10,0), key='pokaz_kina'),
            sg.Button("Pokaż seanse", pad=(10,0), key='pokaz_seanse'),
            sg.Button("Pokaż filmy", pad=(10,0), key='pokaz_filmy'),
            sg.Button("Pokaż aktorów", pad=(10,0), key='pokaz_aktorow'),
            sg.Button("Pokaż reżyserów", pad=(10,0), key='pokaz_rezyserow'),
            ],
            [sg.Frame('Przypisz seans do kina', widokDodajSeans, title_color='chocolate2', border_width=5)],
            [sg.Frame('Raporty', 
                [[sg.Button("Pokaż aktorów filmów", pad=(10,20), key='pokaz_aktorzyFilmu'),
                sg.Button("Pokaż filmy reżyserów", pad=(10,0), key='pokaz_filmyRezysera'),
                sg.Button("Pokaż seanse kin", pad=(10,0), key='pokaz_seanseKina'),
                ]],
            pad=(10,10) ,title_color='chocolate2', border_width=5)],
            ]




# okno wyświetlające główną zawartość programu
def glowne_okno():
    window = sg.Window('Kino', layout, size=(1000, 700), finalize=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Wyjście':
            break

    # funkcje dodawania elementów

        if event == 'dodajKino':
            len = funkcje.kinoID(conn)
            if(len == None): len = 0
            sg.popup('Kino', funkcje.dodaj_kino(conn, len+1, values['nazwaKino'], values['miastoKino'],  values['kodKino'],  values['ulicaKino'], int(values['numerKino'])))
    
        if event == 'dodajFilm':
            len = funkcje.filmID(conn)
            if(len == None): len = 0
            # print(len)
            sg.popup('Film', funkcje.dodaj_film(conn, len+1, values['idRezyserFilm'], values['tytulFilm'], values['gatunekFilm'], int(values['rokFilm'])))

        if event == 'dodajAktora':
            len = funkcje.aktorID(conn)
            if(len == None): len = 0
            sg.popup('Aktor', funkcje.dodaj_aktora(conn, len+1, values['imieAktor'],  values['nazwiskoAktor'], values['dataAktor']))
    
        if event == 'dodajRezysera':
            len = funkcje.rezyserID(conn)
            if(len == None): len = 0
            sg.popup('Rezyser', funkcje.dodaj_rezysera(conn, len+1, values['imieRezyser'],  values['nazwiskoRezyser'], values['dataRezyser'] ))
    
        if event == 'dodajAktoraDoFilmu':
            len = funkcje.aktorFilmID(conn)
            if(len == None): len = 0
            sg.popup('Aktor do filmu', funkcje.dodaj_aktorFilm(conn, len+1, int(values['idAktor']), int(values['idFilm']) ))
    
        if event == 'dodajSeans':
            len = funkcje.seansID(conn)
            if(len == None): len = 0
            sg.popup('Seans', funkcje.dodaj_seans(conn, len+1, int(values['idKinoSeans']), int(values['idFilmSeans']), values['dataSeans'], values['godzinaSeans']))
    

    # funkcje pokazywania tabel

        if event == "pokaz_kina":
            nazwy, wartosci = funkcje.pokaz_kina(conn)
            otworz_liste(nazwy, wartosci)

        if event == "pokaz_seanse":
            nazwy, wartosci = funkcje.pokaz_seanse(conn)
            otworz_liste(nazwy, wartosci)

        if event == "pokaz_filmy":
            nazwy, wartosci = funkcje.pokaz_filmy(conn)
            otworz_liste(nazwy, wartosci)

        if event == "pokaz_aktorow":
            nazwy, wartosci = funkcje.pokaz_aktorow(conn)
            otworz_liste(nazwy, wartosci)

        if event == "pokaz_rezyserow":
            nazwy, wartosci = funkcje.pokaz_rezyserow(conn)
            otworz_liste(nazwy, wartosci)

    # funkcje wyświetlania raportów

        if event == "pokaz_aktorzyFilmu":
            nazwy, wartosci = funkcje.pokaz_aktorzyFilmu(conn)
            nazwy2, wartosci2 = funkcje.pokaz_iloscAktorowFilmu(conn)
            otworz_liste2([nazwy, wartosci, nazwy2, wartosci2])

        if event == "pokaz_filmyRezysera":
            nazwy, wartosci = funkcje.pokaz_filmyRezysera(conn)
            nazwy2, wartosci2 = funkcje.pokaz_iloscFilmowRezysera(conn)
            otworz_liste2([nazwy, wartosci, nazwy2, wartosci2])

        if event == "pokaz_seanseKina":
            nazwy, wartosci = funkcje.pokaz_seanseKina(conn)
            nazwy2, wartosci2 = funkcje.pokaz_iloscSeansowKina(conn)
            otworz_liste2([nazwy, wartosci, nazwy2, wartosci2])


    window.close()
    disconnect(conn)


# okno logowania i rejestracji do systemu
window = sg.Window("Logowanie", widokLogowanie, modal=True)
while True:
    event, values = window.read()
    if event == "Wyjście" or event == sg.WIN_CLOSED:
        break

    if event == "rejestracja":
        len = funkcje.uzytkownikID(conn)
        if(len == None): len = 0
        sg.popup('Użytkownik', funkcje.dodaj_uzytkownika(conn, len+1, values['login'], values['haslo']))

    if event == "logowanie":
        if funkcje.logowanie(conn, values['login'], values['haslo']) != None:
            window.close()
            glowne_okno()
