import psycopg2

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

# funkcje dodawania

def dodaj_film(conn, id_film, tytul, gatunek, rok):
    cur = conn.cursor()
    cur.callproc('dodaj_film', (id_film, tytul, gatunek, rok) )
    conn.commit()
    out = cur.fetchall()
    cur.close()
    return out[0][0]


def dodaj_kino(conn, id_kino, nazwa, miasto, kod_pocztowy, ulica, numer_budynku):
    cur = conn.cursor()
    cur.callproc('dodaj_film', (id_kino, nazwa, miasto, kod_pocztowy, ulica, numer_budynku) )
    conn.commit()
    out = cur.fetchall()
    cur.close()
    return out[0][0]


