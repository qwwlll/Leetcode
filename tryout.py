import calendar
try:
    yy=int(input('请输入年份:'))
    mm=int(input('请输入月份:'))
    L=['零','一','二','三','四','五','六','天']
    if mm<=12 and mm>0:
        # 得到返回的元组，第一个元素是所查月份的第一天对应的是星期几（0-6），并转换为字符串去遍历
        for i in str(calendar.monthrange(yy+1,mm)[0]):
            # 使用eval()函数用来执行字符串表达式，返回应是周几的整数
            b = eval(i)
            # 得到应是周几的索引后 在L列表中查找对应的中文字符--->L[b]
            # 使用mdays()函数得到输入月份的天数
            print('{}年{}月的第一天是周{}，{}月共有{}天'.format(yy,mm,L[b],mm,calendar.mdays[mm]))
    else:
        print('请输入正确的月份')
except ValueError:
    print('请输入数字')
 