import csv

len_all_rows = []
all_lines  = []
with open("t2.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for i in csv_reader:
        all_lines.append(i)
        len_elements_in_row = list(map(len, i))
        len_all_rows.append(len_elements_in_row)
max_all = []
for i in zip(*len_all_rows):
    max_all.extend([max(i)])
print(max_all)
txt_file = open("out.txt", "w")

for i in all_lines:
    line = ""
    for ii, item in enumerate(i):
        line += " ".join(["|", item, (max_all[ii]-len(item))*" "])
    txt_file.writelines(line+"|"+"\n")
