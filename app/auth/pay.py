import http.client, urllib.parse as parse, base64, uuid, json, os
from auth_jwt import token

token = token()
reference_id = str(uuid.uuid4().hex)

headers = {
    # Request headersi
    'Authorization': 'Bearer '+token,
    'X-Callback-Url': "https://45b86062.ngrok.io/",
    'X-Reference-Id': reference_id,
    'X-Target-Environment': 'sandbox',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': os.environ.get('MOMO_PRIMARY_KEY'),
}
params = parse.urlencode({})
body = json.dumps({
  "amount": "10",
  "currency": "USD",
  "externalId": "234134",
  "payer": {
    "partyIdType": "MSISDN",
    "partyId": "0778607727"
  },
  "payerMessage": "test message",
  "payeeNote": "test note"
})
try:
    conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
    conn.request("POST", "/collection/v1_0/requesttopay?%s" % params, body, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))