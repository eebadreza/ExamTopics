from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Topic and question mapping
# AZ-104
# topics = {
#     1: 40,
#     2: 39,
#     3: 98,
#     4: 121,
#     5: 150,
#     6: 63,
#     7: 2,
#     8: 2,
#     9: 2,
#     10: 3,
#     11: 3,
#     12: 1,
#     13: 2,
#     14: 2,
#     15: 1,
#     16: 1
# }

# AZ-400
# topics = {
#     1: 31,
#     2: 45,
#     3: 35,
#     4: 74,
#     5: 44,
#     6: 55,
#     7: 90,
#     8: 77,
#     9: 62,
#     10: 3,
#     11: 1,
#     12: 3,
#     13: 3,
#     14: 3,
#     15: 2,
#     16: 1,
#     17: 5,
#     18: 5,
# }

# AZ-500
topics = {
    1: 42,
    2: 123,
    3: 69,
    4: 125,
    5: 75,
    6: 31,
    7: 14,
    8: 3,
    9: 3,
    10: 2,
    11: 4,
    12: 3,
    13: 5,
    15: 1,
    16: 1
}

# AZ-700
# topics = {
#     1: 52,
#     2: 101,
#     3: 74,
#     4: 70,
#     5: 38,
#     6: 1,
#     7: 3,
#     8: 1,
#     9: 3,
#     10: 2
# }

# Setup Firefox
options = Options()  # No headless mode
service = Service("/opt/homebrew/bin/geckodriver")  # Update path if needed
driver = webdriver.Firefox(service=service, options=options)

# Open output file
with open("results.txt", "w") as file:
    for topic, max_qn in topics.items():
        for q_num in range(1, max_qn + 1):
            query = f"AZ-500 topic {topic} Question {q_num} discussion site:examtopics.com"
            print(f"\n🔍 Searching: Topic {topic} - Question {q_num}")
            driver.get(f"https://www.bing.com/search?q={query}")

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'li.b_algo h2 a'))
                )
                result_link = driver.find_elements(By.CSS_SELECTOR, 'li.b_algo h2 a')[0].get_attribute('href')
                print(f"✅ Found: {result_link}")
                file.write(f"'{result_link}',\n")
            except Exception:
                print(f"❌ No result for Topic {topic} - Question {q_num}")
                file.write(f"'',\n")

            time.sleep(1)  # Avoid hitting Bing too quickly

# Cleanup
driver.quit()
print("\n📁 Results saved to results.txt")
