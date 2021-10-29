'''
    olympics-api.py
    Aaron Schondorf
    28 October 2021
    Flask API implementation
'''
import sys
import argparse
import psycopg2
import flask
import json

app = flask.Flask(__name__)

try:
    connection = psycopg2.connect(database='olympics', user='aschondorf')
except Exception as e:
    print(e)
    exit()

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/games')
def get_games():
    try:
        cursor = connection.cursor()
        query = 'SELECT games_id, year, season, city FROM games'
        cursor.execute(query)
        games_list =[]
        for row in cursor:
            games_dict = {'id': row[0], 'year': row[1], 'season': row[2], 'city': row[3]}
            games_list.append(games_dict)
    except Exception as e:
        print(e)
        exit()
    return json.dumps(games_list)

@app.route('/nocs')
def get_nocs():
    try:
        cursor = connection.cursor()
        query = 'SELECT noc, region FROM noc_region'
        cursor.execute(query)
        noc_list = []
        for row in cursor:
            noc_dict = {'noc': row[0], 'region': row[1]}
            noc_list.append(noc_dict)
    except Exception as e:
        print(e)
        exit()
    return json.dumps(noc_list)

@app.route('/medalists/games/<games_id>')
def get_medalists(games_id):
    noc = flask.request.args.get('noc_abbreviation')
    try:
        cursor = connection.cursor()
        query = 'SELECT id, name, sex, sport, event, gold_medalist, silver_medalist, bronze_medalist, team FROM athletes, events WHERE games = %s'
        cursor.execute(query, [games_id])
        athlete_list = []
        for row in cursor:
            if noc is None or noc == row[8]:
                athlete_dict = {'id': row[0], 'name': row[1], 'sex': row[2], 'sport': row[3], 'event': row[4]}
                if row[0] == row[5]:
                    athlete_dict['medal'] = 'gold'
                elif row[0] == row[6]:
                    athlete_dict['medal'] = 'silver'
                elif row[0] == row[7]:
                    athlete_dict['medal'] = 'bronze'
                else:
                    continue
                athlete_list.append(athlete_dict)
    except Exception as e:
        print(e)
        exit()
    return json.dumps(athlete_list)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application demonstrating templates.')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
