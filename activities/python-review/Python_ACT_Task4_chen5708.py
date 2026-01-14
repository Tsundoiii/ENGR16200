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