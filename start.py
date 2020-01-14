from hh_vacancy import get_vacancy
from hh_resume import get_resume

df_vacancy = get_vacancy()
df_resume = get_resume()
salary_resume = df_resume['salary'].mean()
salary_vacancy = df_vacancy['salary.from'].mean()
salary_balance = (salary_resume  + salary_vacancy) / 2
# print(res_vacancy)
# print(res_resume)
# df["weight"].mean()
print('спрос: ' + salary_vacancy + ' предложение :' + salary_resume + ' равновесная: ' + salary_balance)