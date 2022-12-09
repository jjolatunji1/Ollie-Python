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
 '----------------' '----------------' '----------------' '----------------' '----------------'  -v1
                                                                                    @0dayCTF, @VainXploits
                                                                                      Twitter: https://twitter.com/0dayCTF
                                                                                      Twitter: https://twitter.com/VainXploits
''')

# Bash NC C Haskell Perl Perl PHP Windows ConPty Powershell Python Python3 Ruby socat node.js java js groovy telnet zsh lua golang vlang awk dart

# Variables
payload_options_reverse = ["1. Bash", "2. Cats", "3. C", "4. Haskell", "5. Perl", "6. PHP", "7. Windows ConPty", "8. Powershell", "9. Python", "10. Python3", "11. Ruby", "12. socat", "13. node.js", "14. java", "15. Groovy", "16. telnet", "17. zsh", "18. lua", "19. golang", "20. vlang", "21. awk", "22. dart"]
listener_options = ['1. nc', '2. ncat', '3. ncat.exe', '4. ncat(TLS)', '5. rlwrap+nc', '6. rustcat', '7. rustcat+history', '8. pwncat', '9. Windows ConPty', '10. socat', '11. socat(TTY)', '12. powercat', '13. msfconsole']
bash_payloads = ["1. Bash -1", "2. Bash 196", "3. Bash read line", "4. Bash 5", "5. Bash UDP"]
cats_payloads = ["1. nc mkfifo", "2. nc -e", "3. nc.exe -e", "4. nc -c", "5. ncat -e", "6. ncat.exe -e", "7. ncat UDP", "8. rustcat"]

def display_payload_options():
  for i in payload_options_reverse:
    print(i)
display_payload_options()

user_in_main = input("What payload do you want to use: ")

# Work in progress
def display_payload_options_reverse():
  if user_in_main == "1":
    for i in bash_payloads:
      print(i)
  elif user_in_main == "2":
    for beta in cats_payloads:
      print(beta)
  else:
    print("Hi")
  # elif user_in == "3":
  #   return True

# TODO: rewrite display_one and display_actual for each payload_options_reverse AND if user_in_main = x, display_actual to get from specific bash/cats/c/haskell/etc folders.

display_payload_options_reverse()

user_in = input("What payload do you want to use: ")
IP_var = input("Receiving IP: ")
PORT_var = input("Receiving PORT: ")

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

def print_listener_options(listener_options):
  for lists in listener_options:
    print(lists)
print_listener_options(listener_options)

listener_options_input_yorn = input("Do you want to use any of the above payloads?(Y/N) ")

def listener_options_exec():
  if listener_options_input_yorn.lower() == "y":
    listener_options_userin = input("Which payload do you want to use: ")
    listener_options_userin_port = input("What port are you listening on? ")
    file3 = open('assets/listener-options.txt')
    print_listener = file3.readlines()
    print(print_listener[int(listener_options_userin)].replace('PORT', listener_options_userin_port))
  else:
    print("Have fun hacking! 🚀")
listener_options_exec()

##############################ENCODING PAYLOAD SECTION OF CODE##############################
# This function is for urlencoding the payloads. Needs working on
def url_encode():
  alpha = urllib.parse.quote('payload', safe='')
  print(alpha)

# This function is for double urlencoding the payloads. Needs working on
def double_url_encode():
  bravo = urllib.parse.quote('payload', safe='')
  charlie = urllib.parse.quote(bravo, safe='')
  print(charlie)

# This function is for base64 encoding the payloads. Needs working on
def base64_encode():
  delta = 'PAYLOAD'
  echo = delta.encode('utf-8')
  foxtrot = base64.b64encode(echo)
  print(foxtrot.decode('utf-8'))
##############################ENCODING PAYLOAD SECTION OF CODE##############################
# TODO: Work on printing the stuff from display_payload_options() function in a grid format. Ref: https://stackoverflow.com/questions/32460832/print-a-list-of-strings-in-a-grid-format-python
# TODO: Work on listener options.
# TODO: Work on how I can do most of this from single command in the terminal instead of throwing the user a whole bunch of fucking prompts once they run the tool.
# TODO: ^^ Includes how to select Reverse, Bind or MSF and how to select a particular payload they want(inside the sections in the revhsells website).
# TODO: Start working on displaying listener options cause it's easier compared to shell options. Then work on printing them in a grid option, preferably using a for loop to go through the 'assets/listener-options.txt' and replacing PORT and in the case of MSF replacing the IP aswell.
# TODO: Research input range because huge payloads like the C ones, PHP ones and lot of others exist in singular files rather than in one payloads.txt so I have to use the input ranges in the if conditional statements to make it work.