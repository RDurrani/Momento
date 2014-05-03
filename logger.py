import datetime

def logging(log):
	now=datetime.datetime.now()
	logtime=str(now)
	log='\n'+logtime+'\t'+log
	print(log)
	with open("./log/momento.log", "a") as myfile:
    		myfile.write(log)

