import csv
from datetime import datetime

REMINDERS_FILE = "reminders.csv"

def get_reminders():
    file = open(REMINDERS_FILE, mode='r')
    reader = csv.reader(file)
    reminders = []
    for row in reader:
        reminders.append(row)
    file.close()
    return reminders

def add(reminder):
    file = open(REMINDERS_FILE, "a")
    writer = csv.writer(file)
    writer.writerow(reminder)
    file.close()

def remove(reminder):
    reminders = get_reminders()
    i = 0
    for el in reminders:
        if(reminder == el):
            reminders.pop(i)
            csv_file = open(REMINDERS_FILE, mode='w', newline='')
            writer = csv.writer(csv_file)
            writer.writerows(reminders)
            csv_file.close()
            return True
        i +=1
    return False
    
def check():
    obj = datetime.now()
    date = obj.strftime("%H:%M")
    time = obj.strftime("%d-%m-%Y")
    reminders = get_reminders()

    for el in reminders:
        if(el[1] == date and el[2]==time):
            return [True, el[0], el[3]]
    return[False]