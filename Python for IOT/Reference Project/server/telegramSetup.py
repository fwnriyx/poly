import requests


TOKEN = "6044657815:AAGGrGvHPIDhKiayFyuNxmEUrjnVGTfGz3Y"

# get chatid
# url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
# print(requests.get(url).json())

# send message
chat_id = 837915524
message = "hello world"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())