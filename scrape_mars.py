#!/usr/bin/env python
# coding: utf-8

# In[16]:


import time
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import re

# function to call each scrape
# a function to unify all little functions and return a big dictionary
# In[17]:

def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=True)

def scraping():
    Browser = init_browser()
    url = 'https://mars.nasa.gov/news/'
    Browser.visit(url)
    html = Browser.html
    soup = BeautifulSoup(html, 'html.parser')
    mars_data_scrape = {}

# In[18]:


    news_title = soup.find('div', class_='content_title').get_text()
    news_p = soup.find('div', class_='article_teaser_body').get_text()
    time.sleep(5)
    mars_data_scrape['data_1'] = news_title
    mars_data_scrape['data2'] = news_p

# In[19]:


    # executable_path = {"executable_path": "chromedriver"}
    # browser = Browser("chrome", **executable_path, headless=True)
    Browser = init_browser()
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    Browser.visit(url)

    Browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)
    Browser.click_link_by_partial_text('more info')
    time.sleep(2)
    Browser.click_link_by_partial_text('.jpg')


# In[20]:


    html = Browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_img_url = soup.find('img').get('src')
    mars_data_scrape['image'] = featured_img_url

# In[50]:


    url_twitter = 'https://twitter.com/marswxreport?lang=en'
    html = requests.get(url_twitter)
    soup = BeautifulSoup(html.text, 'html.parser')

    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    mars_data_scrape['weather'] = mars_weather


# In[51]:


    url = 'https://space-facts.com/mars/'
    table_df = pd.read_html(url)[0]
    table_df = table_df.rename(columns={0:'Mars Planet Profile', 1:''})
    table_df = table_df.set_index('Mars Planet Profile', drop=True)
    mars_data_scrape['table'] = table_df.to_html()


# In[52]:


    table = table_df.to_html(classes = 'table table-striped')


# In[91]:

    Browser = init_browser()
    hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    Browser.visit(hemispheres_url)
    html_hemispheres = Browser.html
    soup = BeautifulSoup(html_hemispheres, 'html.parser')
    items = soup.find_all('div', class_='item')

    hemisphere_image_urls = []
    hemispheres_main_url = 'https://astrogeology.usgs.gov'

    for item in items: 
        title = item.find('h3').text
        partial_img_url = item.find('a', class_='itemLink product-item')['href']
        Browser.visit(hemispheres_main_url + partial_img_url) 
        partial_img_html = Browser.html
        soup = BeautifulSoup( partial_img_html, 'html.parser')
        img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']
        hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
        
    mars_data_scrape['hemispheres'] = hemisphere_image_urls

    return mars_data_scrape
