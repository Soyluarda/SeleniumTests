from selenium import webdriver
driver= webdriver.Chrome()
driver.get("http://www.Amazon.com")
driver.find_element_by_id("nav-link-accountList").click()
driver.find_element_by_name("email").send_keys("uyegirisi")
driver.find_element_by_name("password").send_keys("sifre")
driver.close()