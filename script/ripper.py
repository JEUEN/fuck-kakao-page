import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import urllib
import urllib.request
from selenium.common.exceptions import NoSuchElementException

# 첫화 URL
URL = "https://sports.donga.com/cartoon?cid=0100000206&sid=2"

# 크롬 드라이버 셋업
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'D:\Utility\chromedriver\chromedriver.exe', options=options)
driver.implicitly_wait(time_to_wait=1)
driver.get(URL)
name = 'GM2'
# 몇화까지
ep_num = 182
img_num = 2

print("Before Loop")

# For Loop
for ep in range(0, ep_num):
    img = driver.find_element_by_xpath(r'//*[@id="contents"]/div[2]/div[1]/div[1]/div[2]/a/img') 
    src = img.get_attribute('src')
    urllib.request.urlretrieve(src, 'GM2_%03d.jpg'%(img_num))
    img_num = img_num + 1
    next_ep = driver.find_element_by_xpath(r'//*[@id="contents"]/div[2]/div[1]/div[1]/div[1]/div[2]/a[2]/img')
    next_ep.click()

print("Done!")