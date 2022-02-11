import pandas as pd
import math
import matplotlib.pyplot as plt

def csv2ndarray(csv, line_num): #csvと列番号を指定
    # csvからndarray型に変換
    csvdata = pd.read_csv(csv, header=0, usecols=[line_num])
    # 100行間隔で間引き
    # cut_csv = csvdata[1::100]
    # csvから読んだデータをnumpyの行列に入れる
    array = csvdata.values
    # print(array)
    # 配列の平坦化
    data = array.T[0]
    # print(data)
    return data

def RMSfunc(data, num):
    SumSquare = 0.0
    for i in range(num):
        SumSquare += data[i] ** 2
    rms = math.sqrt(SumSquare / num)
    return rms