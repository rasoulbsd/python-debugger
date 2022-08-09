import os

dir_path = r'.'


# get all python files in the directory, recursivly
py_files_list = []
for i  in os.walk(dir_path):
    py_files_list.extend(list(filter(None, map(lambda x:  "{}/{}".format(i[0],x) if ((".py" in x) and (".pyc" not in x)) else None , i[2])))) 


# working on each file gathered in the list above
for py_file in py_files_list:
    if(py_file == "./main.py"):
        continue

    # opening the file in read mode
    f = open(py_file, "r")
    contents = (f.read()).split("\n")
    for i in range(len(contents)):
        # calculate indents needed before the print statement
        if("def " in contents[i]):
            indents = "\t"
            for charactor in contents[i]:
                if(charactor != "d"):
                    indents = " " + indents
                else:
                    break
            # adding the print statement to end of the line of def statement with an enter (\n)
            contents[i] = "{}\n{}print('{}')".format(contents[i], indents, contents[i].replace("'", ""))

    # joining the contents of the file back together
    final_text = ""
    for i in contents:
        final_text = "{}\n{}".format(final_text, i)
    f.close()

    # opening the file in write mode and writing the contents
    f = open(py_file, "w")
    f.write(final_text)
    f.close()


