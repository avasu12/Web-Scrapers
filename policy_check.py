import requests


# Retrieve robots.txt

user_agent_policy = requests.get('https://www.amazon.in/robots.txt')

robots_txt = user_agent_policy.text.splitlines()

for line in robots_txt:
    print("new line here")

buy_reeses = requests.get("https://www.amazon.in/Hersheys-Reeses-Miniature-Chocolate-Sharing/dp/B07N22FPN2/")

print(buy_reeses.text)