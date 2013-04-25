#!/usr/bin/env python3

#projected features
#add adjustment for route based on frequency
#add adjustments for route based on vaction packs ----- complete
#add adjustments for route based on side of road paper tubes are
#link program to GPS tomtom

version = 0.2

import json
from urllib.request import urlopen
import re


"""class Print():
	'''change output as needed'''
	def __init__(self, stringer=None):
		if stringer == None:
			print()
		else:
			print(stringer)"""
			
class Print():
	def __init__(self, stringer=None):
		filer = open('directions.txt','a')
		if stringer == None:
			filer.write('\n')
			print()
		else:
			filer.write(stringer + '\n')
			print(stringer)
	def closeit(self):
		self.filer.close()

class Direction:
	def ui(self, s, e):
		'''set up initial values based on s:start and e:end'''
		self.start = '+'.join(s.split())
		self.end = '+'.join(e.split())
		self.url = 'http://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}&sensor=false'.format(self.start, self.end)
		self.obj = urlopen(self.url).read().decode()
		self.data = json.loads(self.obj)
		
		self.tripper()
		self.steps = self.data['routes'][0]['legs'][0]['steps']

		
	def tripper(self):
		'''get total trip values'''
		t = self.data['routes'][0]['legs'][0]
		self.trip_dist = t['distance']['text']
		self.trip_time = t['duration']['text']
		self.trip_end = t['end_address']
		self.trip_start = t['start_address']
		
	def stepper(self, msg, freq, status):
		'''step through json keys'''
		for num, step in enumerate(self.steps):
			#print(step)
			directions = step['html_instructions'] #get each string of directions
			directions = re.sub("<.*?>", " ", directions) #remove all html tags from strings
			instruction = ' '.join(directions.split()) #remove unwanted spaces
			
			distance = step['distance']['text']
			duration = step['duration']['text']
			
			if msg != 'Home':
				Print(instruction)
				
			if msg == 'Home':
				continue
			elif num == len(self.steps) - 1:
				Print('Deliver {}: {}'.format(freq, self.trip_end))
				Print('MSG: {}'.format(msg))
				Print('DISTANCE: {}'.format(distance))
				Print('DURATION: {}'.format(duration))
				Print('\n{}\n'.format('*' * 40))
				continue



			#distance = step['distance']['text']
			Print('DISTANCE: {}'.format(distance))
			
			#duration = step['duration']['text']
			Print('DURATION: {}'.format(duration))
			
			poly = step['polyline']['points']
			#print(poly)
			
			start_coords = step['start_location']
			#print(start_coords['lat'])
			#print(start_coords['lng'])

			end_coords = step['end_location']
			#print(end_coords['lat'])
			#print(end_coords['lng'])
			
			Print()
			

def get_route():
	'''get route from file'''
	filer = open('address.txt')
	lines = filer.readlines()
	route = []

	for line in lines:
		if not line.startswith('#'):
			if line != '\n':
				line = line.rstrip()
				cust = line.split('|')
				route.append(cust)
				
	return route
	
trip = Direction()
route = get_route()
prev = route[0][0] #start home


	

for num, cust in enumerate(get_route(), 1):
	try:

		if route[num][3].strip() != 'active': #skip non active customers
			Print('SKIP address {} due to {}\n'.format(route[num][0], route[num][3]))
			
			continue
		trip.ui(prev, route[num][0])
	except IndexError: #catch last item of list due to 1 passed to enumerate()
		continue
	trip.stepper(route[num][1], route[num][2], route[num][3])

	prev = route[num][0]
	
	
	
#p = Print()
#p.closeit()


