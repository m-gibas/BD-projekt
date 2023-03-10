SET search_path to projekt;


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

CREATE OR REPLACE FUNCTION uzytkownikID()
RETURNS INTEGER AS
$$
BEGIN
    RETURN (SELECT id FROM uzytkownik 
    ORDER BY uzytkownik DESC 
    LIMIT 1);
END;
$$
LANGUAGE 'plpgsql'; 
-- SELECT * FROM seansID()


-- funkcje dodawania rekordów

CREATE OR REPLACE FUNCTION dodaj_film(id_film BIGINT, id_rezyser BIGINT, tytul VARCHAR, gatunek VARCHAR, rok INTEGER)
RETURNS TEXT AS
$$
DECLARE
    wynik TEXT;
BEGIN
    IF rok < 1895 THEN
        RAISE EXCEPTION 'Przed 1895r nie było filmów!';
    END IF;
    IF tytul !~* '[a-z0-9]' THEN
        RAISE EXCEPTION 'Tytuł musi zawierać jakieś znaki!';
    END IF;
    IF gatunek !~* '[a-z]' THEN
        RAISE EXCEPTION 'Gatunek musi zawierać jakieś znaki i zaczynać się od litery!';
    END IF;
    INSERT INTO film(id_film, id_rezyser, tytul, gatunek, rok) 
    VALUES(id_film, id_rezyser, tytul, gatunek, rok);
    wynik := 'Dodano film o parametrach: id=' || id_film || ', id reżysera=' || id_rezyser || ', tytuł=' || tytul || ', gatunek=' || gatunek || ', rok=' || rok;
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
    IF nazwa !~* '[a-z]' THEN
        RAISE EXCEPTION 'Nazwa musi zawierać jakieś znaki i zaczynać się od litery!';
    END IF;
    IF miasto !~* '[a-z]' THEN
        RAISE EXCEPTION 'Miasto musi zawierać jakieś znaki i zaczynać się od litery!';
    END IF;
    IF ulica !~* '[a-z0-9]' THEN
        RAISE EXCEPTION 'Ulica musi zawierać jakieś znaki!';
    END IF;
    IF kod_pocztowy !~* '[0-9]' THEN
        RAISE EXCEPTION 'Kod pocztowy musi zawierać jakieś cyfry!';
    END IF;

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
    IF imie !~* '[a-z]' THEN
        RAISE EXCEPTION 'Imie musi zawierać jakieś znaki i zaczynać się od litery!';
    END IF;
    IF nazwisko !~* '[a-z]' THEN
        RAISE EXCEPTION 'Nazwisko musi zawierać jakieś znaki i zaczynać się od litery!';
    END IF;
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
    IF imie !~* '[a-z]' THEN
        RAISE EXCEPTION 'Imie musi zawierać jakieś znaki i zaczynać się od litery!';
    END IF;
    IF nazwisko !~* '[a-z]' THEN
        RAISE EXCEPTION 'Nazwisko musi zawierać jakieś znaki i zaczynać się od litery!';
    END IF;
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


CREATE OR REPLACE FUNCTION dodaj_uzytkownika(id BIGINT, login VARCHAR, haslo VARCHAR)
RETURNS TEXT AS
$$
DECLARE
    wynik TEXT;
BEGIN
    IF login !~* '[a-z0-9]' THEN
        RAISE EXCEPTION 'Login musi zawierać jakieś znaki!';
    END IF;
    IF haslo !~* '[a-z0-9]' THEN
        RAISE EXCEPTION 'Haslo musi zawierać jakieś znaki!';
    END IF;
    INSERT INTO uzytkownik(id, login, haslo) 
    VALUES(id, login, haslo) ;
    wynik := 'Dodano użytkownika o parametrach: id=' || id || ', login=' || login;
    RETURN wynik;
END;
$$
LANGUAGE 'plpgsql';


-- widoki danych z tabel

-- DROP VIEW aktorzyFilmu
CREATE OR REPLACE VIEW aktorzyFilmu 
AS
SELECT f.tytul AS "Tytuł filmu", a.imie AS "Imię aktora", a.nazwisko AS "Nazwisko aktora", a.data_urodzenia AS "Data urodzenia", date_part('year', age(a.data_urodzenia))::int AS "Wiek"  FROM aktor_film af
JOIN film f USING (id_film)
JOIN aktor a USING (id_aktor)
WHERE f.id_film = af.id_film
ORDER BY 1, 3, 2;
-- SELECT * FROM aktorzyFilmu;


CREATE OR REPLACE VIEW filmyRezysera 
AS
SELECT r.imie AS "Imię reżysera", r.nazwisko AS "Nazwisko reżysera", r.data_urodzenia AS "Data urodzenia", date_part('year', age(r.data_urodzenia))::int AS "wiek", f.tytul AS "Tytuł filmu" FROM film f
JOIN rezyser r USING (id_rezyser)
WHERE f.id_rezyser = r.id_rezyser
ORDER BY 2, 1, 5;
-- SELECT * FROM filmyRezysera;


CREATE OR REPLACE VIEW seanseKina 
AS
SELECT f.tytul "Tytuł filmu", (s.data + s.godzina) AS "Data wydarzenia", k.nazwa AS "Nazwa kina" FROM seans s
JOIN film f USING (id_film)
JOIN kino k USING (id_kino)
WHERE f.id_film = s.id_film AND k.id_kino = s.id_kino
ORDER BY 1, 2, 3;
-- SELECT * FROM seanseKina;


-- funkcja logowania

CREATE OR REPLACE FUNCTION logowanie(login2 VARCHAR, haslo2 VARCHAR)
RETURNS TEXT AS
$$
DECLARE
    wynik INTEGER;
BEGIN
    wynik := (
		SELECT id FROM uzytkownik u
		WHERE haslo LIKE haslo2 AND login LIKE login2
	);
    RETURN wynik;
END;
$$
LANGUAGE 'plpgsql';

-- SELECT * FROM logowanie('admin', 'admin');


-- funkcje zliczania ilości

CREATE OR REPLACE VIEW iloscFilmowRezysera 
AS
SELECT "Imię reżysera", "Nazwisko reżysera", COUNT(*) AS "Ilość filmów" FROM filmyRezysera
GROUP BY 2, 1
ORDER BY 2, 1, 3;

CREATE OR REPLACE VIEW iloscAktorowFilmu 
AS
SELECT "Tytuł filmu", COUNT(*) AS "Ilość aktorów" FROM aktorzyFilmu
GROUP BY 1
ORDER BY 1, 2;

CREATE OR REPLACE VIEW iloscSeansowKina
AS
SELECT "Nazwa kina", COUNT(*) AS "Ilość seansów" FROM seanseKina
GROUP BY 1
ORDER BY 1, 2;


-- triggery do sprawdzania poprawności danych

DROP TRIGGER sprawdz_date_aktora ON aktor;
DROP TRIGGER sprawdz_date_rezysera ON rezyser;
DROP TRIGGER sprawdz_date_seansu ON seans;


CREATE OR REPLACE FUNCTION sprawdz_date()
RETURNS TRIGGER AS
$$
BEGIN
    IF NEW.data_urodzenia > CURRENT_TIMESTAMP THEN
        RAISE EXCEPTION 'Data urodzenia nie może być później niż aktualny czas!';
    ELSE
        RETURN NEW;
    END IF;
END;
$$
LANGUAGE 'plpgsql';  

CREATE TRIGGER sprawdz_date_aktora
BEFORE INSERT OR UPDATE OF data_urodzenia ON aktor
FOR EACH ROW
EXECUTE FUNCTION sprawdz_date();

CREATE TRIGGER sprawdz_date_rezysera
BEFORE INSERT OR UPDATE OF data_urodzenia ON rezyser
FOR EACH ROW
EXECUTE FUNCTION sprawdz_date();


CREATE OR REPLACE FUNCTION sprawdz_date_seans()
RETURNS TRIGGER AS
$$
BEGIN
    IF NEW.data < CURRENT_TIMESTAMP THEN
        RAISE EXCEPTION 'Wydarzenie nie może się odbyć w przeszłości!';
    ELSE
        RETURN NEW;
    END IF;
END;
$$
LANGUAGE 'plpgsql';  

CREATE TRIGGER sprawdz_date_seansu
BEFORE INSERT OR UPDATE OF data ON seans
FOR EACH ROW
EXECUTE FUNCTION sprawdz_date_seans();