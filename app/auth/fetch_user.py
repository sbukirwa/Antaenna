import http.client, urllib.parse as parse, base64, uuid, json, os
headers = {
    # Request headers
    'X-Reference-Id': str(uuid.uuid4().hex),
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': os.environ.get('MOMO_PRIMARY_KEY'),
}
params = parse.urlencode({})
body = json.dumps({
  "providerCallbackHost":  str(os.environ.get('MOMO_CALLBACK_URL'))})
try:
    conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
    conn.request("POST", "/v1_0/apiuser?%s" % params, body, headers)
    response = conn.getresponse()
    print(response.status)
    print(response.reason)
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print(e)