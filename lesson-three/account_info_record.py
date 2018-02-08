from datetime import datetime
import time


def insert_current_account(trade_object, income, expend, receivable, out_account):
    now_date = datetime.now()
    current_time = '{}月{}日'.format(now_date.month, now_date.day)
    with open('current_account.txt', 'a', encoding='utf-8') as f:
        f.write('\n')
        insert_content = '{} {} {} {} {} {}'.format(trade_object, income, expend, receivable, out_account, current_time)
        f.write(insert_content)
    insert_balance_sheet(income, expend, receivable, out_account, current_time)


def insert_balance_sheet(income, expend, receivable, out_account, current_time):
    balance_sheets = load_balance_sheet()
    sheets = ['init_balance_sheet', 0, 0, 0]
    if len(balance_sheets) != 0:
        sheets = balance_sheets[-1].split()
    asset = int(sheets[1]) + income - expend
    liabilities = int(sheets[2]) + out_account - receivable
    net_asset = asset - liabilities
    write_balance_sheet(current_time, asset, liabilities, net_asset)


def load_balance_sheet():
    with open('balance_sheet.txt', 'r', encoding='utf-8') as f:
        balance_sheets = f.readlines()[1:]
    return balance_sheets


def load_current_account():
    with open('current_account.txt', 'r', encoding='utf-8') as f:
        current_accounts = f.readlines()[1:]
    return current_accounts


def write_balance_sheet(current_time, asset, liabilities, net_assets):
    with open('balance_sheet.txt', 'a', encoding='utf-8') as f:
        f.write('\n')
        write_content = '{} {} {} {}'.format(current_time, asset, liabilities, net_assets)
        f.write(write_content)


def select_trade_by_contacts():
    company_name = input('input company name:')
    accounts = load_current_account()
    if len(accounts) == 0:
        print('no trade recode as of now')
        return

    print('交易对象 收入/w 支出/w 应收账款/w 应出账款/w 交易日期')
    i = 0
    for account in accounts:
        if account.split()[0] == company_name:
            i += 1
            print(account.replace('\n', ''))
    if i == 0:
        print('no trade recode with company {}'.format(company_name))


def select_trade_record_of_number():
    count = int(input('how many are you want query for trade record:'))
    accounts = load_current_account()
    if len(accounts) == 0:
        print('no trade recode as of now')
        return
    if len(accounts) < count:
        print('Note: trade recode numbers {} less than input number {}'.format(len(accounts)), count)
    query_accounts = accounts[-count:]
    query_accounts.reverse()
    print('交易对象 收入/w 支出/w 应收账款/w 应出账款/w 交易日期')
    for account in query_accounts:
        print(account.replace('\n', ''))


def select_latest_balance_sheet():
    balance_sheets = load_balance_sheet()
    if len(balance_sheets) == 0:
        print('no balance sheet as of now')
        return
    print('结算日期 资产/w 负债/w 净资产/w')
    print(balance_sheets[-1].replace('\n', ''))


def write_info():
    def check_input(input_value):
        if input_value == 'Q':
            return True
        return False
    print('请按照提示输入指标内容, 输入【Q】结束输入退出.')
    while True:
        trade_object = input('交易对象:')
        if check_input(trade_object):
            break
        income = input('收入/w:')
        if check_input(income):
            break
        expend = input('支出/w:')
        if check_input(expend):
            break
        receivable = input('应收账款/w:')
        if check_input(receivable):
            break
        out_account = input('应出账款/w:')
        if check_input(out_account):
            break
        insert_current_account(trade_object, int(income), int(expend), int(receivable), int(out_account))
        print('正在写入数据,请稍等继续...')
        time.sleep(2)
    print('input finished')


def read_info():
    print('please input number of you query options')
    print('1: query trade record for some company')
    print('2: query trade record of late by by input number')
    print('3: query latest balance sheet')
    print('Q: exit query')
    while True:
        number = input('choice:')
        if number == '1':
            select_trade_by_contacts()
        if number == '2':
            select_trade_record_of_number()
        if number == '3':
            select_latest_balance_sheet()
        if number == "Q":
            break
    print('query finished')


if __name__ == '__main__':
    print('Tip: please input number of your operation')
    while True:
        print('1: write current_account; 2: read some info; 3: exit')
        operation = input("input value:")
        if operation == '1':
            write_info()
        if operation == '2':
            read_info()
        if operation == '3':
            break

