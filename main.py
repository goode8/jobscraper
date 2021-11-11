import csv 
from datetime inport datetime
import requests
from bs4 import BeatifulSoup#for parsing

#q = python%20developer #removed from url
#l = San%20Jose%2C%20CA #removed from url

def create_url(position, city)
	urltemp = "https://www.indeed.com/jobs?q={}&l={}"
	url = template.format(position,city)
	return url 

url = create_url("python developer", "San Jose CA")
response = requests.get(url)
#response should be 200
#response.reason
soup = BeatifulSoup(response.text,"html.parser")
#this may need work:
card = soup.find_all("div", "slider_container")
print(len(cards))
