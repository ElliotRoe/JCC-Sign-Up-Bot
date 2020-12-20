import sys
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
from datetime import timedelta
from datetime import datetime

try:
    classHour = int(sys.argv[1])
except:
    print("Please make sure the hour parameter is an integer")
    classHour = 8

#try:
targetDate = datetime.strptime(sys.argv[2], '%m/%d/%y')
#except:
    #print("An error occured with the date format. Please make sure it is in the format: m/d/y")
    #targetDate = date.today()

display = Display(visible=0, size=(1366, 768))
display.start()
print("Display started")

option = webdriver.ChromeOptions()
#Removes navigator.webdriver flag
option.add_argument('--disable-blink-features=AutomationControlled')

browser = webdriver.Chrome(executable_path='/usr/lib/chromium-browser/chromedriver',options=option)
print("Browser created")

userStr = 'elliotbroe@gmail.com'
passStr = 'hello!-w0Rld'

userFieldId = 'su1UserName'
passFieldId = 'su1Password'
signInId = 'btnSu1Login'

browser.get(('https://columbusjcc.org/reservations/'))
print("Reservation site visited")

mindLink = browser.find_elements_by_partial_link_text('Fitness Floor')
mindLink[0].click()

WebDriverWait(browser, 20).until(EC.number_of_windows_to_be(2))

newWindow = browser.window_handles
newNewWindow = newWindow[1]
browser.switch_to.window(newNewWindow)

username = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, userFieldId)))
username.send_keys(userStr)

password = browser.find_element_by_id(passFieldId)
password.send_keys(passStr)

signin = browser.find_element_by_id(signInId)
signin.click()
print("Logged in")

signInCheckId = 'top-wel-sp'
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, signInCheckId)))

classBaseURL = "https://clients.mindbodyonline.com/ASP/res_a.asp?"
params = {}
params['classId'] = str(1792 + (classHour - 6) * 5)

params['classDate'] = targetDate.strftime("%m/%d/%y")

classURL = classBaseURL
for param in params:
    classURL = classURL + param + '=' + params[param] + '&'

browser.get((classURL))
print("Class page visited")

registerId = 'SubmitEnroll2'

registerButton = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, registerId)))
registerButton.click()
print("Registered!")

browser.quit()

display.stop()
print("Browser and display stopped")