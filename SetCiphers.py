import http.client
import secrets_file
import json

apiKeyEmail = secrets_file.API_KEY_EMAIL
apiKeyKey = secrets_file.API_KEY_KEY
conn = http.client.HTTPSConnection("api.cloudflare.com")

cfCompCiphers = "{\n  \"value\": [\n    \"ECDHE-ECDSA-AES128-GCM-SHA256\",\n    \"ECDHE-ECDSA-CHACHA20-POLY1305\",\n    \"ECDHE-RSA-AES128-GCM-SHA256\",\n    \"ECDHE-RSA-CHACHA20-POLY1305\",\n    \"ECDHE-ECDSA-AES256-GCM-SHA384\",\n    \"ECDHE-RSA-AES256-GCM-SHA384\",\n    \"ECDHE-ECDSA-AES128-SHA256\",\n    \"ECDHE-RSA-AES128-SHA256\",\n    \"ECDHE-ECDSA-AES256-SHA384\",\n    \"ECDHE-RSA-AES256-SHA384\"\n  ]\n}"
cfModCiphers = "{\n  \"value\": [\n    \"ECDHE-ECDSA-AES128-GCM-SHA256\",\n    \"ECDHE-ECDSA-CHACHA20-POLY1305\",\n    \"ECDHE-RSA-AES128-GCM-SHA256\",\n    \"ECDHE-RSA-CHACHA20-POLY1305\",\n    \"ECDHE-ECDSA-AES256-GCM-SHA384\",\n    \"ECDHE-RSA-AES256-GCM-SHA384\"\n ]\n}"
cipherReset = "{\n  \"value\":[]}"

headers = {
    'Content-Type': "application/json",
    'X-Auth-Email': apiKeyEmail,
    'X-Auth-Key':  apiKeyKey
    }


zoneID = input("Enter Zone ID: ")
conn.request("PATCH", "/client/v4/zones/"+zoneID+"/settings/ciphers", cipherReset, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

cipherData = json.loads(data)
alwCiphers = cipherData['result']['value']
print("Configured ciphers for zone: " +zoneID)
print(zoneID +", "+str(alwCiphers))