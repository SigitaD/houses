from cs50 import SQL
from sys import argv, exit
import csv

db = SQL("sqlite:///students.db")


# Duomenys is csv failo sukeliami i DB, lentele "students", i atitinkamas grafas.


def main():
    validate_files(argv)
    name, house, birth = read_csv()
    first_name, middle_name, last_name = split_name(name)

    for i in range(len(first_name)):
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?,?,?,?,?)",
                   first_name[i], middle_name[i], last_name[i], house[i], birth[i])


# Patikrinama, ar user'is ivede reikiama kieki argumentu.


def validate_files(argv):
    if len(argv) != 2:
        print("Erorr: CSV file is required to run the programme.")
        exit(1)


# Nuskaitomas user'io nurodytas csv failas. Faile esantys duomenys pagal kategorijas sukeliami i atitinkamus listus, kad juos galetu naudoti kitos f-cijos (main() ir split_name()).


def read_csv():
    with open(argv[1], 'r') as file:
        reader = csv.DictReader(file)
        name_list = []
        house_list = []
        birth_list = []
        for student in reader:
            name = student["name"]
            name_list.append(name)
            house = student["house"]
            house_list.append(house)
            birth = student["birth"]
            birth_list.append(birth)
        return name_list, house_list, birth_list


# Vardu list'as yra iskirstomas atskiras kategorijas "first", "middle", "last". Jei name sudaro 2 zodziai, "middle" priskiriama "none" reiksme. Split'inti vardai sudedami i listus, kad juos galetu buti naudojami main() f-cijoje.


def split_name(name):
    split_name = []
    first_name = []
    middle_name = []
    last_name = []
    for i in range(len(name)):
        splitted_name = name[i].split(" ")
        split_name.append(splitted_name)

        if len(split_name[i]) == 2:
            first = splitted_name[0]
            first_name.append(first)
            middle = None
            middle_name.append(middle)
            last = splitted_name[1]
            last_name.append(last)
        else:
            first = splitted_name[0]
            first_name.append(first)
            middle = splitted_name[1]
            middle_name.append(middle)
            last = splitted_name[2]
            last_name.append(last)
    return first_name, middle_name, last_name


main()