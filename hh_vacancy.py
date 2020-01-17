# -*- coding: UTF-8 -*-
import requests
import json
import pandas as pd
from pandas.io.json import json_normalize
from datetime import datetime  
from datetime import timedelta   


import sys

def get_request (querry,area,page):
  # запрос
  # q = str(sys.argv[1]) 
  # q = 'Java'
  # регион или город (1 москва 3 екатеринбург)
  # area = str(sys.argv[2])
  # area = 3
  url = 'https://api.hh.ru/vacancies?area='+str(area)+'&page='+str(page)+'&per_page=10&text='+querry
  res = requests.get(url)
  return res

def get_vacancy(querry,area):
  i=1
  df = pd.DataFrame()
  # идти по всем станицам пока не придет статус не 200, запихать все в один фрейм
  while get_request(querry,area,i).status_code == 200 and len(get_request(querry,area,i).json()['items']) > 0:
    json_data = get_request(querry,area,i).json()
    norm = json_normalize(json_data['items'])
    dfi = pd.DataFrame(norm)
    # print('page :' + str(i) + ' length :' + str(len(get_request(i).json()['items'])))
    df = pd.concat([df,dfi],sort=False)
    i = i + 1

  # дата - 1 
  # new = datetime.now() + timedelta(days=-20)
  # res = df[['']]
  # указана зарплата
  # with_zp = df[df['salary.from'] > 0][['name','employer.name','salary.from','salary.to','published_at','alternate_url']]
  # не указана зарплата
  # without_zp = df[['name','employer.name','salary.from','salary.to','published_at','alternate_url']]
  # без зарплаты , но новые 
  # without_zp_new = df[df['published_at'] >= str(new)][['name','employer.name','salary.from','salary.to','published_at','alternate_url']]
  # without_zp_new.to_excel("output.xlsx")
  # res = df.agg({'salary.from':['mean','median','count']})
  return df
  # print(without_zp_new)
  # print(df[(df['salary.from'] > 0) & (df['salary.to'] > 0)][['name','employer.name','salary.from','salary.to','published_at','alternate_url','snippet.requirement','snippet.responsibility']])
  # print(df[df['salary.from'] > 0][['name','employer.name','salary.from','salary.to','published_at','alternate_url']])
  # print(df[['name','employer.name','salary.from','salary.to','published_at','alternate_url']])
  #print(df.agg({'salary.from':['mean','median','count']}))
  #df[df['salary.from'] > 0][['name','employer.name','salary.from','salary.to','published_at','alternate_url','snippet.requirement','snippet.responsibility']].to_csv('file.csv',encoding='utf-8-sig',sep=';')