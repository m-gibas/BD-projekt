CREATE OR REPLACE FUNCTION dodaj_film(id_film INTEGER, tytul VARCHAR, gatunek VARCHAR, rok INTEGER)
RETURNS TEXT AS
$$
DECLARE
    wynik TEXT;
BEGIN
    INSERT INTO film(id_film, tytul, gatunek, rok) VALUES(id_film, tytul, gatunek, rok);
    wynik := 'Dodano film o parametrach: ' || id_film || ' ' || tytul || ' ' || gatunek || ' ' || rok;
    RETURN wynik;
END;
$$
LANGUAGE 'plpgsql';