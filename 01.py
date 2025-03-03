from datetime import datetime

def get_days_from_today(date: str):
  today = datetime.today().date()
  date = datetime.strptime(date, "%Y-%m-%d").date()
  return (today - date).days

date = "2022-02-24"
days = get_days_from_today(date)

print("Days from today:", days)