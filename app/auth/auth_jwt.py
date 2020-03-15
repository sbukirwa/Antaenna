import http.client, urllib.parse as parse, base64, os, json
from api_key import get_api_key

api_user = os.environ.get('MOMO_API_USER') 
api_key = str(get_api_key())
api_user_and_key  = api_user+':'+api_key
encoded = base64.b64encode(api_user_and_key.encode())
headers = {
# Request headers
'Authorization': 'Basic '+(encoded.decode()),
'Ocp-Apim-Subscription-Key': os.environ.get('MOMO_PRIMARY_KEY'),
}
params = parse.urlencode({
})
def token():
    try:
        conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.com')
        conn.request("POST", "/collection/token/?%s" % params, "{body}", headers)
        response = conn.getresponse()
        print(response.status)
        print(response.reason)
        data = response.read()
        result = json.loads(data.decode())["access_token"]
        conn.close()
        return result
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

if __name__ == '__main__':
    token()