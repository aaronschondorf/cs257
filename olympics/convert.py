'''
Created by Aaron Schondorf
'''

import csv

class Athlete:
    def __init__(self, id, name, sex, age, height, weight, team):
        self.id = int(id)
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.team = team

    def __eq__(self, other):
        return self.id == other.id

    def to_nums(self):
        if self.age != 'NA':
            self.age = int(self.age)
        if self.height != 'NA':
            self.height = float(self.height)
        if self.weight != 'NA':
            self.weight = float(self.weight)

class Event:
    def __init__(self, year, season, sport, event):
        self.year = int(year)
        self.season = season
        self.sport = sport
        self.event = event
        self.gold = 'NA'
        self.silver = 'NA'
        self.bronze = 'NA'

    def __eq__(self, other):
        return self.event == other.event and self.year == other.year

    def set_medal(self, athlete, medal):
        if medal.lower() == 'gold':
            self.gold = athlete.id
        elif medal.lower() == 'silver':
            self.silver = athlete.id
        elif medal.lower() == 'bronze':
            self.bronze = athlete.id
        else:
            print('unknown medal type: '+ medal + ' ' + athlete.id)


class NOC:
    def __init__(self, noc_region, country):
        self.noc_region = noc_region
        self.country = country
        self.medals = 0

    def __eq__(self, other):
        return self.noc_region == other.noc_region

    def add_medal(self):
        self.medals +=1

with open('noc_regions.csv', newline ='') as csvfile:
    noc_reader = csv.reader(csvfile, delimiter = ',')
    noc_list = []

    #Skipping Header
    next(noc_reader)

    for row in noc_reader:
        current_noc = NOC(row[0], row[1])

        if current_noc not in noc_list:
            noc_list.append(current_noc)


with open('athlete_events.csv', newline ='') as csvfile:
    athlete_reader = csv.reader(csvfile, delimiter = ',')
    athletes_list = []
    events_list = []

    #Skipping Header
    next(athlete_reader)

    for row in athlete_reader:
        if len(athletes_list) == 0 or row[0] != current_athlete.id:
            current_athlete = Athlete(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            current_event = Event(row[9], row[10], row[12], row[13])

            current_athlete.to_nums()
            athletes_list.append(current_athlete)

            if current_event not in events_list:
                events_list.append(current_event)

            if row[14] != 'NA':
                for event in events_list:
                    if event == current_event:
                        event.set_medal(current_athlete, row[14])
                for noc in noc_list:
                    if current_athlete.team == noc.noc_region:
                        noc.add_medal()

with open('athletes.csv', 'w', newline='') as csvfile:
    athlete_writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'sex', 'age', 'height', 'weight', 'team'])
    for athlete in athletes_list:
        athlete_writer.writerow({'id': athlete.id, 'name': athlete.name, 'sex': athlete.sex, 'age': athlete.age, 'height': athlete.height, 'weight': athlete.weight, 'team': athlete.team})

with open('events.csv', 'w', newline='') as csvfile:
    event_writer = csv.DictWriter(csvfile, fieldnames=['year', 'season', 'sport', 'event', 'gold', 'silver', 'bronze'])
    for event in events_list:
        event_writer.writerow({'year': event.year, 'season': event.season, 'sport': event.sport, 'event': event.event, 'gold': event.gold, 'silver': event.silver, 'bronze': event.bronze})

with open('noc.csv', 'w', newline ='') as csvfile:
    noc_writer = csv.writer(csvfile, delimiter = ' ')
    for noc in noc_list:
        noc_writer.writerow(noc.noc_region +','+ noc.country)
