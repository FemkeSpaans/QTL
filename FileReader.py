# Author: Femke Spaans en David van Eersel
# Date: 20.05.2021
# Name: FileReader QTL
# Version: 1

def read_files():
    """
    Reads the files CvixLerC9.loc and CvixLerC9.qua.
    Changes the file CvixLerC9.qua into the format [['1', '1.279502474'], ['3', '0.303712231']....]
    Changes the file CvixLerC9.loc {'PVV4 (a,b) ; 1': ['a', 'a', 'b', 'a', 'b', 'b', 'a',
    :return: new_loc, new_qua
    """
    with open("CvixLerC9.loc") as loc, open("CvixLerC9.qua") as qua:
        qua_file = (qua.read().split('\n'))
        qua_file = qua_file[8:-1]
        new_qua = []
        for q in qua_file:
            new_qua.append(q.split('\t'))  # [['1', '1.279502474'], ['3', '0.303712231']....]

        new_loc = {}
        header = ''
        read = False
        for i in loc:
            i = i.replace("\n", '')
            if read:
                for j in i:
                    if " " != j:
                        if header in new_loc.keys():
                            new_loc[header].append(j)
                        else:
                            new_loc[header] = [j]
            if "(a,b)" in i:
                header = i
                read = True
            else:
                read = False

            elif read:
                for j in i:
                    if " " != j:
                        if header in new_loc.keys():
                            new_loc[header].append(j)
                        else:
                            new_loc[header] = [j]

        return new_loc, new_qua
