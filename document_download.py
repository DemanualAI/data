import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from undetected_chromedriver import Chrome, ChromeOptions

driver = Chrome()

# Maximizing the Window Size 
driver.maximize_window()

with open("final_cleaned_SC.json", "r") as file:
    data = json.load(file)

# Hardcoded year value
year = 2000

# Get links for the specified year
links = data.get(str(year), [])

# Loop through the links for the specified year
for link in links:
    try:
        driver.get(link)
        # #pdfdoc
        # Wait for the download PDF button to be clickable
        download_pdf_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "pdfdoc"))
        )
        
        # Click the download PDF button
        download_pdf_button.click()
        time.sleep(1.5)  # Adjust the sleep time as needed
    except Exception as e:
        time.sleep(5)
        print("Error:", e)
        # If encountered an error, try refreshing the page and then proceed
        driver.refresh()
        time.sleep(3)

time.sleep(10)
driver.quit()