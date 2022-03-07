import os
import smtplib


from email.message import EmailMessage
from distutils.filelist import findall
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
import urllib.request
from urllib.request import FancyURLopener
pink_heart_purse_url = "https://www.coachoutlet.com/products/heart-crossbody-in-colorblock/C6952-IMP1X.html?frp=C6952%20IMP1X&isSPC=true"
nolita_white_flower_url = "https://www.coachoutlet.com/products/nolita-19-with-heart-petal-print/C7658.html?frp=C7658%20IMCAH"
    # Uploading webscraping info to a file
    # filename = "products.txt"
    # f = open(filename, "w")
    # headers = "item, price, availability\n"
    # f.write(headers)

# count attempt
coach_job_number = 0
converse_job_number = 0

# scraper, sends email whenever executed
def coach_scrape(coach_url):
    # Opening up connection, grabbing page
    uClient = urlopen(coach_url)
    page = uClient.read()
    uClient.close()

    # html parsing
    page_soup = soup(page, "html.parser")

    # finds attributes in section based on 'class'
    item_name_container = page_soup.findAll("p", {'class':"head-content__heading product-name"})
    item_name = item_name_container[0].text.strip()

    price_container = page_soup.findAll("span", {'class':"value"})
    price = price_container[0].text.strip()

    availability_container = page_soup.findAll("button", {'class':"add-to-cart btn multiline-cta btn-primary btn-block"})
    availability = availability_container[0].text.strip()

    if "reduced from" in price:
        price = price.replace("\t", "")
        reduced_container = page_soup.findAll("span", {'class':"sales"})
        reduced_price = reduced_container[0].text.strip()
        price = price + reduced_price
    
    if availability != 'SOLD OUT': 
        availability = 'IN STOCK'
        print("COMMENCE ALERT")

    email_func(item_name, price, availability, coach_url)
    print("Item: ", item_name)
    print("\nPrice: ", price)
    print("\nAvailability: ", availability)
    # f.write(item_name + "," + price + "," + availability)
    # f.close

# Always running every minute, if out of stock, sends email
def background_coach_scrape(coach_url):
    # Opening up connection, grabbing page
    uClient = urlopen(coach_url)
    page = uClient.read()
    uClient.close()
    page_soup = soup(page, "html.parser")

    item_name_container = page_soup.findAll("p", {'class':"head-content__heading product-name"})
    item_name = item_name_container[0].text.strip()

    price_container = page_soup.findAll("span", {'class':"value"})
    price = price_container[0].text.strip()

    availability_container = page_soup.findAll("button", {'class':"add-to-cart btn multiline-cta btn-primary btn-block"})
    availability = availability_container[0].text.strip()

    if "reduced from" in price:
        price = price.replace("\t", "")
        reduced_container = page_soup.findAll("span", {'class':"sales"})
        reduced_price = reduced_container[0].text.strip()
        price = price + reduced_price
    
    if availability != 'SOLD OUT': 
        availability = 'IN STOCK'
        print("COMMENCE ALERT")
        email_func(item_name, price, availability, coach_url)

    global coach_job_number    
    coach_job_number += 1

    print("\nItem: ", item_name)
    print("\nPrice: ", price)
    print("\nAvailability: ", availability)
    print("Job #:\t", coach_job_number)


# class FixFancyURLOpener(FancyURLopener):

#     def http_error_default(self, url, fp, errcode, errmsg, headers):
#         if errcode == 403:
#             raise ValueError("403")
#         return super(FixFancyURLOpener, self).http_error_default(
#             url, fp, errcode, errmsg, headers
#         )
# urllib.request.FancyURLopener = FixFancyURLOpener
# def background_converse_scrape(converse_url):
#     # Opening up connection, grabbing page
#     req = urllib.request.urlopen(converse_url)
#     with open("webscraper_scripts.py", "w") as fo:
#         fo.write(req.read())
#     req.close()
#     page_soup = soup(page, "html.parser")

#     item_name_container = page_soup.findAll("h1", {'class':"pdp-primary-information__product-name display--small-up"})
#     item_name = item_name_container[0].text.strip()

#     price_container = page_soup.findAll("span", {'class':"product-price--sales"})
#     price = price_container[0].text.strip()

#     availability_container = page_soup.findAll("p", {'class':"variations__notify-stock-title  text-color--cyan text--semibold"})
#     availability = availability_container[0].text.strip()
    
#     if availability != 'The product is sold out.': 
#         availability = 'IN STOCK'
#         print("COMMENCE ALERT")
#         email_func(item_name, price, availability, converse_url_lauren)

#     global converse_job_number    
#     converse_job_number += 1

#     print("\nItem: ", item_name)
#     print("\nPrice: ", price)
#     print("\nAvailability: ", availability)
#     print("Job #:\t", converse_job_number)

# Pure email function
def email_func(item_name, price, availability, link):
    CLAM_EMAIL_ADDRESS = os.environ.get('gmail_clam_user')
    CLAM_EMAIL_PASSWORD = os.environ.get('gmail_clam_pass')
    contacts = ["Insert email(s) here"] # Insert emails here
    
    msg = EmailMessage()
    msg['From'] = CLAM_EMAIL_ADDRESS
    msg['To'] = CLAM_EMAIL_ADDRESS # or substitute : [contact for contact in contacts]
    if availability == 'SOLD OUT':
        msg['Subject'] = f'PRODUCT - NOT AVAILABLE: {item_name}'
        msg.set_content(f'--Script still executing--\n\nItem: \t{item_name}\nPrice: \t{price}\nAvailability: \t{availability}\nLink: {link}')
    else:
        msg['Subject'] = f'PRODUCT IN STOCK/AVAILABLE: {item_name}'
        msg.set_content(f'PRODUCT IS IN STOCK \nORDER THIS ITEM NOW: \t{item_name}\nPrice: \t{price}\nAvailability: \t{availability}\nLink: {link}')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(CLAM_EMAIL_ADDRESS,CLAM_EMAIL_PASSWORD)
        smtp.send_message(msg)

