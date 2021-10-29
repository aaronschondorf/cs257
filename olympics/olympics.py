'''
    olympics.py
    Aaron Schondorf, 21 October 2021

    For use in the "olympics" assignment at the beginning of Carleton's
    CS 257 Software Design class, Fall 2021.
'''

import argparse
import psycopg2

parser = argparse.ArgumentParser()

#mutually exclusive group handles usage of different functions
group = parser.add_mutually_exclusive_group()
group.add_argument('--athletes', action='store_true', help = 'Prints names of all athletes from a given NOC. Enter in form --athletes NOC')
group.add_argument('--medals', action='store_true', help = 'Gives list of NOCs and how many gold medals they have won in descending order. Enter in form --medals')
group.add_argument('--event', action='store_true', help = 'Gives list of who won gold medals in all events of a given sport ordered by year. Enter in form --event EVENT')
parser.add_argument('search', nargs='*')

args = parser.parse_args()

search_string =''
for element in args.search:
    search_string=search_string+' '+element
search_string =search_string.strip()
print(search_string)

try:
    connection = psycopg2.connect(database='olympics', user='aschondorf')
except Exception as e:
    print(e)
    exit()

if args.athletes:
    try:
        cursor = connection.cursor()
        query = 'SELECT name FROM athletes WHERE team = %s'
        cursor.execute(query, (search_string,))
        for row in cursor:
            print(row[0])
    except Exception as e:
        print(e)
        exit()

elif args.medals:
    try:
        cursor = connection.cursor()
        query = 'SELECT noc,golds FROM noc_region ORDER BY golds DESC'
        cursor.execute(query)
        for row in cursor:
            print(row[0] + ': ' + str(row[1]))
    except Exception as e:
        print(e)
        exit()

elif args.event:
    try:
        cursor = connection.cursor()
        query = 'SELECT name, team, year, event FROM athletes, events, games WHERE gold_medalist = id AND sport = %s ORDER BY year'
        cursor.execute(query,(search_string,))
        for row in cursor:
            print(str(row[2]) + ', ' + row[3] + ': ' + row[0] + ', ' + row[1])
    except Exception as e:
        print(e)
        exit()

else:
    print("Invalid command. Type '--help' or '-h', for description of commands supported by this CLI.")
