from operator import methodcaller

def write_table(table, tab_index, out_file):
    len_all_rows, len_elements_in_row = [], []
    for i in table :
        len_elements_in_row = list(map(len, i))
        len_all_rows.append(len_elements_in_row)
    max_all = []
    for i in zip(*len_all_rows):
        max_all.extend([max(i)])
    for i in table:
        line = ""
        for ii, item in enumerate(i):
            line += " ".join(["|", item, (max_all[ii]-len(item))*" "])
        out_file.writelines(tab_index*" " + line +"|"+"\n")


in_file_name = input("input your file name : ")
table = []
try : 
    with open(in_file_name) as gh_file:
        out_file_name = "out" + in_file_name
        out_file = open(out_file_name, "w")
        TAB_SIZE = 0
        for i in gh_file:
            i_stripped = i.strip()
            if len(i_stripped) > 0:
                if i_stripped[0] == "|":
                    if not table : 
                        TAB_SIZE = i.find("|")
                    table.append(list(map(methodcaller("strip"),  i_stripped[1:-1].split('|'))))  
                else :
                    if table:
                        write_table(table, TAB_SIZE, out_file)
                        table = [] 

                    out_file.writelines(i)
            else :
                out_file.writelines("\n")
except IOError:
    print("there is IO error, please make sure that you entered a valid file!")
    exit()

print("Done styling {}, now you can check  {} for pretty tables!".format(in_file_name, out_file_name))
