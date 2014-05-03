import subprocess
import commands
import re
import datetime
import urllib
import smtplib
import httplib2
from twilio.rest import TwilioRestClient

#incomplete


## Sending SMS through GSM Module to the specified contacts in cont- ##
## act.cfg. SMS can also be sent through SMTP, SMMP, POP3 etc, but   ##
## we have not configured it according to these.                     ##

###### We made this functionality using OZEKI NG SMS GATEWAY and ######
###### MONO Framework. Although we have not configured it for -  ######
###### networks with proxy servers.                              ######
def messageSMS(alert):
	now=datetime.datetime.now();
        logtime=str(now);
        log='\n'+logtime+'\t'+alert;
	contactlist=readingContacts();
	for word in contactlist:
		host = 'http://127.0.0.1';
		user_name = 'admin';
		user_password = 'abc123';
		recipient = word;
		message_body = log;

		http_req = host
		http_req += ':9501/api?action=sendmessage&username='
		http_req += urllib.quote(user_name)
		http_req += '&password='
		http_req2 += urllib.quote(user_password)
		http_req += '&recipient='
		http_req += urllib.quote(recipient);
		http_req += '&messagetype=SMS:TEXT&messagedata=';
		http_req += urllib.quote(message_body);

		get = urllib.urlopen(http_req);
		req = get.read();
		get.close();
		print('Sending Message to' + word + '!');
	
		if req.find('Message accepted for delivery') > 1:
    			print('Message successfully sent to' + word + '!');
		else:
    			print('Message not sent! Please check your settings!');



## Sending SMS Alert Through Internet (HTTP/HTTPS) to the specified- ##
## contacts in contacts.cfg using twilio API.                        ## 
def twilio(alert):
	now=datetime.datetime.now();
        logtime=str(now);
        log='\n'+logtime+'\t'+alert;
	account = 'AC7de35ed5c7338faaa0186b34b8329d83'
	token = '0bbc5c485687118ae25c78d626f6fc11'
	client = TwilioRestClient(account, token)
	contactlist=readingContacts();
	for word in contactlist:
		print('Message Sending to ' + word + '!');
		message = client.messages.create(to=word, from_="+19735776493",
                                 body=log);
	print(call.sid);



