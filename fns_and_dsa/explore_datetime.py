from datetime import datetime , timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date , days):
    future_date = current_date + timedelta(days = days)
    print(f"Future date: {future_date.strftime("%Y-%m-%d %H:%M:%S")}")
    return future_date


current_date = display_current_datetime()
days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(current_date , days)