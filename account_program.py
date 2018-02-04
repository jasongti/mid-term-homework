# encoding:utf-8

import datetime

# 新增流水账
def add_bill():
    # 获取当前时间
    now = datetime.datetime.now()
    now_time = '%s-%s-%s' %(now.year,now.month,now.day)
    to_company = raw_input('交易对象：')
    while True:
        try:
            income = input('收入/万：')
            pay = input('支出/万：')
            for_income = input('应收账款/万：')
            for_pay = input('应付账款/万：')
        except:
            print '请输入正确的信息~'
            continue
        else:
            new_record = [to_company,income,pay,for_income,for_pay,now_time]
            break
    return [str(i) for i in new_record]

# 查询流水账，可按最近记录查询、公司名称查询
def search_from_bill(type,*company):
    with open('bill.txt','a+') as f:
        f.seek(0)
        bill = f.readlines()
        # 初始化文档
        if len(bill) == 0:
            f.write('交易对象 收入/万 支出/万 应收账款/万 应付账款/万')
    # 模式1，按最近记录查询
    if type == 1:
        # 交易记录大于10条
        if len(bill) > 10:
            result = bill[0,-10:]
            for k in result:
                print k,
            print
        # 无记录
        elif len(bill) <= 1:
            print '暂无交易记录'
        # 不足10条时显示全部
        else:
            print '当前共有%d条记录' %(len(bill)-1)
            for k in bill:
                print k,
            print
    # 模式2，按公司名称查询
    elif type == 2:
        company_bill_list = []
        for i in bill:
            if company[0] == i.split()[0]:
                company_bill_list.append(i)
        # 有历史记录
        if len(company_bill_list) > 0:
            company_bill_list.insert(0,bill[0])
            for k in company_bill_list:
                print k,
            print '\n总计：%d条交易记录\n' %(len(company_bill_list)-1)
        # 无历史记录
        else:
            print '暂无与%s的交易记录' %company

# 写入流水账文档
def write_in_bill(bill_record):
    with open('bill.txt','a+') as f:
        f.seek(0)
        bill = f.readlines()
        # 初始化文档
        if len(bill) == 0:
            f.write('交易对象 收入/万 支出/万 应收账款/万 应付账款/万')
        f.write('\n')
        f.write(' '.join(bill_record))

# 查询资产负债表
def search_from_balance():
    with open('balance_sheet.txt','a+') as f:
        f.seek(0)
        balance_data = f.readlines()
        # 初始化文档
        if len(balance_data) == 0:
            f.write('结算日期 资产/w 负债/w 净资产/w\n')
    # 有历史记录
    if len(balance_data) > 1:
        # 取最新一条数据
        latest_balance = balance_data[-1].split()
        print '最新资产：%s\n最新负债：%s万\n最新净资产：%s万\n最后更新时间：%s\n' %(latest_balance[1],latest_balance[2],latest_balance[3],latest_balance[0])
    # 无历史记录
    else:
        print '无记录'

# 更新资产负债表
def update_balance(bill_record):
    balance_sheet_date = []
    balance_sheet = []
    add_initial_data = []
    now = datetime.datetime.now()
    with open('balance_sheet.txt','a+') as f:
        f.seek(0)
        for i in f.readlines():
            data = i.split()
            # 将结算日期与对应的数据，按照相同顺序一一对应，分别存储在两个list中
            balance_sheet_date.append(data[0])
            balance_sheet.append(data)
    # 初始化文档
    while len(balance_sheet) == 0:
        balance_sheet.append(['结算日期', '资产/w', '负债/w', '净资产/w'])
    if len(balance_sheet) == 1:
        add_initial_data.append('%s-%s-%s' % (now.year, now.month, now.day))
        add_initial_data += [0, 0, 0]
        balance_sheet.append(add_initial_data)
        balance_sheet_date.append(add_initial_data[0])
    # 取最新一条记录
    goal_data = balance_sheet[-1][:]
    goal_data[1] = float(goal_data[1]) + float(bill_record[1]) - float(bill_record[2])
    goal_data[2] = float(goal_data[2]) + float(bill_record[4]) - float(bill_record[3])
    goal_data[3] = goal_data[1] - goal_data[2]
    # 当天已有更新，更新记录
    if bill_record[5] in balance_sheet_date:
        balance_sheet[-1] = goal_data
    # 当天无更新，新增记录
    else:
        goal_data[0] = '%s-%s-%s' %(now.year,now.month,now.day)
        balance_sheet.append(goal_data)
    return balance_sheet

# 写入资产负债文档
def write_in_balance(balance_sheet):
    with open('balance_sheet.txt','w') as f:
        for i in balance_sheet:
            f.write(' '.join([str(k) for k in i]))
            f.write('\n')
    return 0

if __name__ == '__main__':
    while True:
        print '1.查账； 2.记账; 3.退出'
        try:
            user_choice_mode = input('请选择服务：')
        except:
            print '请输入正确的服务编号~'
            continue
        else:
            if user_choice_mode == 1:
                print '查账模式'
                while True:
                    print '1.查询最近十笔交易记录\n2.查询与某公司交易往来\n3.查询最近资产负债情况\n4.返回上一级\n'
                    try:
                        user_choice_number = input('请选择服务：')
                    except:
                        print '请输入正确的服务编号~'
                        continue
                    else:
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
                # 记账成功显示最新信息
                if write_in_balance(update_balance(new_record)) == 0:
                    print '\n交易已成功记录'
                    search_from_balance()
                else:
                    print '记录交易失败'
            elif user_choice_mode == 3:
                print '谢谢使用，再见'
                break
            else:
                print '请输入正确的服务编号\n'
                continue