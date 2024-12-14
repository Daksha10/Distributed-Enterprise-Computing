# Import necessary classes from pyftpdlib
from pyftpdlib.authorizers import DummyAuthorizer  # Handles user authentication and permissions
from pyftpdlib.handlers import FTPHandler      	# Handles FTP requests (commands)
from pyftpdlib.servers import FTPServer        	# Manages the FTP server and listens for connections

# Configuration for the FTP server
FTP_PORT = 8087                             	# Port on which the FTP server will listen
FTP_USER = "user"                           	# Username for authenticating to the FTP server
FTP_PASSWORD = "pwd"                        	# Password for the FTP user
FTP_DIRECTORY = "/home/cslinux/Desktop/PS1"  	# The directory the user can access via FTP

def main():
	# Create an authorizer object to manage user permissions
	authorizer = DummyAuthorizer()

	# Add a user to the authorizer with specified permissions
	# 'elradfmw' permissions mean:
	# e - change directories,
	# l - list contents of directory,
	# r - retrieve file from the server,
	# a - append data to an existing file,
	# d - delete file or directory,
	# f - rename files or directories,
	# m - create directories,
	# w - store a file on the server
	authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

	# Set up the handler to manage FTP requests using the authorizer
	handler = FTPHandler
	handler.authorizer = authorizer  # Link the authorizer to the handler

	# Optional: Set a banner message when the user connects to the FTP server
	handler.banner = "pyftpdlib based ftpd ready."

	# Define the IP address and port on which the FTP server will listen
	# This binds the FTP server to IP address 10.1.66.252 and port 8087
	address = ('10.1.66.252', FTP_PORT)

	# Create the FTPServer instance with the specified address and handler
	server = FTPServer(address, handler)

	# Set limits on the number of simultaneous connections to the server
	server.max_cons = 256                  	# Maximum number of connections allowed to the server
	server.max_cons_per_ip = 5             	# Maximum number of simultaneous connections per IP address

	# Start the FTP server to listen for incoming connections
	# This will block and keep the server running indefinitely
	server.serve_forever()

# Ensure that the server starts when the script is executed
if __name__ == '__main__':
	main()
