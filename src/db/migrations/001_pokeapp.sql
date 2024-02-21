CREATE TABLE pokemon (
"id" int NOT NULL PRIMARY KEY,
"image" varchar(255) NOT NULL,
"description" text NOT NULL
);

CREATE TABLE pokeapp (
"id" serial NOT NULL PRIMARY KEY,
"date" date NOT NULL,
"hits" int NOT NULL,
"pokemon_id" int NOT NULL,
CONSTRAINT fk_dates
      FOREIGN KEY(pokemon_id) 
      REFERENCES pokemon(id)
);

CREATE TABLE pokename (
"id" serial NOT NULL PRIMARY KEY,
"name" varchar(100) NOT NULL,
"lang" varchar(25) NOT NULL,
"pokemon_id" int NOT NULL,
CONSTRAINT fk_othername
      FOREIGN KEY(pokemon_id) 
      REFERENCES pokemon(id)
);