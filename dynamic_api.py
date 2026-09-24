import requests
import json
import time

print(" Global University Finder")
country_name = input("Enter a country name (e.g., Bangladesh, Canada): ")


url = "http://universities.hipolabs.com/search"


payload = {
    "country": country_name
}

print("Fetching data, please wait...")
time.sleep(2)


try:
        response = requests.get(url, params=payload)
        if response.status_code == 200:
            data = response.json()
              
            print(f"Total Number Of Universities:, {len(data)}")
              

   
        
            print("\n--- Top 5 Universities ---")
        
        
            
            if len(data) == 0:
                print("Sorry, no universities found for this keyword.")
            else:
    
                limit = min(5, len(data))
                top_unis=[]
                for i in range(limit):
                    print(data[i]["name"])
                    top_unis.append(data[i])
            file_name = f"{country_name}_universities.json"
            with open (file_name, "w") as file:
                json.dump(top_unis, file, indent=4)
            print(f"\n Data Successfully Saved To {file_name}")    
            

        else:
            print("Error Can't Proceed... Try again!")
        
      

except Exception as e:
    print(f"Connection Error: {e}")