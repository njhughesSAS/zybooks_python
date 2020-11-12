# Write a program that first reads in the name of an input file and then reads the file using the csv.reader()
# method. The file contains a list of words separated by commas. Your program should output the words and their
# frequencies (the number of times each word appears in the file) without any duplicates.
#
# Ex: If the input is:
#
# input1.csv
# and the contents of input1.csv are:
#
# hello,cat,man,hey,dog,boy,Hello,man,cat,woman,dog,Cat,hey,boy
# the output is:
#
# hello 1
# cat 2
# man 2
# hey 2
# dog 2
# boy 2
# Hello 1
# woman 1
# Cat 1
# Note: There is a newline at the end of the output, and input1.csv is available to download.

import csv

#filename = input()


a = []
counts = []
l = []
with open('input1.csv', 'r') as f:
    contents = csv.reader(f)
    for i in contents:
        for item in i:
            a.append(item)
        for item in i:
            if item not in l:
                l.append(item)
    for i in l:
        print(i, a.count(i))

