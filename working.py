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
    match_am= match_am.group()
    match_pm= match_pm.group()
    find_am= re.search(r"^AM$", match_am)
    find_pm= re.search(r"^PM$", match_pm)
    if find_am and find_pm:
        results_am= re.split(r"\s", match_am)
        results_pm= re.split(r"\s", match_pm)
        if ":" in match_am:
            hours_am, minutes_am= re.split(r":",results_am[0])
            final_am = f"{int(hours_am)}:{int(minutes_am)}"
        else:
            final_am = int(results_am[0])
        if ":" in match_pm:
            hours_pm, minutes_pm = re.split(r":", results_pm[0])
            final_pm = f"{int(hours_pm)+12}:{int(minutes_pm)}"
        else:
            final_pm= int(results_pm[0])+ 12

        return f"{final_am:02d}:00 to {final_pm:02d}:00"






if __name__ == "__main__":
    main()

