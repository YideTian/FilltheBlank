#
# Created: 20170812
# Modified:
#
#
#
#
########################################################

import sys
import xlrd

xlpath = sys.path[0] + '\Test_Library.xlsx'
xldata = xlrd.open_workbook(xlpath)
sheet1_data = xldata.sheet_by_name('Sheet1')

quiz_num = len(sheet1_data.col_values(0)) - 1


def difficulty_choose(difficulty):
    """this function output a group of  question based on the difficulty"""

    question = []
    answer = []
    for i in range(quiz_num):
        if sheet1_data.row_values(i+1)[0].lower() == difficulty.lower():
            # print sheet1_data.row_values(i+1)[1]
            question.append(sheet1_data.row_values(i+1)[1])
            answer.append(sheet1_data.row_values(i+1)[2])
    return question, answer
