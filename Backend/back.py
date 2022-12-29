from googlesearch import search
import config
import openai
import json
import bs4
import requests

query = input("Enter Query")

sites = []
text = ""

for url in search(query, tld='com', lang='en', num=10, start=0, stop=1, pause=2.0):
    sites.append(url)

def getdata(url): 
    r = requests.get(url) 
    return r.text 


for i in sites:
  htmldata = getdata(i) 
  soup = bs4.BeautifulSoup(htmldata, 'html.parser') 
  for data in soup.find_all("p"): 
      text+= data.get_text()
  


openai.api_key = config.api_key

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="{}\n\nTl;dr".format(text),
  temperature=0.7,
  max_tokens=500,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=1
)

json_object = json.loads(str(response))
print(json_object['choices'][0]['text'])