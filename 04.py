import datetime

def get_upcoming_birthdays(users):
    today = datetime.date.today()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        
        next_week = today <= birthday_this_year <= today + datetime.timedelta(days=7)
        print(f"Hаступного тижня: {next_week}")
        
        saturday = birthday_this_year.weekday() == 5
        sunday = birthday_this_year.weekday() == 6
        print(f"Субота чи неділя: {saturday} {sunday}")
        
        if next_week:
            if saturday:
                birthday_this_year += datetime.timedelta(days=2)
            elif sunday:
                birthday_this_year += datetime.timedelta(days=1)
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.03.03"},
    {"name": "Jane Smith", "birthday": "1990.03.08"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
