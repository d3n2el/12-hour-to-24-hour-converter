import re
import sys


def main():
    print(convert(input("Hours: ").upper()))


def convert(s):
    am,pm = s.split(" TO ")
    match_am = re.search(r"[0-9]{1,2}:[0-9]{2} (AM|PM)", am)
    match_pm = re.search(r"[0-9]{1,2}:[0-9]{2} (AM|PM)", pm)
    if match_am and match_pm:
        result_am = match_am.group()
        result_pm = match_pm.group()
        result_am = result_am.split(" ")
        result_pm = result_pm.split(" ")
        return f"{result_am[0]} {result_pm[0]}"
    else:
        print("No match found")



if __name__ == "__main__":
    main()
