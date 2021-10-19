
postgres=# CREATE TABLE athletes (
postgres(# id integer,
postgres(# name text,
postgres(# sex text,
postgres(# age integer,
postgres(# height float,
postgres(# weight float,
postgres(# team text
postgres(# );

postgres=# CREATE TABLE events (
postgres(# year integer,
postgres(# season text,
postgres(# sport text,
postgres(# event text,
postgres(# gold_medalist integer,
postgres(# silver_medalist integer,
postgres(# bronze_medalist integer
postgres(# );

postgres=# CREATE TABLE noc_region (
postgres(# noc text,
postgres(# region text
postgres(# );
