



import csv

from wxpy import *
import  time

def read_info():
    f = open('./data/sample.csv','r')
    reader = csv.DictReader(f)
    return [info for info in reader]

    # xx 同学请于xx 时间参加 xx 课程， 课程地址是xx, 收到请回复，谢谢

#read_info()


def make_msg(raw_info):
    t = '{n}-同学请于{t}时间参加{s}课程，课程地址是{a}。收到请回复，谢谢!'
    return [t.format(n=info['姓名'],t=info['上课时间'],s=info['课程'],a=info['上课地址'])
            for info in raw_info]


def send(msg_list):
    bot = Bot()
    for msg in msg_list:
        fren_name = msg.split('-')[0]
        f = bot.friends().search(fren_name) # list
        if len(f) == 1:
            f[0].send(msg)
        else:
            print(fren_name)
            print('Please check this name')
    time.sleep(3)
    # bot -> bot.find_fren() -> bot.send()
    #  f = bot.friend().search('name')
    #  f.send('msg')
raw_info = read_info()
msg_list = make_msg(raw_info)
send(msg_list)
