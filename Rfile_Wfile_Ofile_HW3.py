import os.path


def file_merger(file_names):
    path = 'C:\\Users\\turra\\OneDrive\\Plocha\\Ramazan\\Programming languages and SW\\Python\\Projects\\Rfile-Wfile-Ofile_HW\\texty'
    with open(path + '\\3.txt', 'w', encoding="utf8") as outfile:
        for fname in file_names:
            num_lines = sum(1 for line in open(path + "\\" + fname))
            with open(path + "\\" + fname, encoding="utf8") as infile:
                outfile.write("\n"+fname+"\n")
                outfile.write(str(num_lines)+"\n")
                for line in infile:
                    outfile.write(line)

file_merger(['1.txt','2.txt'])