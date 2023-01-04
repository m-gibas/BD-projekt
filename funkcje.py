import psycopg2


def dodaj_film(conn, id_film, tytul, gatunek, rok):
    cur = conn.cursor()

    cur.callproc('dodaj_film', (id_film, tytul, gatunek, rok) )
    conn.commit()
    out = cur.fetchall()
    cur.close()
    return out


def filmID(conn):
    cur = conn.cursor()
    cur.callproc('filmID')
    # conn.commit()
    out = cur.fetchone()
    cur.close()
    return out[0]
