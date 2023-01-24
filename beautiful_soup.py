# From chat.openai.com/chat
# Please note that LinkedIn has strict rules against scraping, you should use these information for educational purposes only and not for commercial use.
import requests
from bs4 import BeautifulSoup

URL = "https://www.linkedin.com/jobs/search/?geoId=103644278&keywords=python&location=United%20States"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("li", class_="job-result-card")

for result in results:
    title = result.find("h3", class_="job-result-card__title").text
    company = result.find("span", class_="job-result-card__company-name").text
    location = result.find("span", class_="job-result-card__location").text
    print(title, company, location)
