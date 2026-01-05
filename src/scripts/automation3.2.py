import time
import random
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Topics dictionary
# AZ-305
# topics = {
#     1: 71,
#     2: 42,
#     3: 81,
#     4: 82,
#     5: 52,
#     6: 2,
#     7: 23,
#     8: 12,
#     9: 2,
#     10: 2,
#     11: 1,
#     12: 1,
#     13: 1,
#     14: 4,
#     15: 3,
# }

# AI-102
topics = {
    1: 71, 2: 42, 3: 81, 4: 33, 5: 52, 6: 2, 7: 23, 8: 12, 9: 2, 10: 2, 11: 1, 12: 1, 13: 1, 14: 4, 15: 3, 
}

# GCP-CDL
# topics = {
#     1 : 326,
# }

# GCP-GAI
# topics = {
#     1 : 33, 2: 28, 3: 6, 4: 8, 
# }

# AIF-C01 
# topics = {
#     1 : 334,
# }

# N10-009
# topics = {
#     1 : 472,
# }

# CLF-C02
# topics = {
#     1 : 988,
# }

# START_QUESTION = 685
# END_QUESTION = 988

# Setup Firefox (with anti-bot tweaks)
options = Options()
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)
options.set_preference(
    "general.useragent.override",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:115.0) Gecko/20100101 Firefox/115.0"
)

service = Service("/opt/homebrew/bin/geckodriver")  # Adjust path if needed
driver = webdriver.Firefox(service=service, options=options)

# Open output file
with open("results1.txt", "w") as file:
    for topic, max_qn in topics.items():
        for q_num in range(1, max_qn + 1):
            query = f"AExam AI-102 topic {topic} question {q_num} discussion"
            print(f"\n🔍 Searching: Topic {topic} - Question {q_num}")
            driver.get(f"https://duckduckgo.com/?q={query}")

            try:
                # Wait for at least one DuckDuckGo result
                WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="result-title-a"]'))
                )

                # Get first result link
                first_result = driver.find_elements(By.CSS_SELECTOR, 'a[data-testid="result-title-a"]')[0]
                result_link = first_result.get_attribute("href")

                print(f"✅ Found: {result_link}")
                file.write(f"'{result_link}',\n")

            except Exception:
                print(f"❌ No result for Topic {topic} - Question {q_num}")
                file.write("'',\n")

            # Small random delay to mimic human behavior
            time.sleep(random.uniform(1, 2))

# Cleanup
driver.quit()
print("\n📁 Results saved to results.txt")

