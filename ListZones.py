import http.client
import secrets_file
import json

apiKeyEmail = secrets_file.API_KEY_EMAIL
apiKeyKey = secrets_file.API_KEY_KEY
conn = http.client.HTTPSConnection("api.cloudflare.com")


headers = {
    'Content-Type': "application/json",
    'X-Auth-Email': apiKeyEmail,
    'X-Auth-Key':  apiKeyKey
    }

# Get Zone Name and ID
conn.request("GET", "/client/v4/zones?page=1&per_page=1000", headers=headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
zoneData = json.loads(data)
for i in range (0, len (zoneData['result'])):
    zoneID = zoneData['result'][i]['id']
    zoneName = zoneData['result'][i]['name']

# List Minimum TLS Version
    conn.request("GET", "/client/v4/zones/"+zoneID+"/settings/min_tls_version?page=1&per_page=1000", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    tlsData = json.loads(data)
    tlsVer = tlsData['result']['value']


# List Ciphers
    conn.request("GET", "/client/v4/zones/"+zoneID+"/settings/ciphers?page=1&per_page=1000", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    cipherData = json.loads(data)
    alwCiphers = cipherData['result']['value']
    print(zoneID +", "+zoneName +", "+tlsVer +" ,"+str(alwCiphers))