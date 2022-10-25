"""
Dylan Bown
2/10/22
"""
import datetime
import platform
import os

print("""
1. Enter the IP range. 
2. Enter the first number to ping.
3. Enter the last number to ping.

Example 192.168.56.0
        1
        10
Scans 192.168.56.1 - 192.168.56.10 \n
"""
)

try:
    user_input = input("Enter the Network IP: ")
    #Splits the input string into a list
    ip_parts = user_input.split('.')
    #Recreates the network potion
    network_ip = ip_parts[0] + '.' + ip_parts[1]+'.'+ip_parts[2]+'.'

    first_host = int(input("Enter the first number: "))
    last_host = int(input("Enter the last number: "))
    last_host += 1
except:
    print("Something has occured. Check the format of inputs")
    exit()

oper = platform.system()

if(oper == "Windows"):
    ping = "ping -n 1 "
else:
    ping = "ping -c 1 "

time1 = datetime.datetime.now()
print("Scanning Beginning")

for ip in range(first_host,last_host):
    addr = network_ip + str(ip)
    command = ping + addr
    response = os.popen(command)
    list = response.readlines()

    for line in list:
        if(line.count("TTL")):
            print(addr, "--- Live")
            break

time2 = datetime.datetime.now()
total = time2 - time1 
print("Scanning complete in ", total)