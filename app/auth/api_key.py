import http.client, urllib.parse, base64, uuid,json, os

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': os.environ.get('MOMO_PRIMARY_KEY')
}
params = urllib.parse.urlencode({})
body = json.dumps({"providerCallbackHost": "https://45b86062.ngrok.io"})

def get_api_key():
    #apikey returned
    try:
        conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
        conn.request("POST", "/v1_0/apiuser/e996501c-e721-4ac1-97ff-dc6887b85e8c/apikey?%s" % params, body, headers)
        response = conn.getresponse()
        print(response.status)
        print(response.reason)
        data = response.read()
        conn.close()
        return json.loads(data.decode('utf-8'))["apiKey"]
    except Exception as e:
        print(e)

if __name__ == '__main__':
    print(get_api_key())
