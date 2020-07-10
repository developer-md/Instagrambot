from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

chromedriver_path = r'D:\chrome\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(5)

username = webdriver.find_element_by_name('username')
sleep(2)
#put your username
username.send_keys('your_username')
password = webdriver.find_element_by_name('password')
sleep(2)
#put your password
password.send_keys('your_password')


button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button')
button_login.click()
sleep(8)

#change hashtags on the basis of your posts, any number of hashtags
hashtag_list = ['suggestions','goodmornig','instadaily','instagram','instaphoto']


tag = -1
followed = 0
likes=0
comments=0
comment=["nice:)","awesome","perfect","good one","so cool:)","Really cool!"]

for hashtag in hashtag_list:
    tag += 1
    webdriver.get('https://www.instagram.com/explore/tags/'+ hashtag_list[tag] + '/')
    sleep(6)
    first_thumbnail = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a').click()
    
    sleep(5)    
    try:        
        for x in range(1,200):#(1,200) It means people followed=approx(no. of hashtag X 200)
            if webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
                    
                webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
                followed += 1
                sleep(2)

                #like
                webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button').click()
                likes += 1
                sleep(1)

                #comment
                webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[2]/button').click()
                comment_box=webdriver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
                comment_box.send_keys(random.choice(comment))
                sleep(1)
                comment_box.send_keys(Keys.ENTER)
                comments += 1
                sleep(4)


                # Next picture
                webdriver.find_element_by_link_text('Next').click()
                sleep(5)
            else:
                webdriver.find_element_by_link_text('Next').click()
                sleep(5)

    except Exception as e:
        print(e)
        continue

print('Liked {} photos.'.format(likes))
print('Commented {} photos.'.format(comments))
print('Followed {} new people.'.format(followed))