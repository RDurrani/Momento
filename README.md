Momento
=======

 A python based open source system for monitoring and automatically managing processes on Linux machines

To Start edit configurations files:
1. Momento.cfg
2. processes.cfg
3. contacts.cfg
Execute Momento.py

Momento, dubbed by us as a Process Management System Utility (PMSU), it actively monitor the local host or, in limited capacity, a remote host, and automatically attempt to correct defined "problems" or act when specified conditions became true.

Conditions or problems it can detect or monitor for included:
-Timer based events
-The termination, unresponsiveness of one or more processes
-The results of a layer 4 ping on a local or remote host

Actions that Momento can perform in attempt to rectify a problem
-Stopping one or more processes
-Starting one or more processes
-Restarting one or more processes
-Alerting administrator(s)/user(s) via SMS Message sent from attached GSM module device

All rules, conditions, actions, contacts numbers and groups for Momento are defined in its configuration files

Dated: 29/04/14

Momento Alpha 0.1 Prototype by MetaCortex
Team MetaCortex: RDurrani, Muhammad-Umer (Nasha Jr.), M4v3Rick (Timmy) & Shuja
Programming by RDurrani & Muhammad-Umer (Nasha Jr.)
Testing and documentation by M4v3RicK (Timmy) & Shuja
Special thanks to Sabey (Sohaib Azad)

Incomplete features:
 1	Timer functionality (timer(min, pname))
 2	startuptime wait
 3	gsm module (gsmmodule.py)

Dependencies: cat, nping, ConfigParser.py, twillo (for disfuct gsm module)
Built and tested on Debian Wheezy, gedit, nano, Python 2.7.3

contact by email: vento36 "at" gmail "dot" com

