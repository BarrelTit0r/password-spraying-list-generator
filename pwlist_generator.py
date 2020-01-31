#! /usr/bin/env python

# Author:
#  Cameron Geehr (@BarrelTit0r)

import sys
import datetime
import calendar
import argparse
from datetime import date, datetime

# This code is from stackoverflow https://stackoverflow.com/questions/16139306/determine-season-given-timestamp-in-python-using-datetime
def get_season(now, hemisphere):
    Y = 2000 # dummy leap year to allow input X-02-29 (leap day)
    seasons = []
    if hemisphere == "N":
        seasons = [('Winter', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('Spring', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('Summer', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('Fall', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('Winter', (date(Y, 12, 21),  date(Y, 12, 31)))]
    else:
        seasons = [('Summer', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('Fall', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('Winter', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('Spring', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('Summer', (date(Y, 12, 21),  date(Y, 12, 31)))]

    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= now <= end)

def get_prev_season(now, hemisphere):
    conversion = {
            "Winter": "Fall",
            "Fall": "Summer",
            "Summer": "Spring",
            "Spring": "Winter"
    }
    return conversion.get(get_season(now, hemisphere), "An invalid season was returned")

# Returns a list of tuples with the months and corresponding years
def get_months_and_years(now):
    conversion = {
            "January": [("January", now.strftime("%Y")), ("December", str(int(now.strftime("%Y")) - 1)), ("November", str(int(now.strftime("%Y")) - 1)), ("October", str(int(now.strftime("%Y")) - 1))],
            "February": [("February", now.strftime("%Y")), ("January", now.strftime("%Y")), ("December", str(int(now.strftime("%Y")) - 1)), ("November", str(int(now.strftime("%Y")) - 1))],
            "March": [("March", now.strftime("%Y")), ("February", now.strftime("%Y")), ("January", now.strftime("%Y")), ("December", str(int(now.strftime("%Y")) - 1))],
            "April": [("April", now.strftime("%Y")), ("March", now.strftime("%Y")), ("February", now.strftime("%Y")), ("January", now.strftime("%Y"))],
            "May": [("May", now.strftime("%Y")), ("April", now.strftime("%Y")), ("March", now.strftime("%Y")), ("February", now.strftime("%Y"))],
            "June": [("June", now.strftime("%Y")), ("May", now.strftime("%Y")), ("April", now.strftime("%Y")), ("March", now.strftime("%Y"))],
            "July": [("July", now.strftime("%Y")), ("June", now.strftime("%Y")), ("May", now.strftime("%Y")), ("April", now.strftime("%Y"))],
            "August": [("August", now.strftime("%Y")), ("July", now.strftime("%Y")), ("June", now.strftime("%Y")), ("May", now.strftime("%Y"))],
            "September": [("September", now.strftime("%Y")), ("August", now.strftime("%Y")), ("July", now.strftime("%Y")), ("June", now.strftime("%Y")), ("May", now.strftime("%Y"))],
            "October": [("October", now.strftime("%Y")), ("September", now.strftime("%Y")), ("August", now.strftime("%Y")), ("July", now.strftime("%Y")), ("June", now.strftime("%Y"))],
            "November": [("November", now.strftime("%Y")), ("October", now.strftime("%Y")), ("September", now.strftime("%Y")), ("August", now.strftime("%Y")), ("July", now.strftime("%Y"))],
            "December": [("November", now.strftime("%Y")), ("October", now.strftime("%Y")), ("September", now.strftime("%Y")), ("August", now.strftime("%Y"))]    
    }
    return conversion.get(now.strftime("%B"))

def generate_seasonal_passwords(now, hemisphere):
    current_season = get_season(now, hemisphere)
    current_season_year = now.strftime("%Y")
    previous_season = get_prev_season(now, hemisphere)
    previous_season_year = ""
    if current_season == "Winter":
        previous_season_year = str(int(now.strftime("%Y")) - 1)
    else:
        previous_season_year = now.strftime("%Y")
    passwords = [
            current_season + current_season_year,
            current_season + current_season_year[2:4],
            current_season + current_season_year + "!",
            current_season + "@" + current_season_year,
            previous_season + previous_season_year,
            previous_season + previous_season_year[2:4],
            previous_season + previous_season_year + "!",
            previous_season + "@" + previous_season_year
    ]
    if previous_season == "Fall":
        passwords.extend([
                "Autumn" + previous_season_year,
                "Autumn" + previous_season_year[2:4],
                "Autumn" + previous_season_year + "!",
                "Autumn" + "@" + previous_season_year

            ])
    elif current_season == "Fall":
        passwords.extend([
                "Autumn" + current_season_year,
                "Autumn" + current_season_year[2:4],
                "Autumn" + current_season_year + "!",
                "Autumn" + "@" + current_season_year
            ])

    return passwords

def generate_organizational_passwords(now, organization):
    return [
            organization + now.strftime("%Y"),
            organization + "123",
            organization + "1!",
            organization + str(int(now.strftime("%Y")))[2:],
            organization + str(int(now.strftime("%Y")))[2:] + "!",
            organization + ".1",
            organization + "!"
    ]

def generate_monthly_passwords(now):
    passwords = []
    for tuple in get_months_and_years(now):
        passwords.append(tuple[0] + tuple[1])
        passwords.append(tuple[0] + tuple[1] + "!")
        passwords.append(tuple[0] + tuple[1][2:4])
        passwords.append(tuple[0] + "@" + tuple[1])
    return passwords

def generate_standard_passwords(now):
    return [
            "Welcome123",
            "Welcome" + now.strftime("%Y"),
            "Welcome" + now.strftime("%Y")[2:4],
            "Welcome" + now.strftime("%Y") + "!",
            "Welcome" + now.strftime("%Y")[2:4] + "!",
            "Welcome1!",
            "Welcome1",
            "Password1",
            "Password1!",
            "Password" + now.strftime("%Y"),
            "Password" + now.strftime("%Y")[2:4],
            "Password" + now.strftime("%Y") + "!",
            "Password" + now.strftime("%Y")[2:4] + "!",
            "Pa55word",
            "P@ssword",
            "Passw0rd",
        ]

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--hemisphere", help="Determines what seasons to use. N for northern, S for southern.", choices=["S","N"], default="N")
    parser.add_argument("organization", help="Nickname for the organization. Used in generating passwords based on the organization name.")
    args = parser.parse_args()
    
    passwords = []
    now = date.today()
    passwords.extend(generate_seasonal_passwords(now, args.hemisphere))
    passwords.extend(generate_organizational_passwords(now, args.organization))
    passwords.extend(generate_monthly_passwords(now))
    passwords.extend(generate_standard_passwords(now))
    for password in passwords:
        print (password)

if __name__ == "__main__":
    main()

