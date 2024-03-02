import sqlite3
import csv

#Connect to database
conn = sqlite3.connect('LFB_data.db')
#Create a cursor
c = conn.cursor()


c.execute(""" CREATE TABLE  property_type (
        property_id text PRIMARY KEY,
        property_name text  
        )""")

c.execute(""" CREATE TABLE  incident (
        incident_id text PRIMARY KEY,
        date_of_call text,   
        postcode_full text,
        postcode_district text,
        property_id text,
        CONSTRAINT fk_property_id 
            FOREIGN KEY (property_id)
            REFERENCES property_type (property_id)
        )""")

with open('property.csv', 'r') as file:
    csv_reader = csv.reader(file)
    c.executemany('INSERT INTO property_type VALUES (?, ?)', csv_reader)

with open('LFB incident data from 2018.csv', 'r') as file:
    csv_reader = csv.reader(file)
    c.executemany('INSERT INTO incident VALUES (?, ?, ?,?,?)', csv_reader)



conn.commit()

conn.close()