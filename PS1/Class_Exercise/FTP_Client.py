import ftplib

# FTP server details
HOSTNAME = "10.1.66.252"  # Replace with the correct IP address
USERNAME = "user"
PASSWORD = "pwd"

# Create an FTP connection
ftp_server = ftplib.FTP()

# Try connecting to the server (adjust hostname and port if needed)
ftp_server.connect(HOSTNAME, 8087)

# Login with the provided credentials
ftp_server.login(USERNAME, PASSWORD)
ftp_server.encoding = "utf-8"

# Local file to upload (without the full path in the filename argument)
filename = "Hello.txt"  # Use only the file name here (not the full path)

# Open the local file in binary read mode
with open("/home/cslinux/Documents/Hello.txt", "rb") as file:
	# Upload the file using the STOR command
	ftp_server.storbinary(f"STOR {filename}", file)

# List the contents of the current directory on the FTP server
ftp_server.dir()

# Quit the FTP session
ftp_server.quit()
