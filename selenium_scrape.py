# From chat.openai.com/chat
# Please note that LinkedIn has strict rules against scraping, you should use these information for educational purposes only and not for commercial use.

from selenium import webdriver
from bs4 import BeautifulSoup

# create a new Firefox browser instance
driver = webdriver.Firefox()

# navigate to the LinkedIn job search page
driver.get("https://www.linkedin.com/jobs/search/?geoId=103644278&keywords=python&location=United%20States")

# wait for the page to load
time.sleep(5)

# get the page source
page_source = driver.page_source

# close the browser
driver.quit()

# parse the page source with Beautiful Soup
soup = BeautifulSoup(page_source, 'html.parser')

# find all job posts
job_posts = soup.find_all('li', class_='job-result-card')

# iterate through the job posts and print the title, company, and location
for post in job_posts:
    title = post.find('h3', class_='job-result-card__title').text
    company = post.find('span', class_='job-result-card__company-name').text
    location = post.find('span', class_='job-result-card__location').text
    print(title, company, location)
