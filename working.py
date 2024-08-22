import re
import sys


def main():
    print(convert(input("Hours: ").upper()))


def convert(s):
    am,pm = s.split(" TO ")
    print(am, pm)
    matches= re.search(r"[0-9]{1,2}:[0-9]{2} (AM|PM)" ,am)
    result= matches.group()
    print(result)



if __name__ == "__main__":
    main()
