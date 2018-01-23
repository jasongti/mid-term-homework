# coding:utf-8

answer_report=[]
title_list=[]
with open('report.txt','r') as f:
    total_lst = f.readlines()
for i in range(0,len(total_lst)):
    lst = total_lst[i].split()
    if i == 0:
        lst.append('总分')
        lst.append('平均分')
        lst.insert(0,'名次')
        title_list = lst[:]
    else:
        total_score=0
        average_score=0
        for j in range(1,len(lst)):
            total_score += int(lst[j])
        average_score=round(float(total_score)/(len(lst)-1),2)
        lst.append(total_score)
        lst.append(average_score)
        answer_report.append(lst)
answer_report = sorted(answer_report,key=lambda x:x[-1],reverse=True)
for i in range(0,len(answer_report)):
    l = answer_report[i][1:]
    for j in range(0,len(l)):
        if int(l[j])<60:
            l[j] = '不及格'
    answer_report[i] = answer_report[i][0:1] + l
    answer_report[i].insert(0,i+1)
answer_report.insert(0, title_list)

f = open('answer_report.txt','w')
for i in range(0, len(answer_report)):
    f.write('  '.join('%s' %id for id in answer_report[i]))
    f.write('\n')
f.close()