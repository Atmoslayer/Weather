import requests

url1 = 'https://wttr.in/London?lang=ru&m&p'
url2 = 'https://wttr.in/SVO?lang=ru&m&p'
url3 = 'https://wttr.in/Cherepovets?lang=ru&m&p'

response1 = requests.get(url1)
response2 = requests.get(url2)
response3 = requests.get(url3)

print(response1.text)
print(response2.text)
print(response3.text)


