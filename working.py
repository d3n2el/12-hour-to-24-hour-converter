import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if not " to " in s:
        raise ValueError
    am,pm = s.split(" to ")
    match_am = re.search(r"[0-9]{1,2}:?[0-9]{0,22}? (AM|PM)\b", am, re.IGNORECASE)
    match_pm = re.search(r"[0-9]{1,2}:?[0-9]{0,2}? (AM|PM)\b", pm, re.IGNORECASE)
    if match_am == None or match_pm == None:
        raise ValueError
    hours_am, minutes_am, period_am = match_am.groups()
    hours_pm, minutes_pm, period_pm = match_pm.groups()
    if find_am and find_pm:
        results_am= re.split(r"\s", match_am)
        results_pm= re.split(r"\s", match_pm)
        if ":" in match_am:
            hours_am, minutes_am= re.split(r":",results_am[0])
            hours_am= int(hours_am)
            minutes_am= int(minutes_am)
            if hours_am >= 13 or minutes_am >= 60:
                raise ValueError
            final_am = f"{hours_am:02d}:{int(minutes_am):02d}"
        else:
            final_am = f"{int(results_am[0]):02d}"
        if ":" in match_pm:
            hours_pm, minutes_pm = re.split(r":", results_pm[0])
            hours_pm= int(hours_pm)
            minutes_pm= int(minutes_pm)
            if minutes_pm >= 60 or hours_pm >= 13:
                raise ValueError
            final_pm = f"{hours_pm+12:02d}:{minutes_pm:02d}"
        else:
            final_pm= f"{int(results_pm[0])+ 12:02d}"


        return f"{final_am} to {final_pm}"
    else:
        results_am= re.split(r"\s", match_am)
        results_pm= re.split(r"\s", match_pm)
        if ":" in match_am:
            hours_am, minutes_am= re.split(r":",results_am[0])
            final_am = f"{int(hours_am):02d}:{int(minutes_am):02d}"
        else:
            final_am = f"{int(results_am[0])+12:02d}:00"
        if ":" in match_pm:
            hours_pm, minutes_pm = re.split(r":", results_pm[0])
            final_pm = f"{int(hours_pm)+12:02d}:{int(minutes_pm):02d}"
        else:
            final_pm= f"{int(results_pm[0]):02d}:00"

        return f"{final_am} to {final_pm}"








if __name__ == "__main__":
    main()

