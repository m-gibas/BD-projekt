-- SET search_path to projekt;


-- funkcje zwaracania długości (ostatnie ID)

CREATE OR REPLACE FUNCTION filmID()
RETURNS INTEGER AS
$$
BEGIN
    RETURN (SELECT id_film FROM film 
    ORDER BY id_film DESC 
    LIMIT 1);
END;
$$
LANGUAGE 'plpgsql'; 
-- SELECT * FROM filmID()

CREATE OR REPLACE FUNCTION kinoID()
RETURNS INTEGER AS
$$
BEGIN
    RETURN (SELECT id_kino FROM kino 
    ORDER BY id_kino DESC 
    LIMIT 1);
END;
$$
LANGUAGE 'plpgsql'; 
-- SELECT * FROM kinoID()




-- funkcje dodawania rekordów

CREATE OR REPLACE FUNCTION dodaj_film(id_film BIGINT, tytul VARCHAR, gatunek VARCHAR, rok INTEGER)
RETURNS TEXT AS
$$
DECLARE
    wynik TEXT;
BEGIN
    INSERT INTO film(id_film, tytul, gatunek, rok) 
    VALUES(id_film, tytul, gatunek, rok);
    wynik := 'Dodano film o parametrach: id=' || id_film || ', tytuł=' || tytul || ', gatunek=' || gatunek || ', rok=' || rok;
    RETURN wynik;
END;
$$
LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION dodaj_kino(id_kino BIGINT, nazwa VARCHAR, miasto VARCHAR, kod_pocztowy VARCHAR, ulica VARCHAR, numer_budynku INTEGER)
RETURNS TEXT AS
$$
DECLARE
    wynik TEXT;
BEGIN
    INSERT INTO kino(id_kino, nazwa, miasto, kod_pocztowy, ulica, numer_budynku) 
    VALUES(id_kino, nazwa, miasto, kod_pocztowy, ulica, numer_budynku);
    wynik := 'Dodano kino o parametrach: id=' || id_kino || ', nazwa=' || nazwa || ', adres=' || miasto || ', ' || kod_pocztowy || ', ' || ulica || ', ' || numer_budynku;
    RETURN wynik;
END;
$$
LANGUAGE 'plpgsql';