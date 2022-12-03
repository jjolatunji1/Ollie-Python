import os
import urllib.parse
import base64

#########################################################

print('''
 .----------------. .----------------. .----------------. .----------------. .----------------. 
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |     ____     | | |   _____      | | |   _____      | | |     _____    | | |  _________   | |
| |   .'    `.   | | |  |_   _|     | | |  |_   _|     | | |    |_   _|   | | | |_   ___  |  | |
| |  /  .--.  \  | | |    | |       | | |    | |       | | |      | |     | | |   | |_  \_|  | |
| |  | |    | |  | | |    | |   _   | | |    | |   _   | | |      | |     | | |   |  _|  _   | |
| |  \  `--'  /  | | |   _| |__/ |  | | |   _| |__/ |  | | |     _| |_    | | |  _| |___/ |  | |
| |   `.____.'   | | |  |________|  | | |  |________|  | | |    |_____|   | | | |_________|  | |
| |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------' 
                                                                                    @0dayCTF, @VainXploits
                                                                                      Twitter: https://twitter.com/0dayCTF
                                                                                      Twitter: https://twitter.com/VainXploits
                                                                                    
''')

# Variables
user_in = input("What payload do you want to use: ")
IP_var = input("Receiving IP: ")
PORT_var = input("Receiving PORT: ")


def display_payload_options():
  f = open('assets/payloads.txt', 'r')
  file_contents = f.read()
  print(file_contents)
  f.close()

# display_payload_options()

file = open('assets/payloads.txt')
payloads = file.readlines()

# First function to replace the IP variable from teh payloads
def display_one():
  kilo = open('assets/payloads.txt')
  content1 = kilo.readlines()
  f = open("assets/current-payload.txt", "x+")
  f = open('assets/current-payload.txt', 'w')
  f.write(payloads[int(user_in)].replace('IP', IP_var))
display_one()

# Second
def display_actual():
  file2 = open('assets/current-payload.txt')
  print_payload = file2.readlines()
  print(print_payload[0].replace('PORT', PORT_var))
  file2.close()
  os.remove('assets/current-payload.txt')
display_actual()

# This function is for urlencoding the payloads.
def url_encode():
  alpha = urllib.parse.quote('payload', safe='')
  print(alpha)

# This function is for double urlencoding the payloads.
def double_url_encode():
  bravo = urllib.parse.quote('payload', safe='')
  charlie = urllib.parse.quote(bravo, safe='')
  print(charlie)

# This function is for base64 encoding the payloads.
def base64_encode():
  delta = 'PAYLOAD'
  echo = delta.encode('utf-8')
  foxtrot = base64.b64encode(echo)
  print(foxtrot.decode('utf-8'))

# TODO: Work on printing the stuff from display_payload_options() function in a grid format. Ref: https://stackoverflow.com/questions/32460832/print-a-list-of-strings-in-a-grid-format-python
# TODO: Work on listener options.
# TODO: Work on how I can do most of this from single command in the terminal instead of throwing the user a whole bunch of fucking prompts once they run the tool.
# TODO: ^^ Includes how to select Reverse, Bind or MSF and how to select a particular payload they want(inside the sections in the revhsells website).
# TODO: Start working on displaying listener options cause it's easier compared to shell options. Then work on printing them in a grid option, preferably using a for loop to go through the 'assets/listener-options.txt' and replacing PORT and in the case of MSF replacing the IP aswell.