import datetime
def day(date_str):
    try:
         date_obj = datetime.datetime.strptime(date_str, '%d %m %Y')
         return date_obj.strftime('%A')
    except ValueError:
         return "Invalid date format. Please use DD MM YYYY."

date_input = input("Enter date format: ")
day = day(date_input)
print(f"Output: {day}")
