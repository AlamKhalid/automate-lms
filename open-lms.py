from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://lms.nust.edu.pk/portal/')

# Accessing the fields by their ids and sending the values to them
elem = driver.find_element_by_id('login_username')
elem.send_keys('')   # Enter your username here
elem = driver.find_element_by_id('login_password')
elem.send_keys('')   # Enter your password here
elem.send_keys(Keys.RETURN)     # This is used to press Enter after entering credentials

# This opens up all the courses in new tab using their URL after logging in
driver.execute_script('''window.open("https://lms.nust.edu.pk/portal/course/view.php?id=29983","_blank");''')
driver.execute_script('''window.open("https://lms.nust.edu.pk/portal/course/view.php?id=29981","_blank");''')
driver.execute_script('''window.open("https://lms.nust.edu.pk/portal/course/view.php?id=29979","_blank");''')
driver.execute_script('''window.open("https://lms.nust.edu.pk/portal/course/view.php?id=29977","_blank");''')
driver.execute_script('''window.open("https://lms.nust.edu.pk/portal/course/view.php?id=29975","_blank");''')

