import json
import requests
requests.packages.urllib3.disable_warnings()
#### Step 2: Create the variables that will be the components of the request
IP_ADDRESS= "10.10.20.48"
RESTCONF_USERNAME= "developer"
RESTCONF_PASSWORD= "C1sco12345"
DATA_FORMAT="application/yang-data+json"
api_url = f"https://{IP_ADDRESS}/restconf/data/ietf-interfaces:interfaces/interface=Loopback102"
headers = { "Accept": "application/yang-data+json",  "Content-type":"application/yang-data+json"  }
basicauth = (RESTCONF_USERNAME, RESTCONF_PASSWORD)

#### Step 3: Send a DELETE request to remove the Loopback102 interface
resp = requests.delete(api_url, auth=basicauth, headers=headers, verify=False)

if resp.status_code >= 200 and resp.status_code <= 299:
    print("STATUS OK: {}".format(resp.status_code))
    print("Loopback102 successfully deleted.")
else:
    print("Error. Status Code: {} \nError message: {}".format(resp.status_code, resp.text))
