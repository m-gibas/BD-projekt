SET search_path to projekt;

-- kina
INSERT INTO kino(id_kino, nazwa, miasto, kod_pocztowy, ulica, numer_budynku) 
    VALUES(1, 'Cinema City', 'New York', '10001', 'Broadway', '5');
INSERT INTO kino(id_kino, nazwa, miasto, kod_pocztowy, ulica, numer_budynku) 
    VALUES(2, 'Kino Helios', 'Gdańsk', '80-001', 'Grunwaldzka', '1');
INSERT INTO kino(id_kino, nazwa, miasto, kod_pocztowy, ulica, numer_budynku) 
    VALUES(3, 'Multikino', 'Warszawa', '00-001', 'Marszałkowska', '21');
INSERT INTO kino(id_kino, nazwa, miasto, kod_pocztowy, ulica, numer_budynku) 
    VALUES(4, 'Kino Helios', 'Kraków', '31-111', 'Karmelicka', '6');
INSERT INTO kino(id_kino, nazwa, miasto, kod_pocztowy, ulica, numer_budynku) 
    VALUES(5, 'Kino Rialto', 'Poznań', '60-111', 'Rynkowa', '8');
INSERT INTO kino(id_kino, nazwa, miasto, kod_pocztowy, ulica, numer_budynku) 
    VALUES(6, 'Kino Wisła', 'Kraków', '31-111', 'Limanowskiego', '14');

-- aktorzy
INSERT INTO aktor(id_aktor, imie, nazwisko, data_urodzenia) 
    VALUES(1, 'Tom', 'Hanks', '1956-07-09');
INSERT INTO aktor(id_aktor, imie, nazwisko, data_urodzenia) 
    VALUES(2, 'Brad', 'Pitt', '1963-12-18');
INSERT INTO aktor(id_aktor, imie, nazwisko, data_urodzenia) 
    VALUES(3, 'Robert', 'De Niro', '1943-08-17');
INSERT INTO aktor(id_aktor, imie, nazwisko, data_urodzenia) 
    VALUES(4, 'Leonardo', 'DiCaprio', '1974-11-11');
INSERT INTO aktor(id_aktor, imie, nazwisko, data_urodzenia) 
    VALUES(5, 'Meryl', 'Streep', '1949-06-22');
INSERT INTO aktor(id_aktor, imie, nazwisko, data_urodzenia) 
    VALUES(6, 'Denzel', 'Washington', '1954-12-28');
INSERT INTO aktor(id_aktor, imie, nazwisko, data_urodzenia) 
    VALUES(7, 'Cate', 'Blanchett', '1969-05-14');
INSERT INTO aktor(id_aktor, imie, nazwisko, data_urodzenia) 
    VALUES(8, 'Kate', 'Winslet', '1975-10-05');
INSERT INTO aktor(id_aktor, imie, nazwisko, data_urodzenia) 
    VALUES(9, 'Saoirse', 'Ronan', '1994-04-12');
INSERT INTO aktor(id_aktor, imie, nazwisko, data_urodzenia) 
    VALUES(10, 'Brie', 'Larson', '1989-10-01');
INSERT INTO aktor(id_aktor, imie, nazwisko, data_urodzenia) 
    VALUES(11, 'John', 'Travolta', '1954-02-18');

-- rezyserowie
INSERT INTO rezyser(id_rezyser, imie, nazwisko, data_urodzenia) 
    VALUES(1, 'Steven', 'Spielberg', '1946-12-18');
INSERT INTO rezyser(id_rezyser, imie, nazwisko, data_urodzenia) 
    VALUES(2, 'Quentin', 'Tarantino', '1963-03-27');
INSERT INTO rezyser(id_rezyser, imie, nazwisko, data_urodzenia) 
    VALUES(3, 'Christopher', 'Nolan', '1970-07-30');
INSERT INTO rezyser(id_rezyser, imie, nazwisko, data_urodzenia) 
    VALUES(4, 'Martin', 'Scorsese', '1942-11-17');
INSERT INTO rezyser(id_rezyser, imie, nazwisko, data_urodzenia) 
    VALUES(5, 'James', 'Cameron', '1954-08-16');
INSERT INTO rezyser(id_rezyser, imie, nazwisko, data_urodzenia) 
    VALUES(6, 'David', 'Fincher', '1962-08-28');

-- filmy
INSERT INTO film(id_film, id_rezyser, tytul, gatunek, rok) 
    VALUES(1, 1, 'Jurassic Park', 'Science Fiction', 1993);
INSERT INTO film(id_film, id_rezyser, tytul, gatunek, rok) 
    VALUES(2, 2, 'Pulp Fiction', 'Kryminał', 1994);
INSERT INTO film(id_film, id_rezyser, tytul, gatunek, rok) 
    VALUES(3, 2, 'Bękarty wojny ', 'Wojenny', 2009);
INSERT INTO film(id_film, id_rezyser, tytul, gatunek, rok) 
    VALUES(4, 2, 'Pewnego razu... w Hollywood', 'Komedia dramatyczna', 2019);
INSERT INTO film(id_film, id_rezyser, tytul, gatunek, rok) 
    VALUES(5, 3, 'Mroczny rycerz', 'Akcja', 2008);
INSERT INTO film(id_film, id_rezyser, tytul, gatunek, rok) 
    VALUES(6, 3, 'Incepcja', 'Science fiction', 2010);
INSERT INTO film(id_film, id_rezyser, tytul, gatunek, rok) 
    VALUES(7, 3, 'Dunkierka', 'Historyczny', 2017);
INSERT INTO film(id_film, id_rezyser, tytul, gatunek, rok) 
    VALUES(8, 4, 'Zdrada', 'Kryminał', 2006);
INSERT INTO film(id_film, id_rezyser, tytul, gatunek, rok) 
    VALUES(9, 4, 'Wilk z Wall Street', 'Biograficzny', 2013);
INSERT INTO film(id_film, id_rezyser, tytul, gatunek, rok) 
    VALUES(10, 4, 'Irlandczyk', 'Kryminał', 2019);

-- seanse
INSERT INTO seans(id_seans, id_kino, id_film, data, godzina) 
    VALUES(1, 1, 1, '2023-04-24', '19:20');
INSERT INTO seans(id_seans, id_kino, id_film, data, godzina) 
    VALUES(2, 1, 2, '2023-04-25', '15:00');
INSERT INTO seans(id_seans, id_kino, id_film, data, godzina) 
    VALUES(3, 2, 3, '2023-06-16', '20:45');
INSERT INTO seans(id_seans, id_kino, id_film, data, godzina) 
    VALUES(4, 3, 4, '2023-01-27', '22:00');
INSERT INTO seans(id_seans, id_kino, id_film, data, godzina) 
    VALUES(5, 4, 5, '2023-11-08', '19:15');
INSERT INTO seans(id_seans, id_kino, id_film, data, godzina) 
    VALUES(6, 5, 6, '2023-10-14', '17:30');

