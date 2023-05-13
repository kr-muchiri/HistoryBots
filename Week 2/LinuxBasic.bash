# Check the current directory
pwd

# List the files and directories in the current directory
ls

# Change to a different directory
cd /path/to/directory

# Create a new directory
mkdir new_directory

# Create a new file
touch new_file.txt

# Edit an existing file
nano existing_file.txt

# View the contents of a file
cat existing_file.txt

# Copy a file to a new location
cp existing_file.txt new_directory/

# Move or rename a file
mv existing_file.txt new_file.txt

# Remove a file
rm new_file.txt

# Remove a directory (and its contents)
rm -r new_directory


#!/bin/bash

# Display a welcome message
echo "Welcome to my Linux script!"

# Get the current date and time
now=$(date +"%Y-%m-%d %H:%M:%S")

# Display the current date and time
echo "The current date and time is $now."

# Display the name of the current user
echo "The current user is $(whoami)."

# Display the name of the operating system
echo "The operating system is $(uname -s)."

# Display the available disk space
echo "The available disk space is:"
df -h

# Display the list of running processes
echo "The following processes are currently running:"
ps aux

# Display the list of installed packages
echo "The following packages are installed on this system:"
dpkg --list

# Display the system uptime
echo "The system has been up for $(uptime -p)."

# Display a farewell message
echo "Thanks for using my Linux script! Goodbye."