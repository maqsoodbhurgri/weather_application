import requests

def get_weather(city, api_key):
  
    url = "https://api.openweathermap.org/data/2.5/weather"
    
   
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric" 
    }


    response = requests.get(url, params=params)
    data = response.json()

    
    if response.status_code == 200:
        print("===================================")
        print("City:", data["name"])
        print("Country:", data["sys"]["country"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("Wind Speed:", data["wind"]["speed"], "m/s")
        print("===================================")
    else:
        print("City not found or invalid request!")

def main():
    print("=== Simple Weather CLI App ===")

    # put your api here for working
    api_key = "YOUR_API_KEY_HERE"

    while True:
        city = input("Enter city name (or type 'exit' to quit'): ")

        if city.lower() == "exit":
            print("Goodbye!")
            break

        get_weather(city, api_key)


if __name__ == "__main__":
    main()
