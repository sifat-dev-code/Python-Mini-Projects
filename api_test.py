import requests

print(" Connecting to the Internet...")


url = "https://official-joke-api.appspot.com/random_joke"

try:
        response = requests.get(url)
        if response.status_code == 200:
              print("Connection Successful")
              data = response.json()
              print(f"Setup: {data['setup']}\n Punchline: {data['punchline']}")

        
        else:
            print("Failed to fetch")

         
   
except Exception as e:
    print(f" Error occurred: {e}")
    print("Make sure your internet is working!")