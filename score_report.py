# -*- coding:utf-8 -*-

# 空列表作为结果存储
answer_report=[]
title_list=[]

# 打开文件并逐行读取到新列表中
with open('report.txt','r') as f:
    total_lst = f.readlines()

# 计算每个学生的总分与平均分
for i in range(0,len(total_lst)):
    lst = total_lst[i].split()
    # 若为第一行
    if i == 0:
        lst.append('总分')
        lst.append('平均分')
        lst.insert(0,'名次')
        # 复制到新列表，作为标题行
        title_list = lst[:]
    else:
        total_score=0
        average_score=0
        # 从第2项开始
        for j in range(1,len(lst)):
            # 计算总成绩
            total_score += int(lst[j])
        # 计算平均成绩并保留两位小数
        average_score=round(float(total_score)/(len(lst)-1),2)
        lst.append(total_score)
        lst.append(average_score)
        # 将学生成绩添加进结果列表中
        answer_report.append(lst)

# 按照平均成绩降序排列
answer_report = sorted(answer_report,key=lambda x:x[-1],reverse=True)

# 计算每一科的平均成绩
subject_average_score=['平均']
for i in range(1,len(lst)):
    subject_total_score = 0
    for j in range(0,len(answer_report)):
        subject_total_score += float(answer_report[j][i])
    s = round(float(subject_total_score)/len(answer_report),2)
    subject_average_score.append(s)
answer_report.insert(0,subject_average_score)

# 低于60分的成绩替换为不及格
for i in range(0,len(answer_report)):
    if i>0:
        l = answer_report[i][1:]
        for j in range(0,len(l)):
            if int(l[j])<60:
                l[j] = '不及格'
        answer_report[i] = answer_report[i][0:1] + l
    # 添加学生名次
    answer_report[i].insert(0,i)

# 给结果列表加上标题行
answer_report.insert(0, title_list)

# 以写入权限打开文档
f = open('answer_report.txt','w')
for i in range(0, len(answer_report)):
    # 格式化并拼接成符串，逐行写入
    f.write(' '.join('%s' %id for id in answer_report[i]))
    f.write('\n')
f.close()