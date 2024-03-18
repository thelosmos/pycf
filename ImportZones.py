import http.client
import secrets_file
import json

apiKeyEmail = secrets_file.API_KEY_EMAIL
apiKeyKey = secrets_file.API_KEY_KEY
conn = http.client.HTTPSConnection("api.cloudflare.com")
domainFile = open('testDomainList', 'r')
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

    print(data.decode("utf-8"))

    print(result)