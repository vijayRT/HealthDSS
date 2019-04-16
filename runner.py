from opinion import Opinion
from binomialoperators import BinomialOperators
from complex_operators import ComplexOperators
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


given_notgiven_df = pd.DataFrame.from_dict(given_notgiven, orient='index', columns=['correctdsptch', 'wrongdsptch'])
given_notgiven_df.to_csv('primary_given.csv')
primaryopinions = []
W = 2
a = 0.5
for index, row in given_notgiven_df.iterrows():
    r = int(row['correctdsptch'])
    s = int(row['wrongdsptch'])
    t = s + r
    b = r / (W + t)
    d = s / (W + t)
    u = 2 / (W + t)
    primaryopinions.append(Opinion(b, d, u, a))

# y_x = Opinion(belief=0.55, disbelief=0.15, uncertainty=0.3, baserate=0.39)
# y_notx = Opinion(belief=0.15, disbelief=0.7, uncertainty=0.15, baserate=0.39)
# x = Opinion(belief=0.48, disbelief=0.22, uncertainty=0.3, baserate=0.4)

# db = DedAbd()
# print("y given x: ", y_x)
# print("y given notx: ", y_notx)
# print("x: ", x)
# print("Deduction: ", db.deduction(y_x, y_notx, x))