# -*- coding:utf-8 -*-

answer_report=[]   #空列表作为结果存储
title_list=[]

with open('report.txt','r') as f:
    total_lst = f.readlines()   #打开文件并逐行读取到新列表中

for i in range(0,len(total_lst)):
    lst = total_lst[i].split()    #取每一行，拆分为列表
    if i == 0:  #若为第一行
        lst.append('总分')
        lst.append('平均分')       #则在行尾加上"总分"与"平均分"项
        lst.insert(0,'名次')      #在行首加上"名次"项
        title_list = lst[:]     #复制到新列表，作为标题行
    else:
        total_score=0
        average_score=0
        for j in range(1,len(lst)):     #从第2项开始
            total_score += int(lst[j])      #计算总成绩
        average_score=round(float(total_score)/(len(lst)-1),2)      #计算平均分并保留两位小数
        lst.append(total_score)     #在行尾添加总成绩
        lst.append(average_score)       #在行尾添加平均成绩
        answer_report.append(lst)       #将学生成绩添加进结果列表中

answer_report = sorted(answer_report,key=lambda x:x[-1],reverse=True)       #按照平均成绩降序排列

for i in range(0,len(answer_report)):
    l = answer_report[i][1:]    #取出每一个学生的成绩项
    for j in range(0,len(l)):
        if int(l[j])<60:
            l[j] = '不及格'        #低于60分的成绩替换为不及格
    answer_report[i] = answer_report[i][0:1] + l    #合并姓名项和成绩项
    answer_report[i].insert(0,i+1)      #添加学生名次

answer_report.insert(0, title_list)     #给结果列表加上标题行

f = open('answer_report.txt','w')       #以写入权限打开文档
for i in range(0, len(answer_report)):
    f.write('  '.join('%s' %id for id in answer_report[i]))     #格式化并拼接成符串，逐行写入
    f.write('\n')       #行尾换行
f.close()       #关闭文件