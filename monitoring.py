import os
import sys

import subprocess
import commands
import re
import datetime
import time

#adding scripts from project
scriptpath1 = "cgroups.py"
sys.path.append(os.path.abspath(scriptpath1));
scriptpath2 = "processes.py"
sys.path.append(os.path.abspath(scriptpath2))
scriptpath3 = "rules.py"
sys.path.append(os.path.abspath(scriptpath3))
scriptpath4 = "logger.py"
sys.path.append(os.path.abspath(scriptpath4))
scriptpath5 = "gsmmodule.py"
sys.path.append(os.path.abspath(scriptpath5))
#importing project
from cgroups import *
from processes import *
from rules import *
from logger import *
from gsmmodule import *
#import completed

#return latancy from layer 4 ping
def ping(ptype,port,ip):
	nping = 'nping'+' --'+ptype+' -p '+port+' '+ip+' | grep Avg';
	a = commands.getoutput(nping);
	if a.endswith('N/A'):
            	return a;
        else:
                b=re.search('Avg rtt: (.+?)m',a)
                if b:
                        c=b.group(1);
			return c;

#perform action on process                                                          ##
def actiononprocess(process, action):
	if action == 'restart':
		subprocess.call(process.stopadd, shell=True);
		subprocess.call(process.startadd, shell=True);
        	logmsg='The process,'+process.name+', is restarted successfully!';
		time.sleep(1)
        	logging(logmsg);
		#twilio(logmsg);
                #messageSMS(logmsg);
	elif action == 'start':
		subprocess.call(process.stopadd, shell=True);
                logmsg='The process,'+process.name+', is stopped successfully!';
		time.sleep(1)
                logging(logmsg);
		#twilio(logmsg);
                #messageSMS(logmsg);
		
	elif action == 'stop':
		subprocess.call(process.stopadd, shell=True);
                logmsg='The process,'+process.name+', is started successfully!';
                logging(logmsg);
		#twilio(logmsg);
                #messageSMS(logmsg);	

#process probe and starter
def startifpid(process):
	processid = (int)process.pid()
	if any(char.isdigit() for char in processid)==False:
        	subprocess.call(process.startadd, shell=True);
		logmsg='The process, '+process.name+', is started successfully';
		time.sleep(1)
		logging(logmsg);
		#twilio(logmsg);
                #messageSMS(logmsg);
	#else:
        #print('Services Up and Running')

		
## This function restarts the specified service after a certain time ##
## which is always specified in minutes.                             ##
def timer(min, pname):
	global mincounter;
	if mincounter is None:
		now = datetime.datetime.now();
		mins = now.minute+min;
		if mins>60:
			mins=mins-60;
		mincounter=mins;
	else:
		if datetime.datetime.now().time().minute!=mincounter:
			return;
		else:
			subprocess.call(restartadd, shell=True);
			mincounter=None;
			logmsg='The '+ pname+' has been restarted successfully!';
			logging(logmsg);
			#twilio(logmsg);
			#messageSMS(logmsg);


## Reads momento.cfg and processes.cfg and starts, stops or restarts the- ##
## specified service on the basis of values in both of the configuration  ##
## files specified above						  ##
def processchecking():
	temparrm=[];
	temparrm=readrules();
	arrm=temparrm[0:-1]
	temparrp=[];
	temparrp=readprocess();
	arrp=temparrp[0:-1]
	for word in arrm:
		if word.type=='ping':	
			str1 = ping(word.ptype, word.port, word.ip);
			if str1 = 'timeout':
				str1 = 9999			
			if int(str1)>word.latancy or str1.endswith('N/A'):
				if word.fail == 'restart' or word.fail == 'stop':
					for pn in word.process:
						for a in arrp:
                                                	if a.name==pn:
								if word.fail == 'restart':                                               
									actiononprocess(process, 'restart')
								else:
									actiononprocess(process, 'stop')
                                                	break;
				elif word.fail='alert':
					#insert gsm module code here
					print('---Loading---\n--Loading--\n');
		
		elif word.type=='timer':
			#timer(word.frequency, word.process);
			#work in progress

		else:
			print 'error'

#Active Process monitor
def actiononpid():
	temparrp=[];
        temparrp=readprocess();
	arrp=temparrp[0:-1]
	for eachprocess in arrp:
		if eachprocess.status == 'monitor'
			startifpid(eachprocess); 								
