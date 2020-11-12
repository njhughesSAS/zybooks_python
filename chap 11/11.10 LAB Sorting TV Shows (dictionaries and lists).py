"""
Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method. The input file contains an unsorted list of number of seasons followed by the corresponding TV show. Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, and a list of TV shows are the values (since multiple shows could have the same number of seasons).

Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt, separating multiple TV shows associated with the same key with a semicolon (;). Next, sort the dictionary by values (alphabetical order), and output the results to a file named output_titles.txt.

Ex: If the input is:

file1.txt
and the contents of file1.txt are:

20
Gunsmoke
30
The Simpsons
10
Will & Grace
14
Dallas
20
Law & Order
12
Murder, She Wrote
the file output_keys.txt should contain:

10: Will & Grace
12: Murder, She Wrote
14: Dallas
20: Gunsmoke; Law & Order
30: The Simpsons
and the file output_titles.txt should contain:

Dallas
Gunsmoke
Law & Order
Murder, She Wrote
The Simpsons
Will & Grace
Note: There is a newline at the end of each output file, and file1.txt is available to download.
"""
titles = []
filename = input()
file_dict = dict()
with open(filename, 'r') as f:
    file_list = f.readlines()
    for i in range(0, len(file_list)-1, 2):
        key = file_list[i].rstrip()
        value = file_list[i+1].rstrip()
        if key not in file_dict:
            file_dict[key] = [value]
        else:
            file_dict[key].append(value)

with open("output_keys.txt", "w") as f:
    keys = sorted(list(file_dict.keys()))
    for k in keys:
        f.write("{:01d}".format(int(k)) + ": " + "; ".join(file_dict[k])+"\n")

with open("output_titles.txt", "w") as f:
    values = list(file_dict.values())
    for t in values:
    	for v in t:
        	titles.append(v)
    values = sorted(titles)
    for title in values:
         f.write("{}".format(title))
         f.write("\n")
