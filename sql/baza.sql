SET search_path to projekt;

CREATE TABLE "aktor"(
    "id_aktor" BIGINT NOT NULL,
    "imie" VARCHAR(255) NOT NULL,
    "nazwisko" VARCHAR(255) NOT NULL,
    "data_urodzenia" DATE NOT NULL
);
ALTER TABLE
    "aktor" ADD PRIMARY KEY("id_aktor");
CREATE TABLE "film"(
    "id_film" BIGINT NOT NULL,
    "tytul" VARCHAR(255) NOT NULL,
    "gatunek" VARCHAR(255) NOT NULL,
    "rok" INTEGER NOT NULL
);
ALTER TABLE
    "film" ADD PRIMARY KEY("id_film");
CREATE TABLE "rezyser"(
    "id_rezyser" BIGINT NOT NULL,
    "imie" VARCHAR(255) NOT NULL,
    "nazwisko" VARCHAR(255) NOT NULL,
    "data_urodzenia" DATE NOT NULL
);
ALTER TABLE
    "rezyser" ADD PRIMARY KEY("id_rezyser");
CREATE TABLE "kino"(
    "id_kino" BIGINT NOT NULL,
    "nazwa" VARCHAR(255) NOT NULL,
    "miasto" VARCHAR(255) NOT NULL,
    "kod_pocztowy" VARCHAR(255) NOT NULL,
    "ulica" VARCHAR(255) NOT NULL,
    "numer_budynku" INTEGER NOT NULL
);
ALTER TABLE
    "kino" ADD PRIMARY KEY("id_kino");
CREATE TABLE "seans"(
    "id_seans" BIGINT NOT NULL,
    "id_kino" BIGINT NOT NULL,
    "id_film" BIGINT NOT NULL,
    "data" DATE NOT NULL,
    "godzina" TIME(0) WITHOUT TIME ZONE NOT NULL
);
ALTER TABLE
    "seans" ADD PRIMARY KEY("id_seans");
CREATE TABLE "aktor_film"(
    "id" BIGINT NOT NULL,
    "id_aktor" BIGINT NOT NULL,
    "id_film" BIGINT NOT NULL
);
ALTER TABLE
    "aktor_film" ADD PRIMARY KEY("id");
ALTER TABLE
    "aktor_film" ADD CONSTRAINT "aktor_film_id_aktor_foreign" FOREIGN KEY("id_aktor") REFERENCES "aktor"("id_aktor");
ALTER TABLE
    "aktor_film" ADD CONSTRAINT "aktor_film_id_film_foreign" FOREIGN KEY("id_film") REFERENCES "film"("id_film");
ALTER TABLE
    "seans" ADD CONSTRAINT "seans_id_film_foreign" FOREIGN KEY("id_film") REFERENCES "film"("id_film");
ALTER TABLE
    "seans" ADD CONSTRAINT "seans_id_kino_foreign" FOREIGN KEY("id_kino") REFERENCES "kino"("id_kino");