from datetime import datetime

def get_days_from_today(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        return (date_obj - today).days
    except ValueError:
        return "Неправильний формат дати"

#Приклад використання
print(get_days_from_today('2021-10-09'))
