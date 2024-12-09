
weekly_profit = {
    "Monday": 150,
    "Tuesday": 152,
    "Wednesday": 156,
    "Thursday": 153,
    "Friday": 155,
    "Saturday": 151,
    "Sunday": 150
}
a = max(weekly_profit, key=weekly_profit.get)
print(a)
