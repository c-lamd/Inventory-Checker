from selenium import webdriver as wd
import chromedriver_binary
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

wd = wd.Chrome()
# wd.get("https://www.coachoutlet.com/products/heart-crossbody-in-colorblock/C6952-IMP1X.html?frp=C6952%20IMP1X&isSPC=true")
wd.get("https://www.coachoutlet.com/products/jes-crossbody-in-signature-canvas-with-heart-petal-print/C7617-IMBMC.html?frp=C7617%20IMBMC")
wd.implicitly_wait(5)


try:
    exit_coach_insider_popup = wd.find_element(By.XPATH, "/html/body/div[11]/div[3]/div/div/div/a")
    exit_coach_insider_popup.click()
except:
    print("no popup")

add_to_bag = wd.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/div[3]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/button")
add_to_bag.click()

checkout = wd.find_element(By.XPATH, "/html/body/div[2]/header/div[2]/div[1]/div/div[3]/div[3]/div/div[2]/div/div/div/div[3]/div[1]/div/div[2]/a")
checkout.click()

first_name = wd.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/div/form/div[1]/fieldset/div/div/div[4]/div[1]/input")
type(first_name)
first_name.send_keys("Connor")

last_name = wd.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/div/form/div[1]/fieldset/div/div/div[4]/div[2]/input")
type(last_name)
last_name.send_keys("Lam")

address = wd.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/div/form/div[1]/fieldset/div/div/div[5]/div[1]/input")
type(address)
address.send_keys("Address Here")

apt_num = wd.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/div/form/div[1]/fieldset/div/div/div[5]/div[2]/input")
type(apt_num)
apt_num.send_keys("Apartment Number here")

city = wd.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/div/form/div[1]/fieldset/div/div/div[5]/div[3]/div[1]/input")
type(city)
city.send_keys("City Here")

zip_code = wd.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/div/form/div[1]/fieldset/div/div/div[5]/div[3]/div[3]/input")
type(zip_code)
zip_code.send_keys("Zip Code here")

state = wd.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/div/form/div[1]/fieldset/div/div/div[5]/div[3]/div[2]/select")
drop = Select(state)
drop.select_by_visible_text("State Here")


email = wd.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/div/form/div[3]/div[1]/div/div[1]/input")
type(email)
email.send_keys("Email Address here")

phone_num = wd.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[3]/div[2]/div[1]/div/div[2]/div/div/form/div[3]/div[1]/div/div[2]/input")
type(phone_num)
phone_num.send_keys("Phone number here")

continue_to_payment = wd.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[3]/div[7]/div[1]/div[2]/button[1]")
continue_to_payment.click()

card_number = wd.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div/div[1]/div[3]/div[4]/div[3]/form/fieldset[1]/div[1]/div/div[6]/fieldset/fieldset/div/div/div/div[2]/div/div[1]/label/span[2]")

type(card_number)
card_number.send_keys("Card information here")

time.sleep(1000)