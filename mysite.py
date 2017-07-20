# -*- coding: utf-8 -*-
"""
Created on Mon Jul 03 22:12:56 2017

@author: touristlee

TO:Don't worry,be happy!
"""

import web
import pandas as pd
import numpy as np
#读取数据
df = pd.read_csv('small_user.csv',encoding='utf-8')

#随机生成一个省份列表
def get_province(x):
    youlist = []
    for i in x:
        maplist = [u'北京',u'天津',u'上海',u'重庆',u'河北',u'山西',u'辽宁',u'吉林',u'黑龙江',u'江苏',u'浙江',u'安徽',u'福建',u'江西',u'山东',u'河南',u'湖北',u'湖南',u'广东',u'海南',u'四川',u'贵州',u'云南',u'陕西',u'甘肃',u'青海',u'台湾',u'内蒙古',u'广西',u'西藏',u'宁夏',u'新疆',u'香港',u'澳门']  
        youlist.append(maplist[i])
    return youlist
#切割字符串
def format_time(x):
    return str(x).split(' ')[0]


urls=('/','index')

render=web.template.render('templates/')

class index:
    def GET(self):
        web.header('Content-Type','text/html;charset=utf-8')
        df = pd.read_csv('small_user.csv',encoding='utf-8')
        df = df[['user_id','item_id','behavior_type','item_category','time']]
        df['province'] = get_province(np.random.randint(0,34,len(df)))
        df['time'] = df['time'].map(format_time)
        df.columns=['uid','itemid','behavior','itemcagegory','time','province']
        df['time']=df['time'].astype('datetime64')
        df2=df[df['behavior']==3]
        df2=df2.drop_duplicates('uid')
        tmp=df2.groupby('province').uid.count()
        return render.index(tmp)

app=web.application(urls,globals())

if __name__ == '__main__':
#    df = pd.read_csv('small_user.csv',encoding='utf-8')
#    df = df[['user_id','item_id','behavior_type','item_category','time']]
#    df['province'] = get_province(np.random.randint(0,33,len(df)))
#    df['time'] = df['time'].map(format_time)
#    df.columns=['uid','itemid','behavior','itemcagegory','time','province']
#    df['time']=df['time'].astype('datetime64')
#    df2=df[df['behavior']==3]
#    df2=df2.drop_duplicates('uid')
#    tmp=df2.groupby('province').uid.count()
    app.run()




