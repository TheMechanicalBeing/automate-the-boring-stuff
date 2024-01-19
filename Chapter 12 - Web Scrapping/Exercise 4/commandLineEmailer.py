import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("Usage: python commandLineEmailer.py <email> *<text>")
        sys.exit()

    print("Getting recipent and text data")

    email_to_send = sys.argv[1]
    text_to_send = " ".join(sys.argv[2:])

    my_email = "tornike.tsulukidze.1@btu.edu.ge"
    my_password = os.environ.get("Pass")

    with webdriver.Chrome() as browser:
        print("Opening the Chrome")

        browser.get("https://mail.google.com")
        browser.maximize_window()

        print("Logging to email")

        input_email_element = browser.find_element(By.XPATH, "//input[@type='email']")
        input_email_element.send_keys(my_email)
        input_email_element.send_keys(Keys.RETURN)

        time.sleep(7)

        input_password_element = browser.find_element(By.XPATH, "//input[@type='password']")
        input_password_element.send_keys(my_password)
        input_password_element.send_keys(Keys.RETURN)

        time.sleep(10)
        print("Sending message")

        browser.implicitly_wait(5)
        compose_element = browser.find_element(By.XPATH, "//div[text()='Compose']")
        compose_element.click()

        time.sleep(3)

        recipent_element = browser.find_element(By.CLASS_NAME, "agP")
        recipent_element.send_keys(email_to_send)
        recipent_element.send_keys(Keys.RETURN)

        time.sleep(3)

        textbox_element = browser.find_element(By.XPATH, "//div[@role='textbox']")
        textbox_element.send_keys(text_to_send)

        time.sleep(5)

        send_button = browser.find_element(By.XPATH, "//div[text()='Send']")
        send_button.click()

        time.sleep(10)

    print("Message sent successfully")
