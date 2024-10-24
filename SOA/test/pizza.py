from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path to your ChromeDriver executable
chromedriver_path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'

# Create a new Chrome webdriver instance
driver = webdriver.Chrome()

# Navigate to the Domino's website
driver.get('https://www.dominos.co.uk/store/horsham/menu')

# Find the search inp
#find the specific pizza you want to order and click on it
pizza_tile = driver.find_element(By.XPATH, '//div[@class="base-menu-card__title-container"]/h3[contains(text(), "Mighty Meaty")]')
pizza_tile.click()

#work around the problem of adding to cart by customizing as it is a clickabble
#customize_button = driver.find_element(By.XPATH, '//button[contains(text(), "CUSTOMIZE")]')
#customize_button.click()
# Add the pizza to your cart (assuming there's an 'Add to Cart' button)
add_to_cart_button = driver.find_element(By.XPATH, '//button[contains(text(), "ADD TO BASKET")]')
add_to_cart_button.click()

# Proceed to checkout (assuming there's a 'Checkout' button)
checkout_button = driver.find_element(By.XPATH, '//button[contains(text(), "BASKET")]')
checkout_button.click()

# At this point, you may need to fill in additional information, such as your address, payment details, etc.
# You would need to inspect the website's HTML structure and use appropriate Selenium methods to interact with the elements.

# Once you've filled in all the necessary information, you can proceed with the checkout process.

# Keep the browser open for interaction
input("Press Enter to exit...")

# Finally, close the webdriver
driver.quit()
