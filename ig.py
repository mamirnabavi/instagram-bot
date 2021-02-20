from selenium import webdriver
from time import sleep

username="candooo.ir"
password="Yasahebazaman313"
driver = webdriver.Chrome('chromedriver.exe')

driver.get("https://www.instagram.com/")
sleep(3)

driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_key(username)
sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_key(password)
sleep(1)
driver.find_elements_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button").click()


if driver.find_element_by_id(""):
    print("username or password is not valid.")
else:
    print("login successful.")
