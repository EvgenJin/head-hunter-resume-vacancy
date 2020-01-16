# -*- coding: UTF-8 -*-
from hh_vacancy import get_vacancy
from hh_resume import get_resume

# query = 'python'
for query in ['Java','nodejs','plsql','python']:
    
    area = 1
    period = 30

    df_vacancy = get_vacancy(query,area)
    df_resume = get_resume(query,area,period)

    resume_salary = round(df_resume['salary'].mean())
    resume_count = df_resume['salary'].count()
    vacancy_salary = round(df_vacancy['salary.from'].mean())
    vacancy_count = df_vacancy['salary.from'].count()
    salary_balance = (resume_salary  + vacancy_salary) / 2

    print(query + ': спрос: ' + str(vacancy_salary) + '('+ str(vacancy_count) + ')'+ '; предложение :' + str(resume_salary) + '('+ str(resume_count) + ')'+'; равновесная: ' + str(salary_balance))

