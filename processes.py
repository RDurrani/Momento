#! /usr/bin/python

import ConfigParser
import subprocess

class process(object):
	def __init__(self):
		self.name = ''
		self.pidf = ''
		self.startadd = ''
		self.stopadd = ''
		self.status = ''
	def pid(self):
		getpid = 'cat ' + self.pidf
		pidp = subprocess.Popen(getpid, stdout=subprocess.PIPE, shell=True)
		(pid, err) = pidp.communicate()
		return pid	

def readprocess():
	config = ConfigParser.ConfigParser()
	config.read('configs/processes.cfg')
	pc = 0
	pro = [process()]
	for processes in config.sections():
			
		pro[pc].name = processes	
		pro[pc].pidf = config.get(processes, 'pid')
		#print(pro[pc].name +": "+ pro[pc].pid())
		pro[pc].startadd = config.get(processes, 'start')
		pro[pc].stopadd = config.get(processes, 'stop')
		pro[pc].status = config.get(processes, 'status')
		#print(pro[pc].startadd)
		#print(pro[pc].stopadd)
		#print(pro[pc].status)
		#print('')
		pro.append(process())
		pc += 1
		pro[pc].name='END'
	
	return pro
	print 'end'

