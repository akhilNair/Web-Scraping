import requests

url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
page = requests.get(url)

print(page.text)