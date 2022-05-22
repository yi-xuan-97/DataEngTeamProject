# this program loads Census ACS data using basic, slow INSERTs
# run it with -h to see the command line options

import time
import psycopg2
import argparse
import re
import csv

DBname = "postgres"
DBuser = "postgres"
DBpwd = "123456"
TableName = 'RealSenseData'
Datafile = "filedoesnotexist"  # name of the data file to be loaded
CreateDB = False  # indicates whether the DB table should be (re)-created


def row2vals(row):
	for key in row:
		if not row[key]:
			row[key] = 0  # ENHANCE: handle the null vals

	ret = f"""
	   {row['vehicle_number']},            -- VEHICLE_NUMBER
	   {row['leave_time']},                -- LEAVE_TIME
	   {row['train']},                     -- TRAIN
	   {row['route_number']},              -- ROUTE_NUMBER
	   {row['direction']},                 -- DIRECTION
	   {row['stop_time']},                 -- STOP_TIME
	   {row['arrive_time']},               -- ARRIVE_TIME
	   {row['location_id']},               -- LOCATION_ID
	   {row['estimated_load']},            -- LOAD
	   {row['train_mileage']},             -- MILEAGE
	   {row['pattern_distance']},          -- PATTERN_DISTANCE
	   {row['location_distance']},         -- LOCATION_DISTANCE
	   {row['x_coordinate']},              -- X
	   {row['y_coordinate']},              -- Y
	   {row['data_source']},               -- SOURCE
	   {row['schedule_status']},           -- STATUS
	   {row['leave']},                     -- LEAVE
	   {row['stop']},                      -- STOP
	   {row['arrive']},                    -- ARRIVE
	"""
	return ret


def initialize():
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--datafile", required=True)
  parser.add_argument("-c", "--createtable", action="store_true")
  args = parser.parse_args()

  global Datafile
  Datafile = args.datafile
  global CreateDB
  CreateDB = args.createtable

# read the input data file into a list of row strings


def readdata(fname):
	print(f"readdata: reading from File: {fname}")
	with open(fname, mode="r") as fil:
		dr = csv.DictReader(fil)

		rowlist = []
		for row in dr:
			rowlist.append(row)

	return rowlist

# convert list of data rows into list of SQL 'INSERT INTO ...' commands


def getSQLcmnds(rowlist):
	cmdlist = []
	for row in rowlist:
		valstr = row2vals(row)
		cmd = f"INSERT INTO {TableName} VALUES ({valstr});"
		cmdlist.append(cmd)
	return cmdlist

# connect to the database


def dbconnect():
	connection = psycopg2.connect(
		host="localhost",
		database=DBname,
		user=DBuser,
		password=DBpwd,
	)
	connection.autocommit = False
	return connection

# create the target table
# assumes that conn is a valid, open connection to a Postgres database


def createTable(conn):

	with conn.cursor() as cursor:
		cursor.execute(f"""
			DROP TABLE IF EXISTS {TableName};
			CREATE TABLE {TableName} ( 
				VEHICLE_NUMBER      INTEGER,
				LEAVE_TIME          INTEGER,
				TRAIN               INTEGER,
				ROUTE_NUMBER        INTEGER,
				DIRECTION           NUMERIC,
				STOP_TIME           NUMERIC,
				ARRIVE_TIME         INTEGER,
				LOCATION_ID         NUMERIC,
				LOAD                INTEGER,
				MILEAGE             NUMERIC,
				PATTERN_DISTANCE    NUMERIC,
				LOCATION_DISTANCE   NUMERIC,
				X                   NUMERIC,
				Y                   NUMERIC,
				SOURCE              INTEGER,
				STATUS              INTEGER,
				LEAVE               TEXT,
				STOP                TEXT,
				ARRIVE              TEXT
			);
			ALTER TABLE {TableName} ADD PRIMARY KEY(CensusTract);
			CREATE INDEX idx_{TableName}_State ON {TableName}(State);
		""")

		print(f"Created {TableName}")

def load(conn, icmdlist):

	with conn.cursor() as cursor:
		print(f"Loading {len(icmdlist)} rows")
		start = time.perf_counter()
	
		for cmd in icmdlist:
			cursor.execute(cmd)

		elapsed = time.perf_counter() - start
		print(f'Finished Loading. Elapsed Time: {elapsed:0.4} seconds')


def main():
	initialize()
	conn = dbconnect()
	rlis = readdata(Datafile)
	cmdlist = getSQLcmnds(rlis)

	if CreateDB:
		createTable(conn)

	load(conn, cmdlist)


if __name__ == "__main__":
	main()
