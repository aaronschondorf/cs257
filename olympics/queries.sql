SELECT noc_region.noc
FROM noc_region
ORDER BY noc_region.noc

SELECT athletes.name
FROM noc_region, athletes
WHERE noc_region.noc = athletes.team
AND noc_region.noc = 'Kenya'

SELECT events.event, events.year
FROM events, athletes
WHERE athletes.name = 'Greg Louganis'
AND athletes.id = events.gold
OR athletes.id = events.silver
OR athletes.id = events.bronze
ORDER BY events.year

SELECT noc_region.noc, noc_region.medals
FROM noc_region
ORDER BY noc_region.medals
