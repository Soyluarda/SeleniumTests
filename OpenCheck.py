from selenium import webdriver
driver= webdriver.Chrome()
driver.get("http://www.Amazon.com")
print (driver.title)
driver.close()