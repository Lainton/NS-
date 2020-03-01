import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

#数据文件保存位置
data_file_path = '/Users/ansel/Documents/matlabFile/rmbData'
#读取的数据列
col = ['d10','d15','d20','d25','d35','d45','d50']

#画布大小
plt.rcParams["figure.figsize"] = [12, 6]


def readFromCSV(path):
    """读取csv文件"""
    file_data = pd.read_csv(path, index_col='date', header=0)
    # file_data = pd.read_csv(path, header=0)
    return file_data


def writeToCSV(lineData):
    """写入一行记录"""
    try:
        with open(data_file_path, 'a') as file:
            file.write(lineData) 
        return True
    except:
        return False


def updateCSV():
    """获取数据并更新记录"""
    data = input("输入d10,d15,d20,d25,d35,d45,d50\n")
    date = datetime.date.today()
    data = '\n' + date.__str__() + ',' + data
    writeToCSV(data)


def dnumberMatrix(l, s, t):
    """将列表中的字符串替换字符"""
    return [int(x.replace(s, t)) for x in l]


def getD2Rrate(df):
    """获取美元与人民币比例"""
    l = dnumberMatrix(col, 'd', '')
    return df[col].div(l, axis='columns', level=None, fill_value=None) 


def drawBar(dfbar):
    """绘制 各个点卡的价格/dollar 的直方图"""
    #柱状图
    ax = dfbar.plot.bar()
    for p in ax.patches:
        val = "{:.2f}".format(p.get_height())
        ax.annotate(val, (p.get_x() * 1.005, p.get_height()+0.2), rotation=70)

    # 设置画
    plt.xlabel('date')  #x轴说明
    plt.ylabel('1dollar:xRMB')   #y轴说明
    plt.yticks(np.arange(0,10,0.3)) #y轴刻度
    plt.xticks(rotation=70) #x轴刻度旋转70°
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


def drawLine(dfbar):
    #线条图
    ax = dfbar.plot(figsize=(5,6), grid=True)

    # 设置画
    plt.xlabel('date')  #x轴说明
    plt.ylabel('RMB')   #y轴说明
    plt.xticks(rotation=70, fontsize=6) #x轴刻度旋转70°
    # plt.yticks(np.arange(6, 8,0.2))
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    #绘图
    plt.show()  


def draw(df):
    """画图"""
    drawBar(df)
    drawLine(df)


def command(str):
    if str == 'i':
        updateCSV() 
    elif str == 'p':
        data = readFromCSV(data_file_path)
        data = getD2Rrate(data)
        draw(data)
    elif str == 'q':
        exit()
    else:
        return
    

def main():
    while(True):
        operation = input("输入命令: i--inputData\tp--picture\tq--quit\n")
        command(operation)


main()