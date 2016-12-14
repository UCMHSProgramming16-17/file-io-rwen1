# Dec 14, 2016
# Create a program that can write to a csv file
import csv

text_in = "_"
array_in = []

filename = input("Please Name Your File (default csvfile.csv):  ")
if filename == "":
    filename = "csvfile"
filename += ".csv"

csvfile = open(filename, 'w')
csvwriter = csv.writer(csvfile, delimiter = ',')

while True:
    text_in = input("Add text:  ")
    if text_in == "exit()":
        if array_in != []:
            csvwriter.writerow(array_in)
        break
    if text_in == "":
        csvwriter.writerow(array_in)
        array_in = []
    else:
        array_in.append(text_in)

csvfile.close()