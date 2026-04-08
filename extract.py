import requests 
import datetime
import json

def extract():
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin,ethereum,solana,cardano,ripple'
    
    try :
        #API call
        response = requests.get(url)

        #check status code
        if response.status_code != 200: 
            print(f"API error : {response.status_code}")
            return 

        data = response.json()

        #create a filename 
        file_name = "raw_data/coins_"+datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")+".json"
        
        #save file    
        with open(file_name, 'w') as file:
            json.dump(data, file)
    except requests.exceptions.ConnectionError:
        print("Network error: could not reach the API")


if __name__ == "__main__":
    extract()