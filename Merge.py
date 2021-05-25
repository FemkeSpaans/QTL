# Author: Femke Spaans en David van Eersel
# Date: 25.05.2021
# Name: Merge QTL
# Version: 1


def merge_files(new_loc, new_qua):
    """

    :param new_loc:
    :param new_qua:
    :return:
    """
    list_with_dict = {}

    # {marker:{a:[waarde],b:[waarde]}}
    for marker, loc in new_loc.items():
        temp = {"a": [], "b": []}
        for l in range(len(loc)):
            if new_qua[l][1] != "-":
                if loc[l] == 'a':
                    temp["a"].append(new_qua[l][1])
                elif loc[l] == "b":
                    temp["b"].append(new_qua[l][1])
        list_with_dict[marker] = temp
    return list_with_dict
