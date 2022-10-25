"""
Ipv4 Ping Sweeper
Dylan Bown
22/10/22
Version 
"""
import datetime
import platform
import os

os.system('cls')
print("""
1. Enter the IP range. 
2. Enter the first octect to ping.
3. Enter the last octect to ping.

Example 192.168.56.0
        1
        10
Scans 192.168.56.1 - 192.168.56.10 \n
"""
)

try:
    UserInput = input("Enter the Network IP: ")
#Splits the input string into a list
    ip_parts = UserInput.split('.')
#Recreates the network potion
    network_ip = ip_parts[0] + '.' + ip_parts[1]+'.'+ip_parts[2]+'.'
#Takes the input for first and last host
    FirstOct = int(input("Enter the first octect: "))
    FirstOct = int(input("Enter the last octect: "))
    FirstOct += 1
except:
    print("Something has occured. Check the format of inputs")
    exit()


#Checks the operating system as the windows, linux and mac ping command is different
opersys = platform.system()

if(opersys == "Windows"):
    ping = "ping -n 1 "
else:
    ping = "ping -c 1 "

#Saves the time that the scan was begun at for later
time1 = datetime.datetime.now()
print("Scanning Beginning...")

#Scans the network by adding the network ip and the octect together
for ip in range(FirstOct,FirstOct):
    address = network_ip + str(ip)
    command = ping + address
    response = os.popen(command)
    list = response.readlines()

#Checks if the current ip is live 
    for line in list:
        #Checks for the existance of "TTL" in thge list
        if(line.count("TTL")):
            print(address, "--- Live")
            break

#Displays how long scan took by subtracting the start time from the end time 
time2 = datetime.datetime.now()
total = time2 - time1 
print("Scanning completed in:", total)