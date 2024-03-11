import requests
import json
import random
import time

def upload_to_thingspeak():
    api_key = "FPC7UEB6NHIZXH0O"  # Replace with your ThingSpeak API key
    heart_rate = random.randint(50, 100)
    steps = random.randint(100, 500)
    temperature = random.uniform(20.0, 30.0)
    humidity = random.uniform(30.0, 60.0)
    current_displacement = random.uniform(0.0, 10.0)

    try:
        resp = requests.get(f"https://api.thingspeak.com/update?api_key={api_key}&field1={heart_rate}&field2={steps}&field3={temperature}&field4={humidity}&field5={current_displacement}")
        result = json.loads(resp.text)
        print("Data uploaded to ThingSpeak successfully!")
        print(result)
    except Exception as e:
        print(f"Error uploading data to ThingSpeak: {e}")

if __name__ == "__main__":
    # Upload data every minute (for testing)
    while True:
        upload_to_thingspeak()
        time.sleep(20)