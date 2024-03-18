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
conn.request("GET", "/client/v4/zones?per_page=100", headers=headers)
res = conn.getresponse()
zoneData = res.read().decode("utf-8")
jZoneData = json.loads(zoneData)
print("Zone ID, Zone Name, Record Type, Record Name, Record Content")
for i in range (0, len (jZoneData['result'])):
    zoneID = jZoneData['result'][i]['id']
    zoneName = jZoneData['result'][i]['name']

# List Records
    conn.request("GET", "/client/v4/zones/"+zoneID+"/dns_records", headers=headers)
    res = conn.getresponse()
    recordsData = res.read().decode("utf-8")
    jRecordsData = json.loads(recordsData)
    for i in range (0, len (jRecordsData['result'])):
        zoneRecordType = jRecordsData['result'][i]['type']
        zoneRecordName = jRecordsData['result'][i]['name']
        zoneRecordContent = jRecordsData['result'][i]['content']
        print(zoneID +", "+zoneName +", "+zoneRecordType +", "+zoneRecordName +", "+zoneRecordContent )