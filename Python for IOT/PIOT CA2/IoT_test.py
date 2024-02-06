import requests
import json

def upload_to_thingspeak(heart_rate, steps, temperature, humidity, current_displacement):
    api_key = "FPC7UEB6NHIZXH0O"  # Replace with your ThingSpeak API key
    field1 = str(heart_rate)
    field2 = str(steps)
    field3 = str(temperature)
    field4 = str(humidity)
    field5 = str(current_displacement)

    try:
        resp = requests.get(f"https://api.thingspeak.com/update?api_key={api_key}&field1={field1}&field2={field2}&field3={field3}&field4={field4}&field5={field5}")
        result = json.loads(resp.text)
        print("Data uploaded to ThingSpeak successfully!")
        print(result)
    except Exception as e:
        print(f"Error uploading data to ThingSpeak: {e}")

if __name__ == "__main__":
    # Example fake data (replace with your actual data)
    fake_heart_rate = 75
    fake_steps = 200
    fake_temperature = 25.5
    fake_humidity = 45.0
    fake_distance = 5.0

    # Call the function to upload data to ThingSpeak
    upload_to_thingspeak(fake_heart_rate, fake_steps, fake_temperature, fake_humidity, fake_distance)