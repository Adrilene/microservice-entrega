from datetime import date

def generate_date():
    today = date.today()
    day = today.day + 15
    month = today.month
    year = today.year
    months_less_31 = [4, 6, 9, 11]

    if day >= 31:
        if month in months_less_31:
            day -= 30
        elif month == 2: 
            day -= 28
        else: 
            day -= 31

        if month == 12: 
            year += 1
            month = 1
        else: 
            month += 1
    
    return f'{str(day).zfill(2)}/{str(month).zfill(2)}/{year}'


print(generate_date())