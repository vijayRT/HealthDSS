from opinion import Opinion
from binomialoperators import BinomialOperators
from dedabd import DedAbd
from decimal import *
binop = BinomialOperators()
import pandas as pd

# Deduction using Dispatch and Primary diagnosis
fields=['Call Number/Patient Number', 'DspProbCodeDescription', 'PrimaryProbDescription', 'SecondaryProbDescription']
data = pd.read_csv("EWEMSDataExport.csv", skipinitialspace=True, usecols=fields)
given_notgiven = {}
for index, row in data.iterrows():
    if row['PrimaryProbDescription'] not in given_notgiven:
        given_notgiven[row['PrimaryProbDescription']] = [0, 0]
    if row['PrimaryProbDescription'] == row['DspProbCodeDescription']:
        given_notgiven[row['PrimaryProbDescription']][0] += 1
    else:
        given_notgiven[row['PrimaryProbDescription']][1] += 1


given_notgiven_df = pd.DataFrame.from_dict(given_notgiven, orient='index', columns=['COUNT(correct Dispatch Description)', 'COUNT(wrong Dispatch Description)'])
given_notgiven_df.to_csv('primary_given.csv')


# y_x = Opinion(belief=0.55, disbelief=0.15, uncertainty=0.3, baserate=0.39)
# y_notx = Opinion(belief=0.15, disbelief=0.7, uncertainty=0.15, baserate=0.39)
# x = Opinion(belief=0.48, disbelief=0.22, uncertainty=0.3, baserate=0.4)

# db = DedAbd()
# print("y given x: ", y_x)
# print("y given notx: ", y_notx)
# print("x: ", x)
# print("Deduction: ", db.deduction(y_x, y_notx, x))