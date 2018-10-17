
# coding: utf-8

# ##date 日期函数
# http://www.runoob.com/python/python-date-time.html
# https://docs.python.org/3/library/datetime.html#module-datetime

import time

import calendar


import datetime
from calendar import monthrange



def rangeDate(begin,end):
    """日期范围遍历 ,接受两个date类型参数, 含begin，end两天 
        begin = datetime.date(2018,2,1)
        end = datetime.date(2018,2,24)
        rangeDate(begin,end)     
    """
    list = []
    d=begin
    delta = datetime.timedelta(days=1)
    while d<=end:
        list.append(d.strftime("%Y-%m-%d"))
        d += delta
    return list    



def nDaysAgo(date,n):
    """求x天前日期， 1个date类型参数,一个int数值 x 
        begin = datetime.date(2018,2,1)    /  datetime.datetime.now()
        nDaysAgo(begin,2)     
    """    
    dayAgo = date - datetime.timedelta(days = n)
    return dayAgo


def nextMonth(begin):
    """
        传当月1号，计算出下个月1号 begin = datetime.date(2017,2,1)  
    """
    next=begin + datetime.timedelta(days=monthrange(begin.year,begin.month)[1])
    return next


def minusDay(begin,n):
    """
     减去n天  begin = datetime.date(2017,2,1)   n=1 
    """
    return begin + datetime.timedelta(days=-n)

def lastDay(begin):
    """
     取当月最后一天 begin = datetime.date(2017,2,1)   
    """
    monthRange = monthrange(begin.year, begin.month)
    return datetime.date(year=begin.year, month=begin.month, day=monthRange[1])

def getMonthFirstDayAndLastDay(year=None, month=None):
    """
    :param year: 年份，默认是本年，可传int或str类型
    :param month: 月份，默认是本月，可传int或str类型
    :return: firstDay: 当月的第一天，datetime.date类型
              lastDay: 当月的最后一天，datetime.date类型
    """
    if year:
        year = int(year)
    else:
        year = datetime.date.today().year

    if month:
        month = int(month)
    else:
        month = datetime.date.today().month

    # 获取当月第一天的星期和当月的总天数
    firstDayWeekDay, monthRange = calendar.monthrange(year, month)

    # 获取当月的第一天
    firstDay = datetime.date(year=year, month=month, day=1)
    lastDay = datetime.date(year=year, month=month, day=monthRange)

    return firstDay, lastDay


'''

dt = datetime.now()  
print   '时间：(%Y-%m-%d %H:%M:%S %f): ' , dt.strftime( '%Y-%m-%d %H:%M:%S %f' )  
print   '时间：(%Y-%m-%d %H:%M:%S %p): ' , dt.strftime( '%y-%m-%d %I:%M:%S %p' )  
print   '星期缩写%%a: %s '  % dt.strftime( '%a' )  
print   '星期全拼%%A: %s '  % dt.strftime( '%A' )  
print   '月份缩写%%b: %s '  % dt.strftime( '%b' )  
print   '月份全批%%B: %s '  % dt.strftime( '%B' )  
print   '日期时间%%c: %s '  % dt.strftime( '%c' )  
print   '今天是这周的第%s天 '  % dt.strftime( '%w' )  
print   '今天是今年的第%s天 '  % dt.strftime( '%j' )  
print   '今周是今年的第%s周 '  % dt.strftime( '%U' ) 
print   '今天是当月的第%s天 '  % dt.strftime( '%d' )

输出如下：
--------------------------------------------------------------
时间：(%Y-%m-%d %H:%M:%S %f):  2015-03-08 23:30:42 181000
时间：(%Y-%m-%d %H:%M:%S %p):  15-03-08 11:30:42 PM
星期缩写%a: Sun 
星期全拼%A: Sunday 
月份缩写%b: Mar 
月份全批%B: March 
日期时间%c: 03/08/15 23:30:42 
今天是这周的第0天 
今天是今年的第067天 
今周是今年的第10周 
今天是当月的第08天 
---------------------------------------------------
'''
