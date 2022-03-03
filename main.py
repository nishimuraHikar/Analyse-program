import analyse

datafile = 'tozuka2.csv'
AnalyzeNumber = 14

# RMS計算
rms = analyse.RMSfunc(analyse.csv2ndarray(datafile, AnalyzeNumber), len(analyse.csv2ndarray(datafile, AnalyzeNumber)))
print(rms)