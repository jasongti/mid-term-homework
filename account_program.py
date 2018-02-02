# encoding:utf-8

import datetime

def add_bill():
    i = datetime.datetime.now()
    now_time = '%s-%s-%s' %(i.year,i.month,i.day)
    to_company = raw_input('交易对象：')
    income = raw_input('收入/万：')
    pay = raw_input('支出/万：')
    for_income = raw_input('应收账款/万：')
    for_pay = raw_input('应付账款/万：')
    new_record = [to_company,income,pay,for_income,for_pay,now_time]
    return new_record

def search_from_bill(type,*company):
    with open('bill.txt','r') as f:
        bill = f.readlines()
    if type == 1:
        i = len(bill)
        if i > 10:
            result = bill[0,-10:]
            for k in result:
                print k,
            print
        else:
            print '当前共有%d条记录' %(i-1)
            for k in bill:
                print k,
            print
    elif type == 2:
        company_bill_list = []
        for i in bill:
            if company[0] == i.split()[0]:
                company_bill_list.append(i)
        if len(company_bill_list) > 0:
            company_bill_list.insert(0,bill[0])
            for k in company_bill_list:
                print k,
            print
        else:
            print '暂无与%s的交易记录' %company

def write_in_bill(bill_record):
    with open('bill.txt','a') as f:
        f.write('\n')
        f.write(' '.join(bill_record))

def search_from_balance():
    with open('balance_sheet.txt','r') as f:
        data = f.readlines()
    i = len(data)
    if i > 1:
        latest_balance = data[-1].split()
        print '最新资产：%s\n最新负债：%s万\n最新净资产：%s万\n最后更新时间：%s\n' %(latest_balance[0],latest_balance[1],latest_balance[2],latest_balance[3])
    else:
        print '无记录'

def update_balance(bill_record):
    balance_sheet_date = []
    balance_sheet = []
    add_initial_data = []
    with open('balance_sheet.txt','r') as f:
        for i in f.readlines():
            data = i.split()
            balance_sheet_date.append(data[0])
            balance_sheet.append(data)
    i = datetime.datetime.now()
    if len(balance_sheet) == 1:
        add_initial_data.append('%s-%s-%s' %(i.year, i.month, i.day))
        add_initial_data += [0,0,0]
        balance_sheet.append(add_initial_data)
        balance_sheet_date.append(add_initial_data[0])
    goal_data = balance_sheet[-1][:]
    goal_data[1] = float(goal_data[1]) + float(bill_record[1]) - float(bill_record[2])
    goal_data[2] = float(goal_data[2]) + float(bill_record[4]) - float(bill_record[3])
    goal_data[3] = goal_data[1] - goal_data[2]
    if bill_record[5] in balance_sheet_date:
        balance_sheet[-1] = goal_data
    else:
        goal_data[0] = '%s-%s-%s' %(i.year,i.month,i.day)
        balance_sheet.append(goal_data)
    return balance_sheet

def write_in_balance(balance_sheet):
    with open('balance_sheet.txt','w') as f:
        for i in balance_sheet:
            f.write(' '.join([str(k) for k in i]))
            f.write('\n')
    print '已成功记录\n'

if __name__ == '__main__':
    while True:
        print '1.查账； 2.记账; 3.退出'
        user_choice_mode = input('请选择服务：')
        if user_choice_mode == 1:
            print '查账模式'
            while True:
                print '1.查询最近十笔交易记录\n2.查询与某公司交易往来\n3.查询最近资产负债情况\n4.返回上一级\n'
                user_choice_number = input('请选择服务：')
                if user_choice_number == 1:
                    search_from_bill(1)
                elif user_choice_number == 2:
                    company = raw_input('请输入公司名称：')
                    search_from_bill(2,company)
                elif user_choice_number == 3:
                    search_from_balance()
                elif user_choice_number == 4:
                    break
                else:
                    print '请输入正确的服务编号\n'
                    continue
        elif user_choice_mode == 2:
            print '记账模式'
            new_record = add_bill()
            write_in_bill(new_record)
            write_in_balance(update_balance(new_record))
        elif user_choice_mode == 3:
            print '谢谢使用，再见'
            break
        else:
            print '请输入正确的服务编号\n'
            continue