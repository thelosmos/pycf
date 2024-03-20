import http.client
import secrets_file
import json
import logging

# Domain List File
inputFile = 'domainList.private.00'

# Configure logging to both file and console
logging.basicConfig(filename='ImportZones.log', filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Create a console handler
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

apiKeyEmail = secrets_file.API_KEY_EMAIL
apiKeyKey = secrets_file.API_KEY_KEY
conn = http.client.HTTPSConnection("api.cloudflare.com")
domainFile = open(inputFile, 'r')
domainList = []
headers = {
    'Content-Type': "application/json",
    'X-Auth-Email': apiKeyEmail,
    'X-Auth-Key':  apiKeyKey
    }

for l in domainFile:
    domainList.append(l.strip())
domainFile.close()

conn = http.client.HTTPSConnection("api.cloudflare.com")

for i in domainList:
    payload = {
        "account": {
            "id": secrets_file.ACCOUNT_ID
        },
        "name": i,
        "type": "full"
    }
    json_payload = json.dumps(payload)
    
    conn.request("POST", "/client/v4/zones", json_payload, headers)
    print("Attempting to register: "+ i)
    res = conn.getresponse()
    data = res.read()

    # Check if response is JSON and log formatted JSON
    try:
        json_response = json.loads(data.decode("utf-8"))
        formatted_json = json.dumps(json_response, indent=4)
        logging.info(formatted_json)
    except json.JSONDecodeError:
        # If the response is not JSON, log as is
        logging.info(data.decode("utf-8"))