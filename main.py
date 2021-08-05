from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())

link = 'https://github.com/httpanand/Youtube-Video-Downloader-JS' #Change this link to your link !
driver.get(link)


element = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[2]/div[1]/div[1]/span/get-repo/details/summary").click()
element = driver.find_element_by_xpath("/html/body/div[4]/div/main/div[2]/div/div/div[2]/div[1]/div[1]/span/get-repo/details/div/div/div[1]/ul/li[2]/a").click()

