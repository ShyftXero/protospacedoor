#!/usr/bin/env python3
# authorized =['0212394425','0213660857', '0857870596','0213548985','0217342905','0067305985', '2459177220']


PROD = False

#import sqlite3 as sql
import dataset
import time
import arrow

if PROD:
	import RPi.GPIO as GPIO
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7,GPIO.OUT)

	GPIO.output(7, GPIO.HIGH)

def log(data):
	db = dataset.connect('sqlite:///futurespace.db')	
	entries = db['log']
	utc = arrow.utcnow()
	local = utc.to('US/Central')
	
	temp = {'time':local.format(), 'data':repr(data)}
	
	entries.insert(temp)


def authorized(keyfob_id):
	db = dataset.connect('sqlite:///futurespace.db')
	users = db['users']
	result = users.find_one(keyfob=keyfob_id)

	if result != None and result['enabled'].upper() == "TRUE":
		return result
	return False

def who(keyfob_id):
	db = dataset.connect('sqlite:///futurespace.db')
	users = db['users']
	result = users.find_one(keyfob=keyfob_id)
	if result != None:
		return result
	return 'Unknown'

log("starting up")
while True:
	try:
		keyfob_id = input('id: ')
	except KeyboardInterrupt:
		print("quitting...")
		log("shutting down")
		exit()

	if authorized(keyfob_id):
		user = who(keyfob_id)
		print("allowed")
		print('user:', user['name'], 'keyfob:', user['keyfob'])
		if PROD:
			GPIO.output(7, GPIO.LOW)
			time.sleep(5)
			GPIO.output(7, GPIO.HIGH)
		log(user)

	else:
		if who(keyfob_id) !=  "Unknown":
			print("**********Entry Disabled***********")
			print(who(keyfob_id), 'keyfob id:', keyfob_id)
		else:
			print("**********Not Authorized***********")
			print('Unknown keyfob id:', keyfob_id)
	# if keyfob_id == "quit":
	# 	log("shutting down")
	# 	exit()
#use gui to admin 
#sandman2ctl sqlite+pysqlite:///futurespace.db
#access it via localhost:5000/admin

# db = dataset.connect('sqlite:///futurespace.db')

# db.query('DROP TABLE "users";')

# db.query("""CREATE TABLE "users" (
#     "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     "name" TEXT NOT NULL,
#     "keyfob" TEXT NOT NULL,
#     "enabled" TEXT NOT NULL
# )""")

#create users
# u = db['users']

# t1 = {'name':'eli', 'keyfob':'12345', 'enabled':'TRUE'}
# t2 = {'name':'john', 'keyfob':'23456', 'enabled':'FALSE'}

# u.insert(t1)
# u.insert(t2)

#create an entry into the building
# entries = db['log']
# utc = arrow=utcnow()
# local = utc.to('US/Central')

# temp = {'time':local.humanize(), 'user':user}

# entries.insert(temp)

#listing users 
# all_users = db['users'].all()
# all_entries = db['log'].all()
