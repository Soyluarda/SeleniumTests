from selenium import webdriver
driver= webdriver.Chrome()
driver.get("http://www.Amazon.com")
driver.find_element_by_id("twotabsearchtextbox").send_keys("samsung")
driver.find_element_by_class_name("nav-input").click()
driver.close()