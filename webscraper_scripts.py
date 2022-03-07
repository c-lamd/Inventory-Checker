from inventory_scraper_module import background_coach_scrape, coach_scrape, pink_heart_purse_url, converse_url_lauren
import time
import schedule
import os
from schedule import every, repeat, run_pending

print("Starting scraper_scripts.py")
background_coach_scrape(pink_heart_purse_url)
# Real time check
schedule.every(1).minutes.do(background_coach_scrape, pink_heart_purse_url)
# Updates every 3 hours from 9:00AM to 12:00AM
schedule.every().day.at('09:00').do(coach_scrape, pink_heart_purse_url)
schedule.every().day.at('12:00').do(coach_scrape, pink_heart_purse_url)
schedule.every().day.at('15:00').do(coach_scrape, pink_heart_purse_url)
schedule.every().day.at('18:00').do(coach_scrape, pink_heart_purse_url)
schedule.every().day.at('21:00').do(coach_scrape, pink_heart_purse_url)
schedule.every().day.at('00:00').do(coach_scrape, pink_heart_purse_url)


while True:
    run_pending()  
    schedule.run_pending()
    time.sleep(1)