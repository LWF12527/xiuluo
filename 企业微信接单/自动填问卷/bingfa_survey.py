import random
import time
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def fill_survey_xs():
    # Set up the Chrome driver
    driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    # Load the webpage
    driver.get("https://www.wjx.cn/vm/m9ZYoRT.aspx")

    # Wait for the page to load and the question list to be available
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fieldset1 .field")))

    # Randomly select answers for each question
    for i in range(1, 12):
        options = driver.find_elements(By.CSS_SELECTOR, f"#fieldset1 .field[topic='{i}'] .ui-radio")
        if i == 11:  # Check if it's the last question
            checkboxes = driver.find_elements(By.CSS_SELECTOR, f"#fieldset1 .field[topic='{i}'] .ui-checkbox")
            random.shuffle(checkboxes)  # Randomize the order of checkboxes
            for j in range(random.randint(1, len(checkboxes))):  # Randomly select 1 to all checkboxes
                checkboxes[j].click()
        else:
            random_option = random.choice(options)
            random_option.click()

    # Submit the form
    submit_button = driver.find_element(By.ID, "ctlNext")
    submit_button.click()

    # Close the browser
    driver.quit()


def fill_survey_js():
    # Set up the Chrome driver
    driver = webdriver.Chrome("C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    # Load the webpage
    driver.get("https://www.wjx.cn/vm/eIs1VIQ.aspx#")

    # Wait for the page to load
    wait = WebDriverWait(driver, 3)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fieldset1 .field")))

    # Randomly select answers for each question
    for i in range(1, 16):
        if i == 1 or i == 2 or i == 15:  # Check if it's a multiple-choice question (1, 2, or 15)
            checkboxes = driver.find_elements(By.CSS_SELECTOR, f"#fieldset1 .field[topic='{i}'] .ui-checkbox")
            if checkboxes:  # Check if checkboxes exist
                random.shuffle(checkboxes)  # Randomize the order of checkboxes
                for j in range(random.randint(1, len(checkboxes))):  # Randomly select 1 to all checkboxes
                    checkboxes[j].click()
        else:  # Single-choice question
            options = driver.find_elements(By.CSS_SELECTOR, f"#fieldset1 .field[topic='{i}'] .ui-radio")
            if options:  # Check if options exist
                random_option = random.choice(options)
                random_option.click()

    # Submit the form
    submit_button = driver.find_element(By.ID, "ctlNext")
    submit_button.click()

# 运用并发技术，一次提交5个为一组，共60组，一共300份问卷
if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=5) as executor:
        for _ in range(60):  # Run 60 groups of 5 surveys
            for _ in range(5):  # Submit 5 surveys concurrently
                executor.submit(fill_survey_js)
                executor.submit(fill_survey_xs)
            # time.sleep(5)  # Pause for 5 seconds before submitting the next group
