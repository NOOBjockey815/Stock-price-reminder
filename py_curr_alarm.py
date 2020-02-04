import requests
import json
from playsound import playsound
import time 

#Get the free API key from https://www.alphavantage.co/support/#api-key"
api_key = "Paste API key here"

#To get the desired currency exchange, change from_currency and to_currency
url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=INR&apikey=api_key"
 
req_ob = requests.get(url) 
 
result = req_ob.json() 
#print(result)

#Get the Exchange rate from the dictionary
Ex_rate = result["Realtime Currency Exchange Rate"] ['5. Exchange Rate'] #To get the Exchange rate from the dictionary

print("Exchange Rate: ", Ex_rate)
while(1):
      time.sleep(300) #For delay in seconds
      print("Exchange Rate: ", Ex_rate)
      if(Ex_rate<="71.230"):
            playsound('you_suffer.mp3')  #For playing Sound