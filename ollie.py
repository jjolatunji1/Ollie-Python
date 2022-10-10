import os
import sys
import fileinput

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
                                                                                    -Anirudh Dilli
                                                                                      Twitter: https://twitter.com/VainXploits
''')

IP_var = input("Receiving IP: ")
PORT_var = input("Receiving PORT: ")


IP = print(open('file.txt', 'r').read().replace('IP', IP_var) ) # ----> Really Really important.
print(open('file.txt', 'r').read().replace(IP + 'PORT', PORT_var))

'''file = open('file.txt')
content = file.readlines()

originalStdOut = sys.stdout
with open('demo.txt', 'w') as f:
    sys.stdout = f 
    print(content[5])
    # Reset the standard output
    sys.stdout = originalStdOut'''





'''# open the sample file used
file = open('test.txt')
  
# read the content of the file opened
content = file.readlines()
  
# read 10th line from the file
print("tenth line")
print(content[9]) >'''