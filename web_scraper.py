from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# if chromedriver cannot be opened due to "developer cannot be verified" error, use following command in terminal after cd into the path where chromedriver file is located
# xattr -d com.apple.quarantine chromedriver

PATH = "/Users/liewfuteck/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)

def scrape_page(url):
    url = str(url)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html)
    return soup.prettify()

print(scrape_page()