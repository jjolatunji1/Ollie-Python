import os

user_in = input("What payload do you want to use: ")
IP_var = input("Receiving IP: ")
PORT_var = input("Receiving PORT: ")

file = open('assets/payloads.txt')
payloads = file.readlines()

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