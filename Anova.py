# Author: Femke Spaans en David van Eersel
# Date: 25.05.2021
# Name: Anova QTL
# Version: 1

import pandas as pd

import scipy.stats


def calculate_anova(list_with_dict):
    """

    :param list_with_dict:
    :return:
    """
    count = 0
    anova_list = []
    file_create = open("anova.txt", "x")
    file_write = open("anova.txt", "w")
    for marker, dict in list_with_dict.items():
        fvalue, pvalue = scipy.stats.f_oneway(dict['a'], dict['b'])
        count = count + 1
        anova_list = marker, "\t", str(pvalue), "\t", str(fvalue), "\t", str(count), "\n"
        file_write.writelines(anova_list)

