#!/usr/bin/env python
# coding: utf-8

# In[9]:


##### This code is continuously updated for experiments
##### DNA Center Northbound API: Hello Network
##### DNA Center => Manage Enterprise Networks and Devices
#STEP 1 => DEFINE HARD CODED VARIABLES TO BE USED IN THE SCRIPT
###### TASKS:
# TASK 1: Display the keys of the JSON response
# TASK 2: Filter => hostname, type, IP address
# TASK 3: Display filtered data in JSON format

import requests
import json
import datetime

# Suppress credential warning for this exercise
requests.packages.urllib3.disable_warnings()

print("Current date and time: ")
print(datetime.datetime.now())
print("Starting DNA Center Hello World - Simple")
print("Creating Hard Coded Variables")

# HARD-CODED VARIABLES
DNAC_scheme = 'https://'
DNAC_authority = 'sandboxdnac.cisco.com'
DNAC_port = ':443'
DNAC_path_token = '/dna/system/api/v1/auth/token'
DNAC_path = '/dna/intent/api/v1/network-device'
DNAC_user = 'devnetuser'
DNAC_psw = 'Cisco123!'

# WDNAC_user = input("Username? ")
# DNAC_psw = input("Password? ")


# In[15]:


# STEP 2 => REQUEST TOKEN BASED ON USERNAME AND PASSWORD
print("Current date and time: ")
print(datetime.datetime.now())
print('Post Token Request')

# TOKEN REQUEST
token_req_url = DNAC_scheme + DNAC_authority + DNAC_path_token
print(token_req_url)
auth = (DNAC_user, DNAC_psw)
print(type(auth))

#req = requests.request('POST', token_req_url, auth=auth, verify=False)
req = requests.post(token_req_url, auth=auth, verify=False)
#print(dir(req))
print(req.json())

print("API Return Code: " + str(req.status_code))
print("Request URL : " + token_req_url)
print("Username: " + DNAC_user)

resp = req.text
print(resp)

token = req.json()["Token"]
print("Received Token:")
print(token)
print("Length Token:")
print(len(token))


# In[19]:


#STEP 3
#REQUEST API SERVICE (USING X-AUTH-TOKEN) -- INVENTORY REQUEST
import datetime
print("Current date and time: ")
print(datetime.datetime.now())
print('Inventory Request - Network Devices')

# INVENTORY REQUEST
req_url = DNAC_scheme+DNAC_authority+DNAC_port+DNAC_path
print(req_url)
header_data = {'x-auth-token': token}
resp_devices = requests.request('GET', req_url, headers=header_data, verify=False)
print(resp_devices)
resp_devices_json = resp_devices.json()
print('-------------------------------')
#print(dir(resp_devices))
dev_dict = json.loads(resp_devices.text)
print(dev_dict["response"][0].keys())
print('-------------------------------')
print("Response (json):")
print(json.dumps(resp_devices_json, indent=2))
### keys
#### print(resp_devices_json.keys())


# # Filteren

# In[21]:


# STEP 4 => RESPONSE DATA => LOOPING AND FILTERING
print("Current date and time: ")
print(datetime.datetime.now())
print("Inventory Request - Filtering output")
# RESPONSE DATA: OUTPUT USING A LOOP TO PROCESS LIST ITEMS
for device in resp_devices_json["response"]:
    if device["type"] != None:
        print("===")
        print("Hostname: " + device["hostname"])
        print("Type: " + device["type"])
        print("IP: " + device["managementIpAddress"])
        print("MAC: " + device["macAddress"])
        print("Software Type: " + device["softwareType"])
        print("Software Version: " + device["softwareVersion"])
        #print("Reachability: " + device["reachabilityStatus"])


# In[25]:


#STEP 5 => FILTERING JSON DATA
print("Current date and time: ")
print(datetime.datetime.now())
print("Inventory Request - Providing filtered output in JSON format")
#CREATE EMPTY LIST
dev_list = []
for device in resp_devices_json["response"]:
    if device["type"] != None:
        #CREATE EMPTY LIST
        dev_dict = {}
        dev_dict["hostname"] = device["hostname"]
        dev_dict["type"] = device["type"]
        dev_dict["macAddress"] = device["macAddress"]
        dev_dict["managementIpAddress"] = device["managementIpAddress"]
        dev_dict["serialNumber"] = device["serialNumber"]
        dev_dict["softwareType"] = device["softwareType"]
        dev_dict["softwareVersion"] = device["softwareVersion"]
        #dev_dict["reachabilityStatus"] = device["reachabilityStatus"]
        dev_list.append(dev_dict)
#print(dev_list)
print(json.dumps(dev_list, indent=16))


# # Omzetten naar Spreadsheet 

# In[28]:


import pandas as pd

# Step 4 and 5: Filter Data
dev_list = []
for device in resp_devices_json["response"]:
    if device["type"] != None:
        dev_dict = {
            "Hostname": device["hostname"],
            "Type": device["type"],
            "MAC Address": device["macAddress"],
            "Management IP": device["managementIpAddress"],
            "Serial Number": device["serialNumber"],
            "Software Type": device["softwareType"],
            "Software Version": device["softwareVersion"]
        }
        dev_list.append(dev_dict)

# Step 6: Convert to Excel
df = pd.DataFrame(dev_list)
output_file = "C:\\Users\\stefa\\Documents\\Informatica\\Fase_3\\Devnet\\StefanSutanto_DNA_center_1_Northbound_api_Hello_network.xlsx"
df.to_excel(output_file, index=False)

print(f"Data successfully exported to {output_file}")


# In[ ]:




