from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
import re
import pandas as pd 

# making first selenium script https://www.selenium.dev/documentation/webdriver/getting_started/first_script/

driver = webdriver.Chrome()

ecommerce = ["https://www.amazon.com/", "https://www.ebay.com/", "https://www.etsy.com/", "https://www.aliexpress.us/?gatewayAdapt=glo2usa", "https://us.shein.com/", "https://www.temu.com/",
             "https://www.walmart.com/", "https://www.target.com/", "https://www.rakuten.com/", "https://www.bestbuy.com/",
             "https://www.newegg.com/", "https://www.shopify.com/", "https://www.bedbathandbeyond.com/", "https://www.wayfair.com/",
             "https://www.macys.com/", "https://www.homedepot.com/", "https://www.lowes.com/", "https://www.costco.com/",
             "https://www.nordstrom.com/", "https://www.nike.com/", "https://www.samsung.com/us/"] # This is a test

news = ["https://news.yahoo.com/us/", "https://www.cbsnews.com/us/","https://www.nbcnews.com/us-news","https://www.cnn.com/", "https://www.washingtonpost.com/",
        "https://www.usatoday.com/", "https://www.latimes.com/", "https://www.nytimes.com/", "https://www.theguardian.com/us",
        "https://www.bbc.com/", "https://www.wsj.com/", "https://www.cnet.com/", "https://apnews.com/", "https://www.newsnationnow.com/",
        "https://www.pbs.org/newshour/", "https://www.reuters.com/", "https://abcnews.go.com/", "https://www.usnews.com/",
        "https://www.manilatimes.net/", "https://www.npr.org/", "https://time.com/"]

social = ["https://www.tiktok.com/explore", "https://www.pinterest.com/ideas/", "https://www.reddit.com/","https://www.youtube.com/",
          "https://www.deviantart.com/", "https://www.tumblr.com/", "https://www.linkedin.com/", "https://discord.com/", "https://www.instagram.com/",
          "https://www.facebook.com/", "https://twitter.com/", "https://www.messenger.com/?_rdr", "https://soundcloud.com/",
          "https://www.snapchat.com/", "https://www.skype.com/en/", "https://www.twitch.tv/", "https://www.craigslist.org/about/sites",
          "https://www.eharmony.com/", "https://www.christianmingle.com/en-us", "https://tinder.com/", "https://www.okcupid.com/"]

Website_Dict = {}

#This Could be very long and tedious might have to optimize later

filepath = "EasyList.txt"

# Extracting domains from EasyList
def extract_domain(line):
    # Extracting domain after '$domain=' if present
    domain_match = re.search(r'\$domain=([^\s]+)', line)
    if domain_match:
        # Handle multiple domains separated by '|'
        return [domain.strip() for domain in domain_match.group(1).split('|') if domain.strip()]
    else:
        # If '$domain=' is not present, proceed with the original method
        part = line.split('$')[0]  # Split at the first '$'
        clean_part = re.sub(r'@@\|\||\^.+|\#\#\#.+', '', part)  # Clean up
        return [domain.strip() for domain in clean_part.split(',') if domain.strip()]

ad_domains = set()
with open(filepath, 'r', encoding ='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:  # Check if the line is not empty
            domains = extract_domain(line)
            ad_domains.update(domains)  # Add domains to the set


"""
Note: Cleaing Easy Filter might still need to to be done 
Has CSS and website cleaning 
Need Cleaning: @@@ stuff 
@65429
"""
#"""
for website in ecommerce:
    driver.get(website) # navigate to the page
    driver.implicitly_wait(2) # wait 2 seconds for the page to load else it will throw an error
    images = driver.find_elements(By.TAG_NAME, "img") #list of all images on the page
    num_pixels = 0
    for i in range(len(images)):
        try:
            data = images[i].rect # This is a dictionary of the image's attributes
            width, height = data['width'], data['height']
            #print (src)
            if (width == 1 and height == 1) or (width == 0 and height == 0):  # This condition can be adjusted check for 1x1 pixel images
                src = images[i].get_attribute('src')
                if src and any (ad_url in src for ad_url in ad_domains): #Checks if image is an ad
                    num_pixels += 1             
        except (StaleElementReferenceException, NoSuchElementException):
            print("Stale element reference at index of ecommerce:", i , website)
            continue
    Website_Dict[website] = num_pixels
#"""
#"""    
for website in news:
    driver.get(website) # navigate to the page
    driver.implicitly_wait(2) # wait 2 seconds for the page to load else it will throw an error
    images = driver.find_elements(By.TAG_NAME, "img") #list of all images on the page
    num_pixels = 0
    for i in range(len(images)):
        try:
            data = images[i].rect # This is a dictionary of the image's attributes
            width, height = data['width'], data['height']
            #print (src)
            if (width == 1 and height == 1) or (width == 0 and height == 0):  # This condition can be adjusted check for 1x1 pixel images
                src = images[i].get_attribute('src')
                if src and any (ad_url in src for ad_url in ad_domains): #Checks if image is an ad
                    num_pixels += 1             
        except (StaleElementReferenceException, NoSuchElementException):
            print("Stale element reference at index of news:", i , website)
            continue
    Website_Dict[website] = num_pixels

            
for website in social:
    driver.get(website) # navigate to the page
    driver.implicitly_wait(2) # wait 2 seconds for the page to load else it will throw an error
    images = driver.find_elements(By.TAG_NAME, "img") #list of all images on the page
    num_pixels = 0
    for i in range(len(images)):
        try:
            data = images[i].rect # This is a dictionary of the image's attributes
            width, height = data['width'], data['height']
            #print (src)
            if (width == 1 and height == 1) or (width == 0 and height == 0):  # This condition can be adjusted check for 1x1 pixel images
                src = images[i].get_attribute('src')
                if src and any (ad_url in src for ad_url in ad_domains): #Checks if image is an ad
                    num_pixels += 1             
        except (StaleElementReferenceException, NoSuchElementException):
            print("Stale element reference at index of soical:", i , website)
            continue
    Website_Dict[website] = num_pixels
#"""
driver.quit()

print(Website_Dict)

dataFrame = pd.DataFrame.from_dict(list(Website_Dict.items()), columns=['Website', 'Number of Pixels'])

csv_file = 'Website_Pixels.csv'
dataFrame.to_csv(csv_file, index=False)
print( "CSV file saved to: " + csv_file)

    
    