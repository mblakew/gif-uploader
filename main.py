import requests as requests
from decouple import config

file_path = input("Please enter the path to the file you would like to upload: ")
file = ''
try:
  file = open(file_path, 'rb')
except FileNotFoundError:
  print("\nInvalid file path")
  exit()

url = 'https://api.imgur.com/3/image'
CLIENT_ID = config('CLIENT_ID')

payload = {
  'type': 'file',
  'disable_audio': '0'
  }
files = [
  ('image', file)
]
headers = {
  'Authorization': 'Client-ID {0}'.format(CLIENT_ID)
}
response = requests.request("POST", url, headers=headers, data = payload, files = files)
jsonData = response.json()
print(response.json())
print("Here is the link:\n" + jsonData["data"]["link"])

