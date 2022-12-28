from googlesearch import search
import config
import openai
import json
import bs4
import requests

query = input("Enter Query")

sites = []
text = ""

for url in search(query, tld='com', lang='en', num=10, start=0, stop=3, pause=2.0):
    sites.append(url)

for i in sites:
  res = requests.get(i)
  soup = bs4.BeautifulSoup(res.content, "html.parser")
  A = soup(text=lambda t: "{}".format(query) in t.text)
  for i in A:
    text = text+i

print(text)

#openai.api_key = config.api_key

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="A neutron star is the collapsed core of a massive supergiant star, which had a total mass of between 10 and 25 solar masses, possibly more if the star was especially metal-rich.[1] Neutron stars are the smallest and densest stellar objects, excluding black holes and hypothetical white holes, quark stars, and strange stars.[2] Neutron stars have a radius on the order of 10 kilometres (6.2 mi) and a mass of about 1.4 solar masses.[3] They result from the supernova explosion of a massive star, combined with gravitational collapse, that compresses the core past white dwarf star density to that of atomic nuclei.\n\nTl;dr",
  temperature=0.7,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=1
)

json_object = json.loads(str(response))
print(json_object['choices'][0]['text'])