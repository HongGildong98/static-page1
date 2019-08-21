from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#naver = "https://shopping.naver.com/"
#danawa = "http://www.danawa.com/"
#daum = "https://shopping.daum.net/"

naver = "https://shopping.naver.com/"
danawa = "http://www.danawa.com/"
daum = "https://shoppinghow.kakao.com/"


shopping_site = [naver,danawa,daum]

"""
def search(tap,site):
    tap.maximize_window()
    tap.get(site)
    web = tap.find_element_by_name("query")
    web.send_keys("test")
    wait = WebDriverWait(tap, 10)
    btn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div[1]/form/fieldset/div[1]/a[2]')))
    tap.execute_script("arguments[0].scrollIntoView()", btn)
    btn.click()
    
    #tap.submit()
"""    

def search_naver(tap,site,search_word):
    tap.maximize_window()
    in_ = site.split("&")
    in_[0] = in_[0]+search_word
    final = ""
    for i in range(len(in_)-1):
        final = final+in_[i]+"&"
    final = final+in_[-1]
    tap.get(final)

def search_danawa(tap,site,search_word):
    tap.maximize_window()
    web = tap.find_element_by_name("k1")
    web.sendkeys(search_word)
    web.find_element_by_class_name("btn_search_submit").click()
    
def search_daum(tap,site,search_word):
    tap.maximize_window()
    site +=search_word
    tap.get(site)

def search(tap,site,search_word):
    tap.maximize_window()
    tap.get(site)
    web=""
    if(site == naver):
        web = tap.find_element_by_name("query")
        web.send_keys(search_word)
        #btn = tap.find_element_by_css_selector("co_srh_btn_searchN=a:SNB.search")
        element = tap.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/div[2]/div/div[1]/form/fieldset/div[1]/a[2]")
        tap.execute_script("arguments[0].click();", element)

        
        #web.find_element_by_class_name("co_srh_btn _search N=a:SNB.search").click()
    elif(site==danawa):
        web = tap.find_element_by_name("k1")
        web.send_keys(search_word)
        time.sleep(1)
        web.submit()

        #web.find_element_by_class_name("btn_search_submit").click()
    elif(site==daum):
        web = tap.find_element_by_name("q")
        web.send_keys(search_word)
        time.sleep(1)
        web.submit()
        #web.find_element_by_class_name("ico_comm5 ico_srch").click()

browser = []
for item in shopping_site:
    browser.append(webdriver.Firefox())
    search(browser[-1],item,"세제")


