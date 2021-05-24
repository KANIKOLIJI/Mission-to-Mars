
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)



# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)



html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')



slide_elem.find('div', class_='content_title')


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url



df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


df.to_html()


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# Hemispheres


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)



# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
hemisphere_title = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
 
# links = browser.find_by_css('#product-section > div.collapsible.results > div:nth-child(1) > a > img')
links = browser.find_by_css('a.product-item img')
print(links)
hemisphere_image_urls = []
base_url = "https://astrogeology.usgs.gov"
for i in range(len(links)):
    img_info = {}

    browser.find_by_css('a.product-item img')[i].click();
    img_url = browser.find_by_css('#wide-image > div > ul > li:nth-child(1) > a').first

    img_info["img_url"]=img_url['href']
    img_info["title"]=browser.find_by_css('h2.title').text
    hemisphere_image_urls.append(img_info)
    browser.back()


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls




# 5. Quit the browser
browser.quit()






