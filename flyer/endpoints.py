import requests

def get_category():
  url ="http://127.0.0.1:8000/api/category/"
  r = requests.get(url)
  category = r.json()
  result=category['results']
  return result

def get_page_format():
  url ="http://127.0.0.1:8000/api/page_format/"
  r = requests.get(url)
  page_format = r.json()
  result=page_format['results']
  return result

def get_stopper_format():
  url ="http://127.0.0.1:8000/api/stopper_format/"
  r = requests.get(url)
  stopper_format = r.json()
  result=stopper_format['results']
  return result

def get_poster_format():
  url ="http://127.0.0.1:8000/api/poster_format/"
  r = requests.get(url)
  poster_format = r.json()
  result=poster_format['results']
  return result

def get_project_list():
  url ="http://127.0.0.1:8000/api/project_list/"
  r = requests.get(url)
  project_list = r.json()
  result=project_list
  print(result)
  return result

def get_project_pdf():
  url ="http://127.0.0.1:8000/api/project_pdf/"
  r = requests.get(url)
  project_pdf = r.json()
  result=project_pdf
  print(result)
  return result