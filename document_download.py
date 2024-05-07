import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# Initialize Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

with open("final_cleaned_SC.json", "r") as file:
    data = json.load(file)

# Hardcoded year value
years = [
    1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984,
    1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994,
    1995, 1996, 1997, 1998, 1999, 2002, 2004, 2005, 2006, 2007, 
    2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 
    2018, 2019, 2020, 2021, 2022, 2023, 2024
]

for year in years:
    # Get links for the specified year
    links = data.get(str(year), [])

    count = 0 

    # Loop through the links for the specified year
    for link in links:
        try:
            driver.get(link)
            # Wait for the download PDF button to be clickable
            download_pdf_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "pdfdoc"))
            )
            
            # Click the download PDF button
            download_pdf_button.click()
            count += 1
            print(count)
            time.sleep(2)  # Adjust the sleep time as needed
        except Exception as e:
            time.sleep(5)
            print("Error:", e)
            # If encountered an error, try refreshing the page and then proceed
            driver.refresh()
            time.sleep(3)

    time.sleep(10)

# Close the browser window
driver.quit()
