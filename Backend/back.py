import openai 
from googlesearch import search
query = "how to bake a cake"

sites = []

for url in search(query, tld='com', lang='en', num=10, start=0, stop=5, pause=2.0):
    sites.append(url)

print(sites)