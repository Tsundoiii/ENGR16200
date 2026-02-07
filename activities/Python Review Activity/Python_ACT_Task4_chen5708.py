# Python Review Activity
# File: Python_ACT_Task4_chen5708.py
# Description: Program for sorting dates
# Date: 12 January 2026
# By: Aurora Chen
# chen5708
# Shushil Rao
# rao320
# Porter Stone
# stonpj01
# Caroline Spoelker
# cspoelke
# Section: 2
# 
# ELECTRONIC SIGNATURE
# Full Name team member 1
# Full Name team member 2
# Full Name team member 3
# Full Name team member 4
# 
# The electronic signatures above indicate that the program
# submitted for evaluation is the combined effort of all
# team members and that each member of the team was an
# equal participant in its creation. In addition, each
# member of the team has a general understanding of
# all aspects of the program development and execution.
# 
# Sorts a given file of dates into past, present, and
# future and outputs them to another file.

from datetime import datetime

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

future = []
present = []
past = []

current_month = datetime.today().month
current_year = datetime.today().year

with open("Python_ACT_Task4_input.txt") as fid:
    lines = [[date.split()[0], int(date.split()[1])] for date in fid.readlines()]

def Sort_Dates(dates: list[tuple[str, int]]):
    for date in dates:
        month = months[date[0]]
        year = date[1]

        if month == current_month and year == current_year:
            present.append(date)
        elif current_year > year:
            past.append(date)
        else:
            future.append(date)

    present.sort(key = lambda date: f"{date[1]}.{months[date[0]]}")
    past.sort(key = lambda date: f"{date[1]}.{months[date[0]]}")
    future.sort(key = lambda date: f"{date[1]}.{months[date[0]]}")

Sort_Dates(lines)

with open("Python_ACT_Task4_output.txt", "w") as output:
    output.write(f"Future dates: {len(future)}\n")
    output.writelines([f"{date[0]} {date[1]}\n" for date in future])

    output.write("\n")

    output.write(f"Present dates: {len(present)}\n")
    output.writelines([f"{date[0]} {date[1]}\n" for date in present])

    output.write("\n")

    output.write(f"Past dates: {len(past)}\n")
    output.writelines([f"{date[0]} {date[1]}\n" for date in past])