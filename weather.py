import requests
import csv
import os
import matplotlib.pyplot as plt
API_KEY = 'b438d6e68c344c60a9d171103240707'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

def save_to_csv(data, filename='weather_data.csv'):
    file_exists = os.path.isfile(filename)  
    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

def get_weather(city):
    params = {
        'key': API_KEY,
        'q': city
    }
    response = requests.get(BASE_URL, params=params)
    print(f"Request URL: {response.url}")  
    print(f"Response Status Code: {response.status_code}")  
    print(f"Response Content: {response.content.decode('utf-8')}")
    if response.status_code == 200:
        data = response.json()
        return {
            'city': data['location']['name'],
            'temperature': data['current']['temp_c'],
            'weather': data['current']['condition']['text'],
            'humidity': data['current']['humidity'],
            'wind_speed': data['current']['wind_kph']
        }
    else:
        return None

# show the data
def visualize_weather(data):
    labels = ['Temperature (°C)', 'Humidity (%)', 'Wind Speed (kph)']
    values = [data['temperature'],data['humidity'],data['wind_speed']]

    plt.figure(figsize=(10,6))
    plt.bar(labels,values,color=['blue','green','red'])
    plt.xlabel('Weather Metrics')
    plt.ylabel('Values')
    plt.title(f"Weather Data for {data['city']}")
    plt.show()



city = input("Enter City name: ")
weather_data = get_weather(city)

if weather_data:
    print(f"City: {weather_data['city']}")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Weather: {weather_data['weather']}")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Wind Speed: {weather_data['wind_speed']} m/s")
    save_to_csv(weather_data)
    visualize_weather(weather_data)

else:
    print("City not found or API request failed.")
