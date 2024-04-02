import http.client
import secrets_file
import json

apiKeyEmail = secrets_file.API_KEY_EMAIL
apiKeyKey = secrets_file.API_KEY_KEY
conn = http.client.HTTPSConnection("api.cloudflare.com")

listID = input("Please enter the list ID: ")


headers = {
    'Content-Type': "application/json",
    'X-Auth-Email': apiKeyEmail,
    'X-Auth-Key':  apiKeyKey
    }

conn.request("GET", "/client/v4/accounts/"+secrets_file.ACCOUNT_ID+"/rules/lists/"+listID+"/items?per_page=500", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))