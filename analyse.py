import pandas as pd
import math

def csv2ndarray(csv, line_num): #csvと列番号を指定
    # csvからndarray型に変換
    csvdata = pd.read_csv(csv, header=0, usecols=[line_num])
    # csvから読んだデータをnumpyの行列に入れる
    array = csvdata.values
    # 配列の平坦化
    data = array.T[0]
    return data

def Meticulous_csv2ndarray(csv, line_num, StartLine, EndLine):
    csvdata = pd.read_csv(csv, header=0, usecols=[line_num])
    SpecificLine = csvdata.loc[StartLine:EndLine]
    array = SpecificLine.values
    data = array.T[0]
    return data

def RMSfunc(data, num): #解析するcsvデータとcsvの行数を指定
    SumSquare = 0.0
    for i in range(num):
        SumSquare += data[i] ** 2
    rms = math.sqrt(SumSquare / num)
    return rms