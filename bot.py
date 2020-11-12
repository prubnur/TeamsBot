from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime, timedelta
from threading import Timer

from selenium.webdriver.support.wait import WebDriverWait

def joinmeeting(url, duration, teamsid, teamspass):
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1,
        "profile.default_content_setting_values.notifications": 1
    })

    driver = webdriver.Chrome(options=opt,
                              executable_path=r"C:\\Users\\isaluja1811\\PycharmProjects\\TeamsBot\\drivers\\chromedriver.exe")

    driver.set_page_load_timeout(10)

    #driver.get("https://teams.microsoft.com/_#/pre-join-calling/19:349461a7e103475a880deda07875ecdc@thread.tacv2") # DON'T CHANGE THIS LINK
    driver.get(url)
    time.sleep(2)
    driver.find_element_by_name("loginfmt").send_keys(teamsid)
    driver.find_element_by_name("loginfmt").send_keys(Keys.ENTER)
    driver.find_element_by_id("i0118").send_keys(teamspass)
    time.sleep(1)
    driver.find_element_by_id("i0118").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_id("idSIButton9").click()
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Use the web app instead')]")))

    try:
        driver.find_element_by_xpath("//*[contains(text(), 'Use the web app instead')]").click()
        time.sleep(6)
    except:
        print("No prompt")

    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Join')]")))
    driver.find_element_by_xpath("//*[contains(text(), 'Join')]").click()
    time.sleep(3)
    #driver.find_element_by_class_name("ts-toggle-button-container").click()
    try:
        #driver.find_element_by_xpath("//*[contains(text(), 'Turn camera off')]").click()
        #driver.find_element_by_name("Turn camera off").click()
        driver.find_element_by_xpath("//toggle-button[@title='Turn camera off']").click()
    except:
        print("Camera already off")
    time.sleep(2)
    #driver.find_element_by_id("preJoinAudioButton").click()
    try:
        #driver.find_element_by_xpath("//*[contains(text(), 'Mute microphone')]").click()
        driver.find_element_by_xpath("//toggle-button[@title='Mute microphone']").click()
    except:
        print("Mic already muted")
    time.sleep(2)
    # driver.find_element_by_class_name("join-btn ts-btn inset-border ts-btn-primary").click()
    driver.find_element_by_xpath("//*[contains(text(), 'Join now')]").click()
    time.sleep(duration)

    # driver.find_element_by_name("q").send_keys("Automation step by step")
    # driver.find_element_by_name("q").send_keys(Keys.ENTER)
    # driver.quit()
userid = ""
password = ""

if not (userid and password):
    userid = input("Enter your teams ID: ")
    password = input("Enter your teams password: ")

x=datetime.today()
y = x.replace(day=x.day, hour=8, minute=32, second=0, microsecond=0) + timedelta(days=1)
delta_t=y-x

secs=delta_t.total_seconds()
print(secs)

# Add the link to your meeting here
link = "https://teams.microsoft.com/_#/scheduling-form/?eventId=AAMkADQ0ZTFlZDEwLTVjNjAtNDFiNC1hZWY0LWNmYTYzNWJkYzgwYgBGAAAAAAAl3-u4iCSXQox5DMp39596BwDv7rJnnEaDSakCp-2zZ26IAAAAAAENAADv7rJnnEaDSakCp-2zZ26IAAAzzDqAAAA%3D&conversationId=19:7a04fe22e9364e77a601e575bf596edc@thread.tacv2&opener=0&providerType=1&navCtx=channel"

# Add the Duration of your meeting in seconds
dur = 5400

t = Timer(secs, joinmeeting, [link, dur, userid, password])
t.start()