# ATM-Socket
Automated Teller Machine (ATM) Socket Program

Description:

This program will involve the idea of modern-day banking using an
automated teller machine (ATM). The server-side software maintains a bank account and a user
accesses the account via client software.

For this program, we can assume that a single account
will be accessed by a single user. This avoids synchronization problems with multiple users. 


How To Run The Program:

If user tries to run in local computer:
	1. Navigate over to the location of the file inside the file manager.
	2. on the search bar, type 'cmd'
	3. inside the command prompt, type 'py -3.7 server.py'
		note: it is important to run the server before the client
	              python type depends on the host computer (can be 3.8 or 3.9)
	4. open another command prompt from the same location and type 'py -3.7 client.py'

If user tries to run in turing:
	1. login to turing via command prompt
	2. type 'cd' + name of the folder
	3. type 'python3 server.py'
	4. open another turing and do the same previous steps
	5. instead of typing 'python3 server.py', type: 'python3 client.py'
