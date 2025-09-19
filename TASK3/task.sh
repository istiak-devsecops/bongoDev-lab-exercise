#!/bin/bash

##########################
# Author: Istiak Ahmed   #
# Date: 19-sep-2025      #
##########################

# prompt for email 
read -p "What is your email: " email_address

# prompt for password
read -s -p "Choose a password: " password
echo # added a new line for clear output

# show the info as output
echo "Your email is: $email_address"
echo "Your password is: $password"

