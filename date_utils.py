from datetime import datetime
def days_before(date_string):
    deadline = datetime.fromisoformat(date_string)
    today = datetime.today()
    days = deadline - today
    return days.days
