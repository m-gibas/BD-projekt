# funkcje długości

def filmID(conn):
    cur = conn.cursor()
    cur.callproc('filmID')
    out = cur.fetchone()
    cur.close()
    return out[0]

def kinoID(conn):
    cur = conn.cursor()
    cur.callproc('kinoID')
    out = cur.fetchone()
    cur.close()
    return out[0]

def aktorID(conn):
    cur = conn.cursor()
    cur.callproc('aktorID')
    out = cur.fetchone()
    cur.close()
    return out[0]

def rezyserID(conn):
    cur = conn.cursor()
    cur.callproc('rezyserID')
    out = cur.fetchone()
    cur.close()
    return out[0]

def aktorFilmID(conn):
    cur = conn.cursor()
    cur.callproc('aktorFilmID')
    out = cur.fetchone()
    cur.close()
    return out[0]

def seansID(conn):
    cur = conn.cursor()
    cur.callproc('seansID')
    out = cur.fetchone()
    cur.close()
    return out[0]

def uzytkownikID(conn):
    cur = conn.cursor()
    cur.callproc('uzytkownikID')
    out = cur.fetchone()
    cur.close()
    return out[0]

# funkcje dodawania

def dodaj_kino(conn, id_kino, nazwa, miasto, kod_pocztowy, ulica, numer_budynku):
    cur = conn.cursor()
    cur.callproc('dodaj_kino', (id_kino, nazwa, miasto, kod_pocztowy, ulica, numer_budynku) )
    conn.commit()
    out = cur.fetchall()
    cur.close()
    return out[0][0]


def dodaj_film(conn, id_film, id_rezyser, tytul, gatunek, rok):
    cur = conn.cursor()
    cur.callproc('dodaj_film', (id_film, id_rezyser, tytul, gatunek, rok) )
    conn.commit()
    out = cur.fetchall()
    cur.close()
    return out[0][0]


def dodaj_aktora(conn, id_aktor, imie, nazwisko, data_urodzenia):
    cur = conn.cursor()
    cur.callproc('dodaj_aktora', (id_aktor, imie, nazwisko, data_urodzenia) )
    conn.commit()
    out = cur.fetchall()
    cur.close()
    return out[0][0]


def dodaj_rezysera(conn, id_aktor, imie, nazwisko, data_urodzenia):
    cur = conn.cursor()
    cur.callproc('dodaj_rezysera', (id_aktor, imie, nazwisko, data_urodzenia) )
    conn.commit()
    out = cur.fetchall()
    cur.close()
    return out[0][0]


def dodaj_aktorFilm(conn, id, id_aktor, id_film):
    cur = conn.cursor()
    cur.callproc('dodaj_aktorFilm', (id, id_aktor, id_film) )
    conn.commit()
    out = cur.fetchall()
    cur.close()
    return out[0][0]


def dodaj_seans(conn, id_seans, id_kino, id_film, data, godzina):
    cur = conn.cursor()
    cur.callproc('dodaj_seans', (id_seans, id_kino, id_film, data, godzina) )
    conn.commit()
    out = cur.fetchall()
    cur.close()
    return out[0][0]


def dodaj_uzytkownika(conn, id, login, haslo):
    cur = conn.cursor()
    cur.callproc('dodaj_uzytkownika', (id, login, haslo) )
    conn.commit()
    out = cur.fetchall()
    cur.close()
    return out[0][0]


# funkcje zwracające SELECTy

def pokaz_kina(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM kino')
    wynik = cur.fetchall()
    nazwy = [opis[0] for opis in cur.description]
    cur.close()
    return nazwy, wynik

def pokaz_seanse(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM seans')
    wynik = cur.fetchall()
    nazwy = [opis[0] for opis in cur.description]
    cur.close()
    return nazwy, wynik

def pokaz_filmy(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM film')
    wynik = cur.fetchall()
    nazwy = [opis[0] for opis in cur.description]
    cur.close()
    return nazwy, wynik

def pokaz_aktorow(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM aktor')
    wynik = cur.fetchall()
    nazwy = [opis[0] for opis in cur.description]
    cur.close()
    return nazwy, wynik

def pokaz_rezyserow(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM rezyser')
    wynik = cur.fetchall()
    nazwy = [opis[0] for opis in cur.description]
    cur.close()
    return nazwy, wynik

# funkcje widoków

def pokaz_aktorzyFilmu(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM aktorzyFilmu')
    wynik = cur.fetchall()
    nazwy = [opis[0] for opis in cur.description]
    cur.close()
    return nazwy, wynik

def pokaz_filmyRezysera(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM filmyRezysera')
    wynik = cur.fetchall()
    nazwy = [opis[0] for opis in cur.description]
    cur.close()
    return nazwy, wynik

def pokaz_seanseKina(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM seanseKina')
    wynik = cur.fetchall()
    nazwy = [opis[0] for opis in cur.description]
    cur.close()
    return nazwy, wynik

def pokaz_iloscFilmowRezysera(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM iloscFilmowRezysera')
    wynik = cur.fetchall()
    nazwy = [opis[0] for opis in cur.description]
    cur.close()
    return nazwy, wynik

def pokaz_iloscAktorowFilmu(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM iloscAktorowFilmu')
    wynik = cur.fetchall()
    nazwy = [opis[0] for opis in cur.description]
    cur.close()
    return nazwy, wynik

def pokaz_iloscSeansowKina(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM iloscSeansowKina')
    wynik = cur.fetchall()
    nazwy = [opis[0] for opis in cur.description]
    cur.close()
    return nazwy, wynik

# logowanie do bazy

def logowanie(conn, login, haslo):
    cur = conn.cursor()
    cur.execute('SELECT * FROM logowanie(\'' + login + '\',\'' + haslo +'\')' )
    wynik = cur.fetchone()
    cur.close()
    return wynik[0]