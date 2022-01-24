age = input("what is your age? ")
age_as_int = int(age)
year_remainig = 90 - age_as_int
days_remainig = year_remainig * 365
week_remainig = year_remainig * 52
month_remainig = year_remainig * 12
print(month_remainig)
message = f"you have {days_remainig} days, {week_remainig} week, and {month_remainig} months left "
print(message)