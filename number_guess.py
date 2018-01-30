# encoding:utf-8

import random

def get_score_report(user_name):
    with open('user_record.txt','r') as f:
        score_record = {}
        for i in f.readlines():
            data = i.split()
            score_record[data[0]] = [float(k) for k in data[1:]]
    if not score_record.get(user_name):
        print '你好 %s，祝你游戏愉快' %user_name
        score_record[user_name] = [0,0]
    else:
        print '欢迎回来 %s,祝你游戏愉快' %user_name
    return score_record

def guess_number(roundtimes,averagetimes):
    while True:
        goal = random.randint(1,100)
        totaltimes = roundtimes * averagetimes
        times = 0
        print '猜猜数字是几：1~100\n'
        while True:
            times += 1
            number = input('第%d次\n' %times)
            if goal < number:
                print '太大了'
            elif goal > number:
                print '太小了'
            else:
                print '猜中了,答案就是',goal
                roundtimes += 1
                break
        totaltimes += times
        averagetimes = round(float(totaltimes)/roundtimes,2)
        print '你猜中答案一共用了%d次机会\n你一共玩了%d次游戏\n你平均%.2f次猜中答案\n' %(times,roundtimes,averagetimes)
        go = raw_input('输入"go"再玩一次，否则退出游戏\n')
        if go == 'go':
            continue
        else:
            print '再见\n'
            break
    return (roundtimes,averagetimes)

def set_data(score_record):
    with open('user_record.txt','w') as f:
        for i in score_record:
            score_list = [i]+score_record[i]
            f.write(' '.join('%s' %id for id in score_list))
            f.write('\n')

if __name__ == '__main__':
    user_name = raw_input('请输入玩家姓名：\n')
    score_record = get_score_report(user_name)
    game_result = guess_number(score_record[user_name][0],score_record[user_name][1])
    score_record[user_name] = [int(game_result[0]),game_result[1]]
    set_data(score_record)