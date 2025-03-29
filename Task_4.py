from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    next_week = today + timedelta(days=7)
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        if today <= birthday_this_year <= next_week:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() >= 5: # 5 - субота, 6 - неділя
                days_until_monday = (7 - congratulation_date.weekday())
                congratulation_date += timedelta(days=days_until_monday)

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': congratulation_date.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays

#Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
