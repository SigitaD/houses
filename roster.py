from cs50 import SQL
from sys import argv, exit
import csv

db = SQL("sqlite:///students.db")


# Pagal user'op ivesta house name, parenkami duomenys is DB. Duomenys atspausdinami.


def main():
    house = validate_command(argv)
    result = db.execute("SELECT * FROM students WHERE house = ? ORDER BY last, first", house)

    for i in result:
        if (i['middle'] == None):
            print(i['first'], i['last']+', born', i['birth'])
        else:
            print(i['first'], i['middle'], i['last']+", born", i['birth'])


# Patikrinama, ar user'is ivede reikiama kieki argumentu ir tinkama House name.


def validate_command(argv):
    if (len(argv) != 2):
        print("Error. Programme usage: python roster.py House_name")
        exit(1)
    elif (argv[1] != "Gryffindor" and argv[1] != "Hufflepuff" and argv[1] != "Ravenclaw" and argv[1] != "Slytherin"):
        print("Erorr: command should contain name of the house")
        exit(1)
    return argv[1]


main()