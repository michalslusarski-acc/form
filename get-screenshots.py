import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuration
output_folder = 'images'
input_file = 'data.csv'
wait_time = 4  # seconds to wait for page load

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Read URLs from the CSV file
urls = pd.read_csv(input_file)['url'].tolist()

# Set up Selenium WebDriver with headless Chrome
chrome_options = Options()
# chrome_options.add_argument('--headless')  # Run browser in headless mode
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1200,1080')  # Set window size for consistent screenshots

driver = webdriver.Chrome(options=chrome_options)

# Process each URL
for index, url in enumerate(urls, start=1):
    try:
        print(f'Processing {index}/{len(urls)}: {url}')
        driver.get(url)
        time.sleep(wait_time)  # Wait for the page to load

        screenshot_path = os.path.join(output_folder, f'{index}.jpg')

        driver.save_screenshot(screenshot_path)
        print(f'Screenshot saved to {screenshot_path}')
    except Exception as e:
        print(f'Error processing {url}: {e}')

# Clean up
driver.quit()
print('All done!')
