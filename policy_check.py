import requests


# Retrieve robots.txt

response = requests.get('https://github.com/robots.txt')

print(response.headers)
