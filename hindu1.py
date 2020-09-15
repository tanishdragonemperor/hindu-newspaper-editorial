from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
import time
import schedule

def setting_time():
    
    PATH="C:\Program Files (x86)\chromedriver.exe"
    # driver=webdriver.Chrome(PATH)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', options=options) 
    driver.get("https://iasbano.com/upsc_thehindu_free_download.php")
    driver.maximize_window()
# driver.implicitly_wait(10) 
    search=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/a');
    search.click()
    download_dir = "D:\chll thiq" 



    profile = {"plugins.plugins_list": [{"enabled": False, "name": "Chrome PDF Viewer"}], # Disable Chrome's PDF Viewer
               "download.default_directory": download_dir , "download.extensions_to_open": "applications/pdf"}
    options.add_experimental_option("prefs", profile)
# driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe', chrome_options=options) 
 # Optional argument, if not specified will search path.
    pdf_url=driver.current_url
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("sender id","password")
    message="Your todays link is    \n"+pdf_url
    s.sendmail("sender id","receiver id",message)


schedule.every().day.at("07:00").do(setting_time)
while True:
    schedule.run_pending()
    time.sleep(1)