import random
import time
list1=['赵','钱','孙','李','周','吴','郑','王','冯','陈','褚','卫','蒋','沈','韩','杨']
list2=['男','女']
list3=['1','3','6']
A=random.choice(list1)#姓名
print('姓名:',A)
B=random.randint(20,105)#年龄
print('年龄：',B)
C=random.choice(list2)#性别
print('性别',C)
D=random.randint(0,4)#学历
dict1={0:'初中',1:'高中',2:'本科',3:'博士',4:'硕士'}
print('学历:',dict1.get(D))
E=str(random.choice(list3))#部门
dict2={1:'财务部',3:'销售部',6:'1'}
print('部门:',dict2.get(int(E)))
def regiun():
    '''生成身份证前六位'''
    #列表里面的都是一些地区的前六位号码
    first_list = ['362402','362421','362422','362423','362424','362425','362426','362427','362428','362429','362430','362432','110100','110101','110102','110103','110104','110105','110106','110107','110108','110109','110111']
    first = random.choice(first_list)
    return first

def year():
    '''生成年份'''
    now = time.strftime('%Y')
    #1948为第一代身份证执行年份,now-18直接过滤掉小于18岁出生的年份
    second = random.randint(1948,int(now)-18)
    age = int(now) - second
    # print('随机生成的身份证人员年龄为：'+str(age))
    return second


def month():
    '''生成月份'''
    three = random.randint(1,12)
    #月份小于10以下，前面加上0填充
    if three < 10:
        three = '0' + str(three)
        return three
    else:
        return three


def day():
    '''生成日期'''
    four = random.randint(1,31)
    #日期小于10以下，前面加上0填充
    if four < 10:
        four = '0' + str(four)
        return four
    else:
        return four


def randoms():
    '''生成身份证后四位'''
    #后面序号低于相应位数，前面加上0填充
    five = random.randint(1,9999)
    if five < 10:
        five = '000' + str(five)
        return five
    elif 10 < five < 100:
        five = '00' + str(five)
        return five
    elif 100 < five < 1000:
        five = '0' + str(five)
        return five
    else:
        return five


def main():
    first = regiun()
    second = year()
    three = month()
    four = day()
    last = randoms()
    IDcard = str(first)+str(second)+str(three)+str(four)+str(last)
    # print('随机生成的身份证号码为：'+IDcard)
    return IDcard


if __name__ == '__main__':
    main()
F=str(regiun())+str(random.randint(0,100))#座机号码
print(F)
G=str(regiun())+str(randoms())
print(G)
H=main()#身份证
print('身份证:',H)
I=random.choice(list1)#添加入
print('添加入:',I)
J=str(regiun())+str(randoms())#账号
print('账号:',J)
K=str(regiun())+str(randoms())#密码
print('密码:',K)
L=random.randint(0,2)#婚姻状况
dict3={0:'已婚',1:'未婚',2:'离异'}
print('婚姻状况:',dict3.get(L))
M=str(random.randint(1,3))#角色
dict4={1:'管理员',2:'员工',3:'老板'}
print('角色:',dict4.get(int(M)))
N='1325829'+str(randoms())#电话号码
print('电话号码:',N)
O='252446'+str(randoms())+'@qq.com'#邮箱
print('邮箱:',O)
# print('年龄:',A, '性别' '学历' '部门' '座机' '工资卡号' '身份证' '添加入' '账号' '密码' '民族' '婚姻' '角色' '爱好' '手机' '地址' 'E_mail')
