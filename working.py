import re
import sys


def main():
    print(convert(input("Hours: ").upper()))


def convert(s):
    am,pm = s.split(" TO ")
    match_am = re.search(r"[0-9]{1,2}:?[0-9]{0,22} (AM|PM)", am)
    match_pm = re.search(r"[0-9]{1,2}:?[0-9]{0,2} (AM|PM)", pm)
    result_am = match_am.group()
    result_pm = match_pm.group()
    result_am = result_am.split(" ")
    result_pm = result_pm.split(" ")
    if ":" in  result_am[0] and ":" in  result_pm[0]:
        hours_am,minutes_am= result_am[0].split(":")
        hours,minutes= result_pm[0].split(":")
        hours= int(hours)+12
        minutes= int(minutes)
        hours_am= int(hours_am)
        minutes_am= int(minutes_am)
        if minutes >= 60 or hours >= 24 or hours_am > 12 or minutes_am >= 60 :
            raise ValueError
        if hours_am == 12:
            hours_am = 0
        if hours == 12:
            hours = 12
        final_am= f"{hours_am}:{minutes_am}"
        final_pm=f"{hours}:{minutes}"
        return f"{final_am} to {final_pm}"
    else:
        result_pm[0]= int(result_pm[0])+12
        if result_am[0] == "12":
            result_am[0] = "0"
        if result_pm[0] == 24:
            result_pm[0] = "12"
        return f"{result_am[0]} to {result_pm[0]}"




if __name__ == "__main__":
    main()

