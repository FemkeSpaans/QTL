# Author: Femke Spaans en David van Eersel
# Date: 20.05.2021
# Name: FileReader QTL
# Version: 1

def read_files():
    """

    :return:
    """
    with open("CvixLerC9.loc") as loc, open("CvixLerC9.qua") as qua:
        qua_file = (qua.read().split('\n'))
        qua_file = qua_file[8:-1]
        new_qua = []
        for q in qua_file:
            new_qua.append(q.split('\t'))

        loc_file = (loc.read().split('\n'))
        loc_file = loc_file[7:-1]
        print(loc_file)
        new_loc = {}
        for l in range(len(loc_file)):
            if not loc_file[l].startswith("  "):
                new_loc [loc_file[l]] = loc_file[l+1].replace("  ", " ").split(" ")
                temp = loc_file[l+1].replace("  ", " ").split(" ")
                temp.append(temp)
                print(temp)
                new_loc [loc_file[l]] = loc_file[l+2].replace("  ", " ").split(" ")
                new_loc [loc_file[l]] = loc_file[l+3].replace("  ", " ").split(" ")
                new_loc [loc_file[l]] = loc_file[l+4].replace("  ", " ").split(" ")
            #print(new_loc)


