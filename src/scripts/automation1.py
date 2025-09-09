from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Firefox
options = Options()  # No headless
service = Service("/opt/homebrew/bin/geckodriver")
driver = webdriver.Firefox(service=service, options=options)

# Open file for writing
with open("results.txt", "w") as file:
    # Header (optional, can be removed for pure HTML output)
    # file.write("Question Number\tResult URL\n")

    # Loop from Question 1 to 988
    for q_num in range(988, 989):
        query = f"AWS CERTIFIED CLOUD PRACTITIONER Topic 1 Question {q_num} discussions site:examtopics.com"
        print(f"\n🔍 Searching for Question #{q_num}")
        driver.get(f"https://www.bing.com/search?q={query}")

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'li.b_algo h2 a'))
            )
            result_link = driver.find_elements(By.CSS_SELECTOR, 'li.b_algo h2 a')[0].get_attribute('href')
            print(f"✅ Found: {result_link}")
            file.write(f"'{result_link}',\n")
        except Exception as e:
            print(f"❌ No result for Question #{q_num}")
            file.write(f"'',\n")

        time.sleep(1)  # Be polite to Bing

# Close browser
driver.quit()
print("\n📁 Results saved to results.txt")
