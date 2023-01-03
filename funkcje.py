import psycopg2


def dodaj_film(conn, id_film, tytul, gatunek, rok):
    cur = conn.cursor()

    cur.callproc('dodaj_film', (id_film, tytul, gatunek, rok) )
    conn.commit()
    out = cur.fetchall()
    cur.close()
    return out
