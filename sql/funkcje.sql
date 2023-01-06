-- SET search_path to projekt;


-- funkcje zwaracania długości (ostatnie ID)

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

CREATE OR REPLACE FUNCTION aktorID()
RETURNS INTEGER AS
$$
BEGIN
    RETURN (SELECT id_aktor FROM aktor 
    ORDER BY id_aktor DESC 
    LIMIT 1);
END;
$$
LANGUAGE 'plpgsql'; 
-- SELECT * FROM aktorID()

CREATE OR REPLACE FUNCTION rezyserID()
RETURNS INTEGER AS
$$
BEGIN
    RETURN (SELECT id_rezyser FROM rezyser 
    ORDER BY id_rezyser DESC 
    LIMIT 1);
END;
$$
LANGUAGE 'plpgsql'; 
-- SELECT * FROM rezyserID()

CREATE OR REPLACE FUNCTION aktorFilmID()
RETURNS INTEGER AS
$$
BEGIN
    RETURN (SELECT id FROM aktor_film 
    ORDER BY id DESC 
    LIMIT 1);
END;
$$
LANGUAGE 'plpgsql'; 
-- SELECT * FROM aktorFilmID()

CREATE OR REPLACE FUNCTION seansID()
RETURNS INTEGER AS
$$
BEGIN
    RETURN (SELECT id_seans FROM seans 
    ORDER BY id_seans DESC 
    LIMIT 1);
END;
$$
LANGUAGE 'plpgsql'; 
-- SELECT * FROM seansID()



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


CREATE OR REPLACE FUNCTION dodaj_aktora(id_aktor BIGINT, imie VARCHAR, nazwisko VARCHAR, data_urodzenia DATE)
RETURNS TEXT AS
$$
DECLARE
    wynik TEXT;
BEGIN
    INSERT INTO aktor(id_aktor, imie, nazwisko, data_urodzenia) 
    VALUES(id_aktor, imie, nazwisko, data_urodzenia);
    wynik := 'Dodano aktora o parametrach: id=' || id_aktor || ', imię=' || imie || ', nazwisko=' || nazwisko || ', data=' || data_urodzenia;
    RETURN wynik;
END;
$$
LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION dodaj_rezysera(id_rezyser BIGINT, imie VARCHAR, nazwisko VARCHAR, data_urodzenia DATE)
RETURNS TEXT AS
$$
DECLARE
    wynik TEXT;
BEGIN
    INSERT INTO rezyser(id_rezyser, imie, nazwisko, data_urodzenia) 
    VALUES(id_rezyser, imie, nazwisko, data_urodzenia);
    wynik := 'Dodano reżysera o parametrach: id=' || id_rezyser || ', imię=' || imie || ', nazwisko=' || nazwisko || ', data=' || data_urodzenia;
    RETURN wynik;
END;
$$
LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION dodaj_aktorFilm(id BIGINT, id_aktor BIGINT, id_film BIGINT)
RETURNS TEXT AS
$$
DECLARE
    wynik TEXT;
BEGIN
    INSERT INTO aktor_film(id, id_aktor, id_film) 
    VALUES(id, id_aktor, id_film);
    wynik := 'Dodano aktora do filmu';
    RETURN wynik;
END;
$$
LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION dodaj_seans(id_seans BIGINT, id_kino BIGINT, id_film BIGINT, data DATE, godzina TIME)
RETURNS TEXT AS
$$
DECLARE
    wynik TEXT;
BEGIN
    INSERT INTO seans(id_seans, id_kino, id_film, data, godzina) 
    VALUES(id_seans, id_kino, id_film, data, godzina) ;
    wynik := 'Dodano seans o parametrach: id=' || id_seans || ', data=' || data || ', godzina=' || godzina;
    RETURN wynik;
END;
$$
LANGUAGE 'plpgsql';