#fantastic five web scraping
from bs4 import BeautifulSoup
import requests
#first i scrape indeed, then women who code. making two files to write and import on our site!

#files:
fjob = open("py-jobs.txt", "w")

url = "https://www.indeed.com/jobs?q=python%20developer&l=San%20Jose%2C%20CA"
#response should be 200
#print(response)

txtresponse = requests.get("https://www.indeed.com/jobs?q=python%20developer&l=San%20Jose%2C%20CA").text
#response without .text should be 200
#print(txtresponse)
soup = BeautifulSoup(txtresponse,"html.parser")#lxml

cards1 = soup.find_all("div", "slider_container")
#print(len(cards1))
#print(cards1)

for card in cards1:
	#print("type",type(card.find("h2", {"class": "jobTitle jobTitle-color-purple"})))#.text gives error? 
	var1 = (card.find("h2", {"class": "jobTitle jobTitle-color-purple"}))
	print(var1)
	fjob.write(str(var1))
	#sometimes type is bs4.element.tag sometimes it's NoneType?
	#print("card", card.find("span", {"class": "companyName"}))
	#fjob.write(print("card", card.find("span", {"class": "companyName"})))
	#print(card.find("span", {"class": "companyName"}).text)
	#print(type(str(var1)))
	if str(var1) == "<class 'bs4.element.Tag'>":
		bsvar = (card.find("span", {"class": "companyName"}).text)
		print(bsvar)
		fjob.write(bsvar)
		fjob.write("\n")

	if str(var1) == "<class 'NoneType'>":
		nonevar = (card.find("span", {"class": "companyName"}).text)
		print(nonevar)
		fjob.write(nonevar)
		fjob.write("\n")

	print(card.find("div", {"class": "companyLocation"}).text)
	print(card.find("div", {"class": "job-snippet"}).text.strip())
	fjob.write(card.find("div", {"class": "companyLocation"}).text)

	fjob.write("\n")
	fjob.write(card.find("div", {"class": "job-snippet"}).text.strip())
	fjob.write("\n\n")
	print("")
	#var1 = card.find("h2", {"class": "jobTitle jobTitle-color-purple"})
	#var2 = var1.strip('<h2 class="jobTitle jobTitle-color-purple"><span title="')
fjob.close()