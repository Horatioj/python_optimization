#coding=utf-8

import pandas as pd

sData = pd.DataFrame(pd.read_excel('testData.xlsx'))
meanRow = sData[["数学","英语","计算机"]].mean()

sData["平均分"] = round((sData["数学"]+sData["英语"]+sData["计算机"])/3.0, 2)
sData = sData.sort_values("学号", ascending=True)
print("*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*")
print("原式：")
print(sData, "\n")

print("*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*")
print("按平均分打印：")
print(sData.sort_values("平均分", ascending=False), "\n")

print("*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*")
print("按数学成绩打印：")
sData = sData.sort_values("数学", ascending=False)
print(sData.iloc[0:7, 0:3])
print(sData[0:7][["数学"]].describe(),"\n")
count1 = count2 = count3 = count4 = count5 = 0
for x in sData["数学"]:
    if x < 60:
        count1 += 1
    if((x >= 60) & (x < 70)):
        count2 += 1
    if((x >= 70) & (x < 80)):
        count3 += 1
    if((x >= 80) & (x < 90)):
        count4 += 1
    if((x >= 90) & (x < 100)):
        count5 += 1
print("不及格人数：", count1, "人；60~69分人数：", count2, "人；70~79分人数：", count3, "人；80~89分人数", count4,
      "人；90分以上人数：", count5, "人；\n")

print("*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*")
print("按英语成绩打印：")
sData = sData.sort_values("英语", ascending=False)
print(sData[0:7][["学号","姓名", "英语"]])
print(sData[0:7][["英语"]].describe(),"\n")
count1 = count2 = count3 = count4 = count5 = 0
for x in sData["英语"]:
    if x < 60:
        count1 += 1
    if((x >= 60) & (x < 70)):
        count2 += 1
    if((x >= 70) & (x < 80)):
        count3 += 1
    if((x >= 80) & (x < 90)):
        count4 += 1
    if((x >= 90) & (x < 100)):
        count5 += 1
print("不及格人数：", count1, "人；60~69分人数：", count2, "人；70~79分人数：", count3, "人；80~89分人数", count4,
      "人；90分以上人数：", count5, "人；\n")

print("*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*\n")
print("按计算机成绩打印：")
sData = sData.sort_values("计算机", ascending=False)
print(sData[0:7][["学号","姓名","计算机"]])
print(sData[0:7][["计算机"]].describe(), "\n")
count1 = count2 = count3 = count4 = count5 = 0
for x in sData["计算机"]:
    if x < 60:
        count1 += 1
    if((x >= 60) & (x < 70)):
        count2 += 1
    if((x >= 70) & (x < 80)):
        count3 += 1
    if((x >= 80) & (x < 90)):
        count4 += 1
    if((x >= 90) & (x < 100)):
        count5 += 1
print("不及格人数：", count1, "人；60~69分人数：", count2, "人；70~79分人数：", count3, "人；80~89分人数", count4,
      "人；90分以上人数：", count5, "人；\n")
print("*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*")

dict={"1":"王放",
      "2":"张强",
      "3":"李浩",
      "4":"黄鹏兵",
      "5":"李浩",
      "6":"陈利风",
      "7":"尚晓"}

#dict = sData.to_dict(orient='index')
sData = sData.sort_values("学号", ascending=True)
#continuing = True
#while continuing:
determine = int(input("请选择查询姓名(1)或者是学号(2):"))
if(determine == 1):
    name = input("请输入需要查询的姓名：")
    if name in dict.values():
        for a in range(0, len(dict)):
            if list(dict.values())[a]==name:
                index = map(int, list(dict.keys())[a])
                for b in index:
                    print(sData[(b-1):b])
    else:
        print("查无此人，请核对需要查询的姓名！")
if(determine == 2):
    id = int(input("请输入需要查询的学号："))
    if(id<=7):
        print(sData[(id-1):id])
    else:
        print("查无此人，请核对需要查询的学号！")
    '''
    ask_ = input("Would you like to continue your input?(yes/no)")
    if ask_ == 'no':
        continuing = False
        print("Thank you for using \^o^/!")'''