def is_leap(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("leap year")
        return True
    else:
        print("not leap year")
        return False
is_leap(int(input("year:")))
