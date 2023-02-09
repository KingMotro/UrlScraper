from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = input("Enter the URL of the web page to scrape: ")

# Headless scraping
browser = webdriver.Firefox()

browser.get(url)
# Delay for startup
time.sleep(20)
soup = BeautifulSoup(browser.page_source,"html.parser")

# Find video file hyperlinks
results = soup.find_all("a", href=lambda href: href and (href.endswith(".mp4") or href.endswith(".mkv")))

# Iterate over every url
with open("scraped_urls.txt", "w") as file:
    # write the links to a text file
    for link in results:
        file.write(link["href"] + "\n")