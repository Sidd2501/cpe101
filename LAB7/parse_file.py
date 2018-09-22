# Lab 7
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

import sys
args = sys.argv


def main():
    if len(args) < 2 or len(args) > 3:
        print('Usage: [-s] file_name')
        exit()
    elif len(args) == 2:
        file_name = args[1]
    elif len(args) == 3:
        if '-s' not in args:
            print('Usage: [-s] file_name')
            exit()
        elif '-s' == args[1]:
            file_name = args[2]
        else:
            file_name = args[1]
    try:
        is_in_file = open(file_name, 'r')
    except FileNotFoundError:
        print('Unable to open ' + file_name)
        exit()
    except PermissionError:
        print('Unable to open ' + file_name)
        exit()
    integers = 0
    floaters = 0
    other_type = 0
    sumitup = 0
    for line in is_in_file:
        splitter = line.split()
        for supper in splitter:
            try:
                float(supper)
                isfloat = True
            except:
                isfloat = False
            if supper.isdigit():
                integers += 1
                sumitup += int(supper)
            elif isfloat:
                floaters += 1
                sumitup += float(supper)
            else:
                other_type += 1
    if '-s' in args:
        print('Sum:', sumitup)
    print('Ints:', integers)
    print('Floats:', floaters)
    print('Other:', other_type)


if __name__ == '__main__':
    main()
