import colorama     # importing colorama python library for colorful text
from colorama import Fore
colorama.init(autoreset=True)

from datetime import date
from calendar import monthrange

# defining a function to calculate the age in days, months and year using given Date of Birth
def age_calculator(year, month, day):
    dob = date(year, month, day)
    t = date.today()
    age = t.year - dob.year - ((t.month, t.day) < (dob.month, dob.day))
    year_days = 0
    for i in range(year, t.year + 1):
        if i%4==0:
            year_days += 366
        else:
            year_days += 365
    if dob.month - t.month > 0:
        agem = t.month + (12 - dob.month)
        month_days = 0
        for i in range(t.month, 13):
            month_days += monthrange(dob.year, i)[1]
        for j in range(1, dob.month + 1 ):
            month_days += monthrange(t.year, j)[1]
    else:
        agem = abs(dob.month - t.month)
        month_days = 0
        for j in range(1, t.month + 1):
            month_days += monthrange(t.year, j)[1]
    if t.day - dob.day > 0:
        aged = t.day - dob.day
    else:
        aged = monthrange(dob.year, dob.month)[1] - abs(t.day - dob.day)
    print(f"{Fore.CYAN}Formats of your age calculation: ")
    print(f"{Fore.YELLOW}[1.] X years, Y months and Z days")
    print(f"{Fore.YELLOW}[2.] X months and Y days")
    print(f"{Fore.YELLOW}[3.] X days")
    print(f"{Fore.YELLOW}[4.] All formats")
    format = input(f"Choose the format of your age calculation: ")
    print()
    if format == "1" or format.lower() == "one":
        print(f"{age} year(s), {agem} month(s) and {aged} day(s)")
    elif format == "2" or format.lower() == "two" or format.lower() == "second":
        print(f"{(12 * age) + agem} month(s) and {aged} day(s)")
    elif format == "3" or format.lower() == "three" or format.lower() == "third":

        print(f"{year_days + month_days} day(s)")
    elif format == "4" or format.lower() == "four" or format.lower() =="fourth":
        print(f"[1] {age} year(s), {agem} month(s) and {aged} day(s)")
        print(f"[2] {(12 * age) + agem} month(s) and {aged} day(s)")
        print(f"[3] {year_days + month_days} day(s)")
    else:
        print("Invalid input!")

# Strating the program
if __name__ == '__main__':
    # taking DOB as user input
    y = int(input(f"{Fore.CYAN}Enter the year of birth: "))
    m = int(input(f"{Fore.CYAN}Enter the month of birth(1-12): "))
    d = int(input(f"{Fore.CYAN}Enter the day of the birth: "))
    # calling function to calculate age
    age_calculator(y, m, d)
