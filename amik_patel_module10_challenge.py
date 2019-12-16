#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path)


# In[3]:


# Visit URL
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[4]:


#Obtain high-resolution images for each of Mar’s hemispheres
#full_image_elem = browser.find_by_id('wide-image')
#full_image_elem.click()


# In[10]:


# Find the more info button and click that
browser.is_element_present_by_text('Cerberus Hemisphere Enhanced', wait_time=1)
Cerberus_Hemisphere_Enhanced = browser.find_link_by_partial_text('Cerberus Hemisphere Enhanced')
Cerberus_Hemisphere_Enhanced.click()


# In[11]:


# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


# In[23]:


# Find and save the relative image url
img_url_cerberus = img_soup.select_one('img.wide-image').get("src")
img_url_cerberus


# In[25]:


cerberus_url = f'https://astrogeology.usgs.gov{img_url_cerberus}'
cerberus_url


# In[27]:


# Find and save hemisphere title 
#title_soup = BeautifulSoup(html, 'html.parser')
#slide_elem = title_soup.select_one('ul.item_list li.slide')


# In[29]:


# Find and save hemisphere title 
cerberus_title = img_soup.find("h2", class_='title').get_text()
cerberus_title


# In[30]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[31]:


browser.is_element_present_by_text('Schiaparelli Hemisphere Enhanced', wait_time=1)
Schiaparelli_Hemisphere_Enhanced = browser.find_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
Schiaparelli_Hemisphere_Enhanced.click()


# In[34]:


# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


# In[35]:


# Find and save the relative image url
img_url_schiaparelli = img_soup.select_one('img.wide-image').get("src")
img_url_schiaparelli


# In[36]:


schiaparelli_url = f'https://astrogeology.usgs.gov{img_url_schiaparelli}'
schiaparelli_url


# In[37]:


# Find and save hemisphere title 
schiaparelli_title = img_soup.find("h2", class_='title').get_text()
schiaparelli_title


# In[38]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[40]:


browser.is_element_present_by_text('Syrtis Major Hemisphere Enhanced', wait_time=1)
Syrtis_Major_Hemisphere_Enhanced = browser.find_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
Syrtis_Major_Hemisphere_Enhanced.click()


# In[42]:


# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


# In[43]:


# Find and save the relative image url
img_url_syrtis_major = img_soup.select_one('img.wide-image').get("src")
img_url_syrtis_major


# In[44]:


syrtis_major_url = f'https://astrogeology.usgs.gov{img_url_syrtis_major}'
syrtis_major_url


# In[45]:


# Find and save hemisphere title 
syrtis_major_title = img_soup.find("h2", class_='title').get_text()
syrtis_major_title


# In[46]:


url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[47]:


browser.is_element_present_by_text('Valles Marineris Hemisphere Enhanced', wait_time=1)
Valles_Marineris_Hemisphere_Enhanced = browser.find_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
Valles_Marineris_Hemisphere_Enhanced.click()


# In[48]:


# Parse the resulting html with soup
html = browser.html
img_soup = BeautifulSoup(html, 'html.parser')


# In[49]:


# Find and save the relative image url
img_url_Valles_Marineris = img_soup.select_one('img.wide-image').get("src")
img_url_Valles_Marineris


# In[50]:


Valles_Marineris_url = f'https://astrogeology.usgs.gov{img_url_Valles_Marineris}'
Valles_Marineris_url


# In[51]:


# Find and save hemisphere title 
Valles_Marineris_title = img_soup.find("h2", class_='title').get_text()
Valles_Marineris_title


# In[ ]:




