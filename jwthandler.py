import requests
import json

def My_Authenticate():
    url = "http://10.10.120.19:1338/auth/local"

    payload = json.dumps({
        "identifier": "machine1",
        "password": "pogi123"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    dict = json.loads(response.text)
    global auth_token #you can just return auth token if you want
    auth_token = dict['jwt']
    print(auth_token)


'''
Sending without Parameters
'''
def send_only():
    url = "http://10.10.120.19:1338/statuses"
    #myToken =
    #head = {'Authorization': '{}'.format(myToken)}
    #payload = "{\r\n    \"machineID\": \"machine1\",\r\n    \"status\": \"on\"\r\n}"
    #headers = {}

    payload = json.dumps({
        "machine": "machine1",
        "status": "on"
    })
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)


'''
Sending with Parameters
'''
    
def sendWithParams(machineID,status):
    myToken = auth_token  # (Dummy token, have copied actual token from session storage in chrome)
    url = "http://10.10.120.19:1338/statuses"

    head = {'Authorization': 'Bearer {}'.format(myToken), 'content-type': 'application/json'}
    headers = {'content-type': 'application/json'}

    payload = json.dumps({
        "machine": machineID,
        "status": status
    })

    response = requests.request("POST", url, headers=head, data=payload)

    pastebin_url = response.text

    print(pastebin_url) # print the response

My_Authenticate() #used to get the JWT; run once or whenever needed

sendWithParams(2, "ON")


    
  
    
    
