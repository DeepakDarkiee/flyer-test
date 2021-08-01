import requests
# import webbrowser
# import urllib.request
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.chrome import ChromeDriverManager


# def redirect_url():
#   url = "http://127.0.0.1:8000/"

#   # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#   driver = webdriver.Chrome(ChromeDriverManager().install())
#   driver.get(url)

#   u = driver.find_element_by_name('username')
#   u.send_keys('deep')
#   p = driver.find_element_by_name('password')
#   p.send_keys('Deepak@7415@')
#   p.send_keys(Keys.RETURN)
  



def redirect_url():
  url = "http://127.0.0.1:8000/"
  client = requests.session()
  client.get(url)
  if 'csrftoken' in client.cookies:
    # Django 1.6 and up
    csrftoken = client.cookies['csrftoken']
    print(csrftoken)
  else:
    # older versions
    csrftoken = client.cookies['csrf']
    # print(csrftoken)

  data = {'username':'deep','password':'Deepak@7415@','csrfmiddlewaretoken':csrftoken}

  # session = requests.Session()
  # r = session.post(url, data=data)
  login_data = dict(username='deep', password="Deepak@7415", csrfmiddlewaretoken=csrftoken, next='/')
  r = client.post(url, data=login_data, headers=dict(Referer=url),allow_redirects=True)
  
  return r

print(redirect_url())