#!/bin/python3

# The sys module provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter
import sys

# The socket module implements sockets so that it can be used in the program for Internet communication. This is what allows to make a node-to-node connenction
import socket

# The datetime module allows to create a banner and show the date and time when running the Python scanner
from datetime import datetime

# End goal accepts 2 arguments: python3 scanner.py <ip>
# Define the target

if len(sys.argv) == 2:
	# Create a variable called "target" and set it equal to the 1st argument
	target = socket.gethostbyname(sys.argv[1]) # Translate hostname to IPv4 address
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py")


# Add a pretty banner
print("-" * 50)
print("Scanning target "+ target)
print("Time started: "+ str(datetime.now()))
print("-" * 50)


# Try-catch statement

try:
	# Full on port scanner consists of ports (1, 65535)
	for port in range(100,150):
	
		# AF_INET is the IPv4 address
		# SOCK_STREAM is the port
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		# This is going to attempt to connect to a port and if that port is not connectable then it will wait 1 second and then it will move onto the next port
		socket.setdefaulttimeout(1)
		
		# Store the result
		result = s.connect_ex((target,port)) #returns an error indicator - if port is open it throws a 0, otherwise 1
		
		# Enable the below statement after it is built out
		print("Checking port {}".format(port))
		
	
		if result == 0:
			print("Port {} is open".format(port))
		s.close()



# A few exceptions to make the code flawless
except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to server.")
	sys.exit()
	
	
