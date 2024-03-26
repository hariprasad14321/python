from datetime import date
ageofbirth=int(input("please tell your birth year "))
presentyear=date.today().year
age=presentyear-ageofbirth
print("age is ",age)