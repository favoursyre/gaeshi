#I want to create a Virtual Machine Detector

#Useful libraries that I would be working with -->
import os
import sys 
import subprocess 
import re 
import uuid
import socket
import ctypes
import time
import requests
import urllib.request
from scapy.all import *


#This function helps get the vendor of a specified mac address
def macVendor(mac_address):
    #This loops helps to handle connection error and retries connecting 
    count = 0
    while True:
        try:
            url = "https://api.macvendors.com/"
            response = urllib.request.urlopen(url + mac_address).read().decode('utf8')
            print("got mac response successfully")
            break
        except:
            url = "https://api.macvendors.com/"
            print("response wasn't successfully, retrying the connection")
            time.sleep(3)
            response = urllib.request.urlopen(url + mac_address).read().decode('utf8')
            count += 1
            if count == 5:
                response = "Microsoft"
                print(f"retried connecting for {count} times, {response} has been designated as the target's mac vendor instead")
                break
            else:
                pass

    print(f"Response: {response}")

    if not response:
        raise Exception("[!] Invalid MAC Address!")
    return response

#Declaring the function to handle the checking of vm ware
def status():
    try:
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        #print(f"Mac: {mac}")
        vm_vendors = ["VMware, Inc."] #Add other vm ware companies if there's any
        vendor = macVendor(mac)
        #print(f"Vendor: {vendor}")
        for i in vm_vendors:
            if i == vendor:
                stat = True
                #break
                print(os.path.basename(sys.argv[0]))
                sys.exit()
            else:
                stat = False
    except Exception as e:
        stat = f"An error occurred in vm ware status due [{e}]"
    return stat
        
        
if __name__ == '__main__':
    #Commencing the code
    print("Gaeshi Virtual Machine Detector \n")

    detect = status()
    print(f"VM Status: {detect}")

    print("\nExecuted successfully!!")
