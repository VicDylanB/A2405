"""
Dylan Bown
"""
import subprocess

try:
    Network = input("Enter Network Address: ")
    #Splits the input string into a list 
    NetworkAddress = Network.split('.') 
    dot = '.'

    NetworkAddress = NetworkAddress[0] + dot + NetworkAddress [1] + dot
    FirstHost = int(input('Enter First Host: '))
    LastHost = int(input('Enter Last Host: '))

except:
    print("Error Check format")
    exit()

