# encoding:utf-8

import random

# 读取用户历史成绩
def get_user_score(user_name):
    # 尝试打开文件，没有则创建新文件
    try:
        f = open('user_record.txt','r')
    except IOError:
        f = open('user_record.txt','w')
    finally:
        score_record = {}
        for i in f.readlines():
            data = i.split()
            score_record[data[0]] = [float(k) for k in data[1:]]
        f.close()
        # 判断用户是否为新用户
        if not score_record.get(user_name):
            print '你好 %s，祝你游戏愉快' %user_name
            score_record[user_name] = [0,0]
        else:
            print '欢迎回来 %s,祝你游戏愉快' %user_name
        return score_record

# 猜数字
def guess_number(roundtimes,averagetimes):
    while True:
        goal = random.randint(1,100)
        # 计算用户历史总猜测次数
        totaltimes = roundtimes * averagetimes
        times = 0
        print '猜猜数字是几：1~100\n'
        while True:
            times += 1
            print '第%d次' %times
            while True:
                try:
                    number = int(raw_input())
                except:
                    print '请输入1-100之间的整数~\n'
                else:
                    break
            if goal < number:
                print '太大了'
            elif goal > number:
                print '太小了'
            else:
                print '猜中了,答案就是',goal
                roundtimes += 1
                break
        totaltimes += times
        # 计算用户当前猜测平均次数
        averagetimes = round(float(totaltimes)/roundtimes,2)
        print '你猜中答案一共用了%d次机会\n你一共玩了%d次游戏\n你平均%.2f次猜中答案\n' %(times,roundtimes,averagetimes)
        # 继续游戏判断
        go = raw_input('输入"go"再玩一次，否则退出游戏\n')
        if go == 'go':
            continue
        else:
            print '再见\n'
            break
    # 返回用户成绩（元组）
    return (roundtimes,averagetimes)

# 更新用户成绩
def set_data(score_record):
    with open('user_record.txt','w') as f:
        for i in score_record:
            score_list = [i]+score_record[i]
            f.write(' '.join('%s' %id for id in score_list))
            f.write('\n')

if __name__ == '__main__':
    while True:
        # 防止用户输入空姓名
        try:
            user_name = raw_input('请输入玩家姓名：\n')
            if user_name == '':
                raise TypeError
        except TypeError:
            print '玩家姓名不能为空~'
        else:
            break
    score_record = get_user_score(user_name)
    game_result = guess_number(score_record[user_name][0],score_record[user_name][1])
    score_record[user_name] = [int(game_result[0]),game_result[1]]
    set_data(score_record)