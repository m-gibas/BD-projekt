-- SET search_path to projekt;

CREATE OR REPLACE FUNCTION dodaj_film(id_film INTEGER, tytul VARCHAR, gatunek VARCHAR, rok INTEGER)
RETURNS TEXT AS
$$
DECLARE
    wynik TEXT;
BEGIN
    INSERT INTO film(id_film, tytul, gatunek, rok) VALUES(id_film, tytul, gatunek, rok);
    wynik := 'Dodano film o parametrach: id=' || id_film || ', tytuł=' || tytul || ', gatunek=' || gatunek || ', rok=' || rok;
    RETURN wynik;
END;
$$
LANGUAGE 'plpgsql';


-- SELECT id_film FROM film
-- ORDER BY id_film DESC
-- LIMIT 1;

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