#! /usr/bin/python

import ConfigParser
import subprocess

class contactgroups(object):
	def __init__(self):
		self.groupname = ''
		self.contact = ['']
def readcontacts():
	config = ConfigParser.ConfigParser()
	config.read('configs/contact.cfg')
	lists = [contactgroups()]
	lc=0
	#read
	for group in config.sections():
		clist = []
		lists[lc].groupname=group	
		for contact in config.options(group):
			number = config.get(group , contact)
			if lists[lc].contact[0]=='':
				lists[lc].contact[0]=number
			else:
				lists[lc].contact.append(number)
		lists.append(contactgroups())
		lc += 1
		lists[lc].groupname='END'
	return lists
#write
lat = readcontacts()
lst = lat[0:-1]

#for g in lst:
#	#print g.groupname
#	for a in g.contact:	
#		print a
#print 'end'


