from getpass import getpass
username = 'dragonslayer'
password =  'demonslayer'


name = input(" Enter your Username ->")
passw = getpass(" Enter your password ->")

if name == username and passw == password :
    print("Acess Granted")
    
else :
   print("Acess Denied")