#! /usr/bin/python

import ConfigParser
import subprocess
import re

def processparser(tempprocess):
	i=0
	im=0
	process=['']
	while(i<len(tempprocess)):
		if (tempprocess[i]!=',' and tempprocess[i]!=' '):
			process[im]+=tempprocess[i]
		if tempprocess[i]==',':
			process.append('')
			im +=1
		i +=  1;
	return process
	
class actions(object):
	def __init__(self):
        	self.type = ''
        	self.latancy = ''
		self.ip = ''
		self.port = ''
		self.ptype = ''
		self.fail = ''
		self.process = ['']
		self.time = ''
		self.attempts = ''
		self.contact = ''
		self.message = ''

def readrules():
	config = ConfigParser.ConfigParser()
	config.read('configs/momento.cfg')
	action = [actions()]
	ac = 0
	for rule in config.sections():
		#PID
		type = config.get(rule, 'type')
		#print type
		if type == 'ping':

			action[ac].latancy = config.get(rule, 'latancy')
			#print action[ac].latancy
			action[ac].ip = config.get(rule, 'ip')
			#print action[ac].ip
			action[ac].port = config.get(rule, 'port')
			#print action[ac].port
			action[ac].ptype = config.get(rule, 'ptype')
			#print action[ac].ptype
			action[ac].fail = config.get(rule, 'fail')
			#print action[ac].fail
			if action[ac].fail == 'restart':
				action[ac].process = processparser(config.get(rule, 'process'))
				#print action[ac].process
				action[ac].time = config.get(rule, 'startuptime')
				#print action[ac].time
				action[ac].attempts = config.get(rule, 'attempts')
				#print action[ac].attempts
			else:
				if action[ac].fail == 'alert':
					action[ac].contact = config.get(rule, 'contact')
					#print action[ac].contact
					action[ac].message = config.get(rule, 'message')
					#print action[ac].message
				else:
					if action[ac].fail == 'stop':
						action[ac].process = processparser(config.get(rule, 'process'))
						#print action[ac].process
			
		else:
			if type == 'timer':
				action[ac].frequency = config.get(rule, 'frequency')
				#print action[ac].frequency
			action[ac].process = processparser(config.get(rule, 'process'))
				#print action[ac].process
		action.append(actions())
		ac += 1
		action[ac].type = 'END'

	return action
