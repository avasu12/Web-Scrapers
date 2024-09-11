import requests


# Product page

url = "https://www.amazon.com/Kitsure-Large-Dish-Drying-Rack/dp/B0B76DW8LQ/"

response = requests.get(url)

print(response.text)
print(response.status_code)