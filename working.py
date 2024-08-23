import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if not " to " in s:
        raise ValueError
    am,pm = s.split(" to ")
    match_am = re.search(r"([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)", am, re.IGNORECASE)
    match_pm = re.search(r"([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)", pm, re.IGNORECASE)
    if match_am == None or match_pm == None:
        raise ValueError
    hours_am, minutes_am, period_am = match_am.groups()
    hours_pm, minutes_pm, period_pm = match_pm.groups()
    minutes_am = int(minutes_am) if minutes_am else 0
    minutes_pm = int(minutes_pm) if minutes_pm else 0
    hours_am= int(hours_am)
    hours_pm = int(hours_pm)
    if hours_am >= 13 or minutes_am >= 60 or minutes_pm >= 60 or hours_pm >= 13:
        raise ValueError
    if period_am.upper() == "AM" or period_pm.upper == "AM":
         hours_am = 0 if hours_am == 12 else hours_am
         hours_pm = 12 if hours_pm == 12 else hours_pm+12
    else:
        hours_am = 12 if hours_am == 12 else hours_am+12
        hours_pm = 0 if hours_pm == 12 else hours_pm
    final_am = f"{hours_am:02d}:{int(minutes_am):02d}"
    final_pm = f"{hours_pm:02d}:{minutes_pm:02d}"
    return f"{final_am} to {final_pm}"











if __name__ == "__main__":
    main()

