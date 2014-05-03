#! /usr/bin/python

#Momento Prototype programmed in 4 days
#Dated: 29/04/14
#
#Momento by MetaCortex
#Team MetaCortex: RDurrani, Nasha Jr., M4v3Rick (Timmy) & Shuja
#Programming by RDurrani & Nasha Jr.
#Testing and documentation by M4v3RicK (Timmy) & Shuja
#Special thanks to Sabey (Sohaib Azad)
#
#Incomplete features:
# 1	Timer functionality (timer(min, pname))
# 2	startuptime wait
# 3	gsm module (gsmmodule.py)
#
#Dependencies: cat, nping, ConfigParser.py, twillo (for disfuct gsm module)
#Built and tested on Debian Wheezy, gedit, nano, Python 2.7.3
#
#contact by email: vento36 "at" gmail "dot" com

import os
import sys

#adding scripts from project
scriptpath1 = "monitoring.py"
sys.path.append(os.path.abspath(scriptpath1));
#importing project
from monitoring import *
#import completed

#deamonizing
Momentopid = os.fork()
if Momentopid!=0:
	sys.exit(0)

#starting Momento
print 'Starting Momento'
while 1:
	actiononpid()
	processmonitor()
	time.sleep(120)
