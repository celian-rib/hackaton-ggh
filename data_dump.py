import csv

def main():
    with open('accidents.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for row in spamreader:
            print(', '.join(row))

if __name__ == '__main__':
    main()