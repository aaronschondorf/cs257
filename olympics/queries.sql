SELECT noc
FROM noc_region
ORDER BY noc

SELECT name
FROM noc_region, athletes
WHERE noc = team
AND noc = 'Kenya'

SELECT event, year
FROM events, athletes
WHERE name = 'Greg Louganis'
AND id = gold
OR id = silver
OR id = bronze
ORDER BY year

SELECT noc, medals
FROM noc_region
ORDER BY medals
