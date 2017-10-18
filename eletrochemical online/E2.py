#coding=utf-8
import csv
import web
import re
import math
import sqlite3

import xlrd
import string
import numpy as np
import matplotlib.pyplot as plt
import sys
import os


urls = ('/','homepage',
        '/homepage.html','homepage',
        '/homepageEn.html','homepageEn',
        "/dhxGCD.html","dhxGCD",
        "/dhxRATE.html","dhxRATE",
        "/dhxCV.html","dhxCV",
        "/dhxEIS.html","dhxEIS",
        )


render = web.template.render('templates')

class baseweb():  #替代POST和GET方法，捕捉详细异常
    def myGET(self):
        return "baseweb get"
    def myPOST(self):
        return "baseweb post" 
    def GET(self):
        v=""
        try:
            v=self.myGET()
        except Exception,e:
            return "erro %s"%(e)
        return v
    def POST(self):
        v=""
        try:
            v=self.myPOST()
        except Exception,e:
            return "erro %s"%(e)
        return v

def reInitiateGlobal():  #初始化所有变量
    global weight,xList,yList,table,data,startNum,ValleyTime,Valley,PeakNum,PeakTime,Peak,endNum,\
            ReValley,LastPeak,LastPeakTime,LastPeakNum,LastValley,LaststartNum,LastValleyTime,filePath,\
            weight,fCurrent,density,newRow,fileIndex,pathList,pathVaList,openIndex,colorList,\
            densityList,densityVaList,capacityList,qualityRow,noticeRow,startNum,endNum,fScanrate,\
            figPath,pathList,xy
    pathList=['']
    figPath=''
    xy = []
    xList = ['']
    yList = ['']
    table = []
    data = [] #列表初始化不能连等，原因未知
    startNum=ValleyTime=Valley=PeakNum=PeakTime=Peak=endNum=ReValley=LastPeak=LastPeakTime=LastPeakNum=LastValley=LaststartNum=LastValleyTime= ''
    filePath = ""
    fCurrent = ''
    density = 0
    weight = 0
    newRow = 2
    fileIndex = 1
    pathVaList = ['',''] #文件路径的值列表，用于后续引用
    openIndex = 1 #用于打开文件的索引
    colorList = ['','black','red','blue','green','Yellow','grey','orange','pink']
    densityList = ['']
    densityVaList = []
    capacityList = []
    qualityRow = 2
    noticeRow = 3
    startNum = 0
    endNum = 0
    fScanrate = ''

def notNum(value): #定位数据起始位置
    try:
        value + 1
    except TypeError:
        return True
    else:
        return False

def dealEIS(table):
    global startNum,endNum
    Ns = 15
    while notNum(table.cell(Ns,2).value):
        Ns +=1
    startNum = Ns
    endNum = table.nrows - 1
    

def dealCV(table):
    global startNum,endNum
    Ns = 29
    while notNum(table.cell(Ns,0).value):
        Ns +=1
    Ns +=1
    while (table.cell(Ns,0).value)!=0:
        Ns +=1
    startNum = Ns
    Ns +=1
    while (table.cell(Ns,0).value)!=0:
        Ns +=1
    endNum = Ns
    
def dealGCDandRate(table): #处理GCD和Rate的原始数据
    global startNum,ValleyTime,Valley,PeakNum,PeakTime,Peak,endNum,ReValley,LastPeak,LastPeakTime,LastPeakNum,LastValleyTime,LastValley,LaststartNum
    Ns = 20
    while notNum(table.cell(Ns,0).value):
        Ns +=1
    N1 = Ns
    N2 = N1 + 1
    Xn1 = table.cell(N1,1).value
    Xn2 = table.cell(N2,1).value #定位数据起始位置
    while Xn2 <= Xn1:
        N2 += 1
        Xn1 = Xn2
        Xn2 = table.cell(N2,1).value #遍历并比较递减数据
    startNum = N2 #第一个谷值的行数
    Valley = table.cell(startNum,1).value #第一个谷值
    ValleyTime = table.cell(startNum,0).value #第一个谷值对应的时间

    N1 = N2
    N2 += 1
    Xn1 = Xn2
    Xn2 = table.cell(N2,1).value #重新初始化
    while Xn2 >= Xn1:
        N2 += 1
        Xn1 = Xn2
        Xn2 = table.cell(N2,1).value #遍历并比较递增数据
    PeakNum = N2 - 1 #第一个峰值的行数
    Peak = table.cell(PeakNum,1).value #第一个峰值
    PeakTime = table.cell(PeakNum,0).value  #第一个峰值对应的时间

    N1 = N2
    N2 = N2 + 1
    Xn1 = Xn2
    Xn2 = table.cell(N2,1).value #重新初始化
    while Xn2 <= Xn1:
        N2 += 1
        Xn1 = Xn2
        Xn2 = table.cell(N2,1).value #遍历并比较递减数据
    N2 -= 1
    Xn2 = table.cell(N2,1).value
    while Xn2 == table.cell((N2-1),1).value:
        N2 -= 1
        Xn2 = table.cell(N2,1).value #对重复谷值数据的修正
    endNum = N2
    ReValley = table.cell(endNum,1).value #第二个谷值的定位

    nrows = table.nrows
    N1 = nrows - 1
    N2 = N1 - 1
    Xn1 = table.cell(N1,1).value
    Xn2 = table.cell(N2,1).value #从最后一行定位，准备逆向检索
    while Xn2 <= Xn1:
        N2 -= 1
        Xn1 = Xn2
        Xn2 = table.cell(N2,1).value #逆向遍历，去除冗余数据

    N1 = N2
    N2 -= 1
    Xn1 = table.cell(N1,1).value
    Xn2 = table.cell(N2,1).value
    while Xn2 >= Xn1:
        N2 -= 1
        Xn1 = Xn2
        Xn2 = table.cell(N2,1).value
    LastPeakNum = N2 + 1
    LastPeak = table.cell(LastPeakNum,1).value
    LastPeakTime = table.cell(LastPeakNum,0).value #获得最后一个峰值

    N1 = N2
    N2 -= 1
    Xn1 = table.cell(N1,1).value
    Xn2 = table.cell(N2,1).value
    while Xn2 <= Xn1:
        N2 -= 1
        Xn1 = Xn2
        Xn2 = table.cell(N2,1).value
    N2 += 1
    Xn2 = table.cell(N2,1).value
    if Xn2 != table.cell((N2 + 1),1).value:
        LaststartNum = N2 + 1
        LastValley = table.cell(LaststartNum,1).value
        LastValleyTime = table.cell(LaststartNum,0).value
    else:
        while Xn2 == table.cell((N2 + 1),1).value:
            N2 += 1
            Xn2 = Xn2 = table.cell(N2,1).value
        LaststartNum = N2 + 1
        LastValley = table.cell(LaststartNum,1).value
        LastValleyTime = table.cell(LaststartNum,0).value #获得最后一个谷值

def getCurrent(table): 
    global fCurrent
    fCurrent=''
    current = str(table.cell(8,0).value)
    fil = '0123456789' + '.'
    for c in current:
       if c in fil:
            fCurrent += c     #读取电流强度

def getScanrate(table):
    global fScanrate
    fScanrate = ''
    scanrate = str(table.cell(11,0).value)
    fil = '0123456789' + '.'
    for c in scanrate:
       if c in fil:
            fScanrate += c     #读取扫描电压
    fScanrate = float(fScanrate) * 1000  #单位转换

def calDensityA():
    global density,densityList,densityVaList,weight
    density = float(fCurrent)/weight * 1000 #计算电流密度 A/g
    densityVaList.append(int(density))
    densityList.append(str(density)+'A·g-1')

def calResult():
    global capacityList
    dischTime = float(PeakTime) - float(ValleyTime)
    dischVol = -(float(Valley) + float(Peak))
    capacity = density * dischTime / dischVol
    capacityList.append(capacity)

def formData(table):
    x = []
    y = []
    global endNum,startNum,xList,yList,windowIndex,weight
    span = endNum - startNum
    index = startNum
    for i in range(1,span+2):
        x.append(float(table.cell(index,0).value)-float(table.cell(startNum,0).value))
        y.append(float(table.cell(index,1).value))
        index+=1
    xList.append(x)
    yList.append(y)

def formCVData(table):
    x = []
    y = []
    global endNum,startNum,xList,yList,windowIndex,weight
    span = endNum - startNum
    index = startNum
    for i in range(1,span+2):
        x.append(float(table.cell(index,0).value)-float(table.cell(startNum,0).value))
        y.append(float(table.cell(index,1).value)/weight * 1000)
        index+=1
    xList.append(x)
    yList.append(y)

def formEISData(table):
    x = []
    y = []
    global endNum,startNum,xList,yList,windowIndex,weight
    span = endNum - startNum
    index = startNum
    for i in range(1,span+2):
        x.append(float(table.cell(index,1).value)-float(table.cell(startNum,0).value))
        y.append(-(float(table.cell(index,2).value)))
        index+=1
    xList.append(x)
    yList.append(y)

"""def formEISData(table):
    global endNum,startNum,xList,yList,windowIndex,weight,xy
    span = endNum - startNum
    index = startNum
    for i in range(1,span+2):
        x = float(table.cell(index,1).value)-float(table.cell(startNum,0).value)
        y = -(float(table.cell(index,2).value))
        index+=1
        xy.append([x,y])"""
    


def formGcdGraphic():
    global colorList,openIndex,xList,yList,densityList
    reload(sys)
    sys.setdefaultencoding('utf-8')
    plt.plot(xList[openIndex],yList[openIndex],label=densityList[openIndex],color=colorList[openIndex],linewidth=2)
    plt.legend()
    plt.xlabel(u"Time / s",fontsize=18)
    plt.ylabel(u'Potential / V',fontsize=18)

def formRateGraphic():
    global densityVaList,capacityList
    reload(sys)
    sys.setdefaultencoding('utf-8')
    plt.plot(densityVaList,capacityList,label='line1',color='black',linewidth=2)
    plt.scatter(densityVaList,capacityList,label= 'scatter1',marker='o',color='black',s=50)
    plt.xlabel(u"Current Density / A·g-1",fontsize=18)
    plt.ylabel(u'Specific Capacitance / F·g-1',fontsize=18)

def formCvGraphic():
    global colorList,openIndex,xList,yList,fScanrate
    reload(sys)
    sys.setdefaultencoding('utf-8')
    plt.plot(xList[openIndex],yList[openIndex],label= str(int(fScanrate)) + u'mV/s',color=colorList[openIndex],linewidth=2)
    plt.legend()
    plt.xlabel(u"Potential / V",fontsize=18)
    plt.ylabel(u'Current Density / A·g-1',fontsize=18)

def formEisGraphic():
    global colorList,openIndex,xList,yList,fScanrate
    reload(sys)
    sys.setdefaultencoding('utf-8')
    plt.plot(xList[openIndex],yList[openIndex],label= 'line1',color=colorList[openIndex],linewidth=2)
    plt.scatter(xList[openIndex],yList[openIndex],label= 'scatter1',marker='^',color=colorList[openIndex],s=50)
    plt.xlabel(u"Z' / ohm",fontsize=18)
    plt.ylabel('-Z\'\' / ohm',fontsize=18)  
       
def saveGraphic(fileName):
    figPath=u'static/images/' + fileName
    if os.path.exists(figPath):
        os.remove(figPath)
    plt.savefig(figPath)
    plt.clf()   

class homepage(baseweb):
    def myGET(self):
        title=""
        return render.homepage(title)

class homepageEn(baseweb):
    def myGET(self):
        title=""
        return render.homepageEn(title)

class dhxGCD(baseweb):
    def myGET(self):
        W1,F1,F2,F3,F4,F5,F6,F7,F8,answer1='','','','','','','','','',''
        reInitiateGlobal()
        return render.dhxGCD(W1,F1,F2,F3,F4,F5,F6,F7,F8,answer1)
    def myPOST(self):
        global fCurrent,startNum,ValleyTime,Valley,PeakNum,PeakTime,Peak,endNum,ReValley,LastPeak,\
               LastPeakTime,LastPeakNum,LastValleyTime,LastValley,LaststartNum,density,densityList,\
               densityVaList,weight,colorList,openIndex,xList,yList,pathList
        reInitiateGlobal()
        data=web.input()
        weight = float(data['W1'])
        pathList=['',data['F1'],data['F2'],data['F3'],data['F4'],data['F5'],data['F6'],data['F7'],data['F8']]
        for openIndex in range(1,9):
            if pathList[openIndex]=='':
                break
            path=u'电化学数据'+'/'+ pathList[openIndex]
            workbook = xlrd.open_workbook(path)
            table = workbook.sheets()[0]
            getCurrent(table)
            calDensityA()
            dealGCDandRate(table)
            formData(table)
            formGcdGraphic()
        saveGraphic('gcd.png')


        return render.dhxGCD('','','','','','','','','','')

class dhxRATE(baseweb):
    def myGET(self):
        W1,F1,F2,F3,F4,F5,F6,F7,F8,answer1='','','','','','','','','',''
        reInitiateGlobal()
        return render.dhxRATE(W1,F1,F2,F3,F4,F5,F6,F7,F8,answer1)
    def myPOST(self):
        global fCurrent,startNum,ValleyTime,Valley,PeakNum,PeakTime,Peak,endNum,ReValley,LastPeak,\
               LastPeakTime,LastPeakNum,LastValleyTime,LastValley,LaststartNum,density,densityList,\
               densityVaList,weight,colorList,openIndex,xList,yList,capacityList,pathList
        reInitiateGlobal()
        data=web.input()
        weight = float(data['W1'])
        pathList=['',data['F1'],data['F2'],data['F3'],data['F4'],data['F5'],data['F6'],data['F7'],data['F8']]
        for openIndex in range(1,9):
            if pathList[openIndex]=='':
                break
            path=u'电化学数据'+'/'+ pathList[openIndex]
            workbook = xlrd.open_workbook(path)
            table = workbook.sheets()[0]
            getCurrent(table)
            calDensityA()
            dealGCDandRate(table)
            calResult()
        formRateGraphic()
        saveGraphic('rate.png')
        
        
        return render.dhxRATE('','','','','','','','','','')

class dhxCV(baseweb):
    def myGET(self):
        W1,F1,F2,F3,F4,F5,F6,F7,F8,answer1='','','','','','','','','',''
        reInitiateGlobal()
        return render.dhxCV(W1,F1,F2,F3,F4,F5,F6,F7,F8,answer1)
    def myPOST(self):
        global fCurrent,startNum,ValleyTime,Valley,PeakNum,PeakTime,Peak,endNum,ReValley,LastPeak,\
               LastPeakTime,LastPeakNum,LastValleyTime,LastValley,LaststartNum,density,densityList,\
               densityVaList,weight,colorList,openIndex,xList,yList,capacityList,fScanrate,pathList
        reInitiateGlobal()
        data=web.input()
        weight = float(data['W1'])
        pathList=['',data['F1'],data['F2'],data['F3'],data['F4'],data['F5'],data['F6'],data['F7'],data['F8']]
        for openIndex in range(1,9):
            if pathList[openIndex]=='':
                break
            path=u'电化学数据'+'/'+ pathList[openIndex]
            workbook = xlrd.open_workbook(path)
            table = workbook.sheets()[0]
            getScanrate(table)
            dealCV(table)
            formCVData(table)
            formCvGraphic()
        saveGraphic('cv.png')

        return render.dhxCV('','','','','','','','','','')

"""class dhxEIS(baseweb):
    def myGET(self):
        F1,answer1='',''
        reInitiateGlobal()
        return render.dhxEIS(F1,answer1)
    def myPOST(self):
        global fCurrent,startNum,ValleyTime,Valley,PeakNum,PeakTime,Peak,endNum,ReValley,LastPeak,\
               LastPeakTime,LastPeakNum,LastValleyTime,LastValley,LaststartNum,density,densityList,\
               densityVaList,weight,colorList,openIndex,xList,yList,capacityList,fScanrate,pathList
        reInitiateGlobal()
        data=web.input()
        pathList=['',data['F1']]
        path=u'电化学数据'+'/'+ pathList[1]
        workbook = xlrd.open_workbook(path)
        table = workbook.sheets()[0]
        dealEIS(table)
        formEISData(table)
        formEisGraphic()
        saveGraphic('EIS.png')

        return render.dhxEIS('','')"""

class dhxEIS(baseweb):
    def myGET(self):
        F1,answer1='',''
        reInitiateGlobal()
        return render.dhxEIS(F1,answer1)
    def myPOST(self):
        global fCurrent,startNum,ValleyTime,Valley,PeakNum,PeakTime,Peak,endNum,ReValley,LastPeak,\
               LastPeakTime,LastPeakNum,LastValleyTime,LastValley,LaststartNum,density,densityList,\
               densityVaList,weight,colorList,openIndex,xList,yList,capacityList,fScanrate,pathList
        reInitiateGlobal()
        data=web.input()
        pathList=['',data['F1']]
        path=u'电化学数据'+'/'+ pathList[1]
        workbook = xlrd.open_workbook(path)
        table = workbook.sheets()[0]
        dealEIS(table)
        formEISData(table)
        formEisGraphic()
        saveGraphic('EIS.png')

        return render.dhxEIS('',xList) 

#全局变量
pathList=['']
figPath=''
xy = []
xList = ['']
yList = ['']
table = []
data = [] #列表初始化不能连等，原因未知
startNum=ValleyTime=Valley=PeakNum=PeakTime=Peak=endNum=ReValley=LastPeak=LastPeakTime=LastPeakNum=LastValley=LaststartNum=LastValleyTime= ''
filePath = ""
fCurrent = ''
density = 0
weight = 0
newRow = 2
fileIndex = 1
pathVaList = ['',''] #文件路径的值列表，用于后续引用
openIndex = 1 #用于打开文件的索引
colorList = ['','black','red','blue','green','Yellow','grey','orange','pink']
densityList = ['']
densityVaList = []
capacityList = []
qualityRow = 2
noticeRow = 3
startNum = 0
endNum = 0
fScanrate = ''

    
if __name__ == "__main__":
    
   
    app = web.application(urls, globals())
    web.config.debug = False
    app.run()    

