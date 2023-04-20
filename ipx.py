import sys 
import client 
import argparse
 

parser = argparse.ArgumentParser()

parser.add_argument("--K", dest="api_key" , default="" ) 
parser.add_argument("--S", dest="query" , default="apache" ) 
args = parser.parse_args()   

print()
 
if args.api_key is None: 
    print("⚠️  \033[0;31mError: %s \033[0m" % (" insert criminalip api key ! "))    
    exit(0) 
elif args.query is None: 
    print("⚠️  \033[0;31mError: %s \033[0m" % (" insert query ! "))        
    exit(0) 

try:

    logo =  """
             _                     _   __   __                                                _ 
            (_)                   (_) / _| / _|                                              (_)
             _  _ __   ___  _ __   _ | |_ | |_   ___  _ __  ______   ___   ___   _ __   __ _  _ 
            | || '_ \ / __|| '_ \ | ||  _||  _| / _ \| '__||______| / __| / _ \ | '__| / _` || |
            | || |_) |\__ \| | | || || |  | |  |  __/| |           | (__ | (_) || |   | (_| || |
            |_|| .__/ |___/|_| |_||_||_|  |_|   \___||_|            \___| \___/ |_|    \__, ||_|
            | |                                                                      __/ |   
            |_|                                                                     |___/
            """
    print(logo)

    Criminalio_API_KEY = args.api_key 
    query = args.query 
    print(" ⚠️  \033[0;31mquery: %s \033[0m" % (query)) 

    api = client.Criminalip(Criminalio_API_KEY)  

    results = api.search_query(query) 

    for result in results:
        print(result["ip_address"], end=" ")
        print(result["org_name"]) 

except Exception as oeps:
    print(" ⚠️  \033[0;31mError: %s \033[0m" % ("Error occured. Check criminalip api_key"))

except Exception as e:
    print(e)  
               