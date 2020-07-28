from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

chromedriver_path = r'D:\chrome\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
sleep(1)
username.send_keys('your_user_name')
password = webdriver.find_element_by_name('password')
sleep(1)
password.send_keys('your_password')


button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(5)

webdriver.get('https://www.instagram.com/your_user_name/')

sleep(5)
link=webdriver.find_element_by_partial_link_text("following")
link.click()
sleep(2)
unfollowed=0

for x in range(1,200):
    try:
        if webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[3]/button'.format(x)).text == 'Following':
            webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[3]/button'.format(x)).click()
            sleep(2)
            webdriver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click()
            unfollowed = unfollowed + 1
            sleep(4)
    except Exception as e:
        print(e)
        continue

print("people unfollowed=",unfollowed)