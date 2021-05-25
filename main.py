# Author: Femke Spaans en David van Eersel
# Date: 20.05.2021
# Name: main QTL
# Version: 1
import FileReader
import Merge

if __name__ == '__main__':
    new_loc, new_qua = FileReader.read_files()
    list_with_dict = Merge.merge_files(new_loc, new_qua)
    Anova.calculate_anova(list_with_dict)

