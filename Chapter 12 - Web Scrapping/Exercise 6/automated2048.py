# The program DOES NOT work
# I think the reason is that website uses anti-automation tools

import time
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


if __name__ == "__main__":

    computer_inputs = (Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT)

    with webdriver.Chrome() as browser:
        browser.get("https://play2048.co/")

        body = browser.find_element(By.CLASS_NAME, "body")

        # Simulate arrow key presses
        for _ in range(200):
            body.send_keys(random.choice(computer_inputs))
            time.sleep(0.1)
