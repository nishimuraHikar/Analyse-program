import analyse

datafile = 'tozuka2.csv'
AnalyzeNumber = 29

data = analyse.csv2ndarray(datafile, AnalyzeNumber)

# RMS計算
rms = analyse.RMSfunc(data, len(data))
print(rms)