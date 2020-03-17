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
product_name = "antaenna"

#Set the phone number you want and set it to the international format
phone_number = "+254795877416"

#Set the 3 letter ISO currency code and checkout amount
currency_code = "KES"
amount = 10.00

#You can add in your own metadata which will be resent back to you
#For the final payment notification
metadata = {
    "agentId": "9029",
    "productId": "abcd"
}

#Time to send and we'll handle the rest
try:
    res = payments.mobile_checkout(product_name, phone_number, currency_code, amount, metadata)
    print(res)
except Exception as e:
    print(f"Houston we have a problem {e}")
