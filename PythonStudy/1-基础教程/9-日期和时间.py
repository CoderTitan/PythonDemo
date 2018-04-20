
# 日期和时间
import time

'''
# 当前时间戳
ticks = time.time()
print(ticks)
# 本地时间
localTime = time.localtime()
print(localTime)
# 格式化时间
print(time.asctime(localTime))


# 1.格式化日期
# 格式化成 2018-04-18 19:49:44 形式
newDate1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(newDate1)
# 格式化成 Wed Apr 18 19:50:53 2018 形式
newDate2 = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
print(newDate2)
# 将时间字符串转化为时间戳
timeNum = time.mktime(time.strptime(newDate2, "%a %b %d %H:%M:%S %Y"))
print(timeNum)


# 2. Time模块介绍
# 回格林威治西部的夏令时地区的偏移秒数
print(time.altzone)

# 把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。 如果参数未给或者为None的时候，将会默认time.time()为参数
print(time.ctime())
print(time.ctime(time.time() - 100))

# 将一个时间戳转换为UTC时区（0时区）的struct_time
print(time.gmtime())
print(time.gmtime(time.time() - 100))

# 类似gmtime()，作用是格式化时间戳为本地的时间
print(time.localtime())
print(time.localtime(time.time() - 100))

# 回用秒数来表示时间的浮点数
t = (2018, 4, 19, 10, 10, 20, 2, 34, 0)
print(time.mktime(t))
print(time.mktime(time.localtime()))

# 推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间
# print(time.ctime())
# time.sleep(3)
# print(time.ctime())

# 根据指定的格式把一个时间字符串解析为时间元组
structTime= time.strptime('20 Nov 2018', '%d %b %Y')
print(structTime)

# Time模块属性
print(time.timezone)
print(time.tzname)
'''



# Calendar模块
import calendar

'''
year18 = calendar.calendar(2018)
# print(year18)

# 返回当前每周起始日期的设置, 默认情况下，首次载入caendar模块时返回0，即星期一
print(calendar.firstweekday())
# 是闰年返回True，否则为false
print(calendar.isleap(2016))
# 返回在Y1，Y2两年之间的闰年总数
print(calendar.leapdays(2015, 2021))
# 返回一个元组, 第一个元素是该月的第一天是星期几(0-6, 0是星期一), 第二个元素是该月有几天
print(calendar.monthrange(2018, 4))
# 返回给定日期是星期几(0-6, 0是星期一)
# calendar.weekday(year,month,day)
print(calendar.weekday(2018, 4, 19))

# 设置每周的起始日期
# calendar.setfirstweekday(weekday) 无返回值
calendar.setfirstweekday(3)
print(calendar.firstweekday())

'''

monthTime = calendar.month(2018, 4)
# print(monthTime)
# print(calendar.prcal(2018))
# print(calendar.prmonth(2018, 4))
print(calendar.timegm(time.localtime()))




