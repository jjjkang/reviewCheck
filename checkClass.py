from selenium import webdriver
import requests

driver = webdriver.Chrome()


def check_url_for_class(url):
    try:
        
        driver.get(url)

        elements_with_class = driver.find_elements_by_class_name("HlvSq")

        if elements_with_class:

            post_url = "https://api-endpoint.com/post_status"

            data = {"url": url, "status": "true"}

            response = requests.post(post_url, json=data)

            
            if response.status_code == 200:
               
                print(f"Posted status for {url}")
            
            else:
                #don't need to post when false, then?
                print(f"Failed to post status for {url}")
    
        else:
            print(f"false {url}")

    except Exception as e:

        print(f"Error checking URL {url}: {str(e)}")


while True:

    api_url = "https://api-endpoint.com/get_urls"
    response = requests.get(api_url)

    if response.status_code == 200:
        url_list = response.json() 
    
    else:
        print("Failed to fetch URL list from API.")
        continue

    for url in url_list:
        check_and_post_status(url)

driver.quit()

