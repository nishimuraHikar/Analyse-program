import analyse

datafile = 'x_data.csv'

# RMS計算
rms = analyse.RMSfunc(analyse.csv2ndarray(datafile, 3), len(analyse.csv2ndarray(datafile, 3)))
print(rms)