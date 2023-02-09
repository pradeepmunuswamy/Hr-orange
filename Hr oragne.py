from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up the webdriver
driver = webdriver.Firefox()

# Navigate to the website
driver.get("https://opensource-demo.orangehrmlive.com/")

# Find the username and password fields and enter the creds
username = driver.find_element_by_id("txtUsername")
password = driver.find_element_by_id("txtPassword")
username.send_keys("Admin")
password.send_keys("admin123")

# Submit the form
driver.find_element_by_id("btnLogin").click()

# Navigate to the PIM section and create a new employee
driver.find_element_by_id("menu_pim_viewPimModule").click()
driver.find_element_by_id("menu_pim_addEmployee").click()

# Navigate to the Admin section and add a new user
driver.find_element_by_id("menu_admin_viewAdminModule").click()
driver.find_element_by_id("menu_admin_UserManagement").click()
driver.find_element_by_id("btnAdd").click()

# Close the webdriver
driver.quit()





