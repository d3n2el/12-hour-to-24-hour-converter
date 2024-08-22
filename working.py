import re
import sys


def main():
    print(convert(input("Hours: ").upper()))


def convert(s):
    am,pm = s.split(" TO ")
    match_am = re.search(r"[0-9]{1,2}:?[0-9]{0,22} (AM|PM)", am)
    match_pm = re.search(r"[0-9]{1,2}:?[0-9]{0,2} (AM|PM)", pm)
    if match_am == None or match_pm == None:
        raise ValueError
    result_am = match_am.group()
    result_pm = match_pm.group()
    result_am = result_am.split(" ")
    result_pm = result_pm.split(" ")
    if ":" in  result_am[0] and ":" in  result_pm[0]:
        if "PM" in result_am[1]:
            hours_am,minutes_am= result_am[0].split(":")
            hours_pm,minutes_pm= result_pm[0].split(":")
            hours_pm= int(hours_pm)
            minutes_pm= int(minutes_pm)
            hours_am= int(hours_am)
            minutes_am= int(minutes_am)
            if minutes_pm >= 60 or hours_pm >=13 or hours_am >= 13 or minutes_am >= 60 :
                raise ValueError
            if hours_pm == 12:
                hours_pm = 0
            if hours_am == 12:
                hours_am = 12
            else:
                hours_am= hours_am+12
            final_am= f"{hours_pm:02d}:{minutes_am:02d}"
            final_pm=f"{hours_am:02d}:{minutes_pm:02d}"
            return f"{final_pm} to {final_am}"


        hours_am,minutes_am= result_am[0].split(":")
        hours_pm,minutes_pm= result_pm[0].split(":")
        hours_pm= int(hours_pm)
        minutes_pm= int(minutes_pm)
        hours_am= int(hours_am)
        minutes_am= int(minutes_am)
        if minutes_pm >= 60 or hours_pm >=13 or hours_am >= 13 or minutes_am >= 60 :
            raise ValueError
        if hours_am == 12:
            hours_am = 0
        if hours_pm == 12:
            hours_pm = 12
        else:
            hours_pm= hours_pm+12
        final_am= f"{hours_am:02d}:{minutes_am:02d}"
        final_pm=f"{hours_pm:02d}:{minutes_pm:02d}"
        return f"{final_am} to {final_pm}"
    else:
        if "PM" in result_am[1]:
            result_pm[0]= int(result_pm[0])
            result_am[0] = int(result_am[0])+12
            if result_pm[0] == 12:
                result_pm[0] = 0
            if result_am[0] == 24:
                result_am[0] = 12
            return f"{result_am[0]:02d}:00 to {result_pm[0]:02d}:00"
        else:
            result_pm[0]= int(result_pm[0])+12
            result_am[0] = int(result_am[0])
            if result_am[0] == 12:
                result_am[0] = 0
            if result_pm[0] == 24:
                result_pm[0] = 12
            return f"{result_am[0]:02d}:00 to {result_pm[0]:02d}:00"




if __name__ == "__main__":
    main()

