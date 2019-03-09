

import time
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd


executable_path = {"executable_path": "chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)
base_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(base_url)

# html = browser.html
# soup = BeautifulSoup(html, 'html.parser')

# img_urls = []
# pic_dict = {'title': [], 'img_url': [],}

# pictures = soup.find_all('div',{"class":"item"})
# a=pictures[0].find_all("a")
# print(a[0]["href"])

browser.click_link_by_href('/search/map/Mars/Viking/cerberus_enhanced')

# print(pictures)

# for pic in pictures:
#     try:
#         t = pic.get_text()
#         title = t.strip('Enhanced')
#         time.sleep(5)
#         browser.click_link_by_href('/search/map/Mars/Viking/cerberus_enhanced')
#     except:
#         raise
#     finally:
#         browser.quit()
#     browser.click_link_by_partial_href('Enhanced')
#     browser.click_link_by_partial_text(t)    
#     url = browser.find_link_by_partial_href('download')['href']
#     image_dict = {'title': title, 'img_url': url}
#     img_urls.append(image_dict)
#     browser.visit(base_url)
# print(img_urls)