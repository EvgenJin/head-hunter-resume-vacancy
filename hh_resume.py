from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# страница со всеми резюме 
def get_all (page):
  period = 7 # за сколько дней
  area = 1 # Екатеринбург 3 / Москва 1
  querry = 'plsql' # Ключевое слово
  url = 'https://hh.ru/search/resume?text='+querry +'&specialization=1&clusters=true&order_by=publication_time&no_magic=false&st=resumeSearch&logic=normal&pos=keywords&order_by=publication_time&exp_period=all_time&area=' + str(area) + '&search_period='+str(period)+'&page='+str(page)
  #pos=full_text / keywords
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
  res = requests.get(url, headers=headers)
  soup_all = BeautifulSoup(res.content, 'html.parser')
  data_all = soup_all.find_all('div', {'data-qa':"resume-serp__resume"})  
  # print(res.status_code)
  return data_all

# scan page with one vacancy
def get_one(id):
  url = 'https://hh.ru'+id
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
  res = requests.get(url, headers=headers)
  return res

# if null function
def if_null_bf(par):
  if par:
    res = par.get_text()
  else:
    res = ''  
  return res

# колонки и массив строк для dataframe
columns = ['title','dbirth','salary','last_work','last_work_per','url']
rows = []

i=0
# запрашивать пока массив не опустеет
while len(get_all(i)) > 0:
  result_all = get_all(i)
  # i = i + 1
  i +=1
  for item in result_all:
    id = item.find('a', href=True)['href']
    result_one = get_one(id)
    soup_one = BeautifulSoup(result_one.content, 'html.parser')
    title = soup_one.find('span',class_='resume-block__title-text resume-block__title-text_position').find("span")
    dbirth = soup_one.find('meta',itemprop="birthDate")
    if dbirth:
      dbirth = dbirth["content"]
    else:
      dbirth = ''    
    salary = soup_one.find('span',class_='resume-block__salary resume-block__title-text_salary')
    last_work = soup_one.find('div',class_='resume-block__sub-title')
    last_work_per = soup_one.find('div',class_='bloko-column bloko-column_xs-4 bloko-column_s-2 bloko-column_m-2 bloko-column_l-2')
    row = [if_null_bf(title),dbirth,if_null_bf(salary),if_null_bf(last_work),if_null_bf(last_work_per),'https://hh.ru'+id]
    rows.append(row)

df = pd.DataFrame(rows, columns=columns)
print(df[['title','dbirth','salary','last_work']])




