
CREATE TABLE athletes (
  id integer,
  name text,
  sex text,
  age integer,
  height integer,
  weight integer,
  team text
);

CREATE TABLE events (
  games integer,
  event text,
  sport text,
  gold_medalist integer,
  silver_medalist integer,
  bronze_medalist integer
);

CREATE TABLE noc_region (
  noc text,
  region text,
  golds integer,
  silvers integer,
  bronzes integer
);

CREATE TABLE games (
  games_id integer,
  year integer,
  season text,
  city text
);
