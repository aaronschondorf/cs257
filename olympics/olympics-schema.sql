
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
  year integer,
  season text,
  sport text,
  event text,
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
