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
    for marker, dict in list_with_dict.items():
        fvalue, pvalue = scipy.stats.f_oneway(dict['a'], dict['b'])
        count = count + 1
        print(marker, pvalue, fvalue, count)
