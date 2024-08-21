import jdatetime
from datetime import datetime

def age_calculator(birth_year, birth_month, birth_day):
    birth_date_jalali = jdatetime.date(birth_year, birth_month, birth_day)
    today_jalali = jdatetime.date.today()
       
    birth_date_gregorian = birth_date_jalali.togregorian()
    today_gregorian = today_jalali.togregorian()
     
    birth_date = datetime(birth_date_gregorian.year, birth_date_gregorian.month, birth_date_gregorian.day)
    today_date = datetime(today_gregorian.year, today_gregorian.month, today_gregorian.day)
    
    age_years = today_date.year - birth_date.year
    age_months = today_date.month - birth_date.month
    age_days = today_date.day - birth_date.day
    
    if age_days < 0:
        prev_month = today_date.month - 1 
        prev_year = today_date.year 
        days_in_prev_month = (datetime(prev_year, prev_month + 1, 1) - datetime(prev_year, prev_month, 1)).days
        
        age_days += days_in_prev_month
        age_months -= 1
        
    if age_months <0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days



birth_year = int(input("please enter a year: "))
birth_month = int(input("please nter a month: "))
birth_day = int(input("please enter a day: "))

age = age_calculator(birth_year, birth_month, birth_day)
print(f"Age: {age[0]} years, {age[1]} months, {age[2]} days")