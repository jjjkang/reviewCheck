import requests

# Get List of URLs from api endpoint
api_url = "api endpoint" 
response = requests.get(api_url)

if response.status_code == 200:
    url_list = response.json() 

else:
    print("Failed to fetch URL list from API.")