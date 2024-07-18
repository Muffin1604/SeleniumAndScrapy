from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

def selenium1():
    try:
        # URL to scrape
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
        url = 'https://www.saucedemo.com/'
        driver.get(url)
        driver.implicitly_wait(5)
        driver.maximize_window()

        # Explicit wait for the username field to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'user-name'))
        )
        # Login to the site
        username_element = driver.find_element(By.ID, 'user-name')
        username_element.send_keys('visual_user')

        password_element = driver.find_element(By.ID, 'password')
        password_element.send_keys('secret_sauce')
        password_element.send_keys(Keys.RETURN)
        
        add_cart = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        add_cart.click()
        
        cart = driver.find_element(By.ID, 'shopping_cart_container')
        cart.click()

        
        continue_shopping = driver.find_element(By.ID, 'continue-shopping')
        continue_shopping.click()
        
        remove_cart = driver.find_element(By.ID, 'remove-sauce-labs-backpack')
        remove_cart.click()
        

        # Open the menu and log out
        side_menu = driver.find_element(By.ID, 'react-burger-menu-btn')
        side_menu.click()
        

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'logout_sidebar_link'))
        )
        logout_btn = driver.find_element(By.ID, 'logout_sidebar_link')
        logout_btn.click()

        # Give some time for logout to complete
        print('"Script Run Successfully"')

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the WebDriver
        driver.quit()
# webdriver
# driver = webdriver.Chrome()
# options
# options.headless =True