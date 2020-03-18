#Import the Africa's Talking SDK
import africastalking, json


# read file
with open('config.json', 'r') as f:
    data=f.read()

# parse file
config = json.loads(data)

#Set up your credentials
username,api_key = config["username"], config["apiKey"]
#Initialize the SDK
africastalking.initialize(username, api_key)

#Define the Payment service
payments = africastalking.Payment

#Set your product name
product_name = "Antaenna"

def pay(phone_number, currency_code, amount, metadata):
    """
    currency is in iso format
    phone number is in international format
    metadata is an object {}
    """
    #Time to send and we'll handle the rest
    try:
        res = payments.mobile_checkout(product_name, phone_number, currency_code, amount, metadata)
        return res
        #after a response is confirmed we redirect to the login page
        """
        Successful response is like so: 
        {
            "requestMetadata": {
                "agentId": "9029",
                "productId": "abcd"
            },
            "sourceType": "PhoneNumber",
            "source": "+254795877416",
            "provider": "Athena",
            "destinationType": "Wallet",
            "description": "Received Mobile Checkout funds from +254795877416",
            "providerChannel": "525900",
            "direction": "Inbound",
            "transactionFee": "KES 0.1000",
            "providerRefId": "ef6ae214-cb5e-4e18-8846-4f739977b60a",
            "providerMetadata": {
                "KYCInfo1": "Sample KYCInfo1",
                "KYCInfo2": "Sample KYCInfo2"
            },
            "providerFee": "KES 0.1000",
            "origin": "ApiRequest",
            "status": "Success",
            "productName": "antaenna",
            "category": "MobileCheckout",
            "transactionDate": "2020-03-17 22:09:55",
            "destination": "PaymentWallet",
            "value": "KES 10.0000",
            "transactionId": "ATPid_d8ee42c1475f8b3ae0cc2c76902a12b9"
        }
        Using https://webhook.site/ to get the payload from AT but should be replaced by an internal server 
        inorder to read the output and verify success
        """
    except Exception as e:
        print(f"Houston we have a problem {e}")
        return "Request not successful"

if __name__ == '__main__':
    metadata =  {
                "agentId": "9029",
                "productId": "abcd"
            }
    pay("+256778607727", "UGX", "3500", metadata)