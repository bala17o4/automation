from logging import Manager
from os import name
from flask import *
from helium import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller as chromedriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)


@app.route('/focus', methods=['POST','GET'])
def whatsapp_web():
    if request.method=='POST':
        data = request.form
        brow=request.form.get('browser')
        if(brow=='chrome'):
            c_options = Options()
            c_options.add_experimental_option("detach",True)
            c_options.add_argument("start-maximized")
            c_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            c_options.add_experimental_option('excludeSwitches', ['enable-logging'])
            c_options.add_experimental_option('useAutomationExtension', False)
            c_options.add_argument('--disable-blink-features=AutomationControlled')
            s=Service(chromedriver.install())
            driver = start_chrome(request.form.get('link'),options=c_options)
            time.sleep(10)
            try:
                click('sign in')
            except LookupError:
                try:
                    click('log in')
                except LookupError:
                    pass


            # driver = webdriver.Chrome(service=s, chrome_options=c_options)
            # driver.maximize_window()
            # driver.get(request.form.get('link'))
            # textDemo = driver.find_element("xpath","// a[contains(text(),\'sign')]").click()
            # search_text = "signin"
            # source = driver.page_source
            # if(search_text in source):
            #     search_text.click()
            #     print("true")

            # else:
            #     print("false")
            
        if(brow=='firefox'):
            s=Service(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=s)
            driver.maximize_window()
            driver.get("https://web.whatsapp.com/")
        return render_template('submit.html',result = data)



@app.route('/')
def intro():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)










