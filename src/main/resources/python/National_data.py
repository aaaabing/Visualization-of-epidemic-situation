import requests,re
import xlwt
import pymysql

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

response = requests.get(url)
response.encoding='utf-8'
pattern = r'window.getStatisticsService = {(.*?)}'
data_list = re.findall(pattern, response.text)
print(data_list)
#具体的包含全国疫情数据的信息
form = r'currentConfirmedCount"(.*?)":"'
data = re.findall(form,data_list[0])
print(data)
#存储全国疫情数据的列表
list_count = []
#存储全国疫情数据较昨日新增数的列表
list_incr = []
#储存疫情信息类型
list_name = ['现存确诊数' ,'累计确诊数','境外输入','累计治愈','累计死亡','现存无症状']
form1 = r':(.*?),'
currentConfirmedCount = re.findall(form1,data[0])[0]
print("现存确诊数：" + currentConfirmedCount)
list_count.append(currentConfirmedCount)
form11 = r'"currentConfirmedIncr":(.*?),'

currentConfirmedIncr = re.findall(form11,data[0])[0]
print("较昨日:" + currentConfirmedIncr + "\n")
list_incr.append(currentConfirmedIncr)

form2 = r'"confirmedCount":(.*?),'
confirmedCount = re.findall(form2,data[0])[0]
print("累计确诊数："+confirmedCount)
list_count.append(confirmedCount)
form22 = r'"confirmedIncr":(.*?),'
confirmedIncr = re.findall(form22,data[0])[0]
print("较昨日:" + confirmedIncr + "\n")
list_incr.append(confirmedIncr)

form3 = r'"suspectedCount":(.*?),'
suspectedCount = re.findall(form3,data[0])[0]
print("境外输入：" + suspectedCount)
list_count.append(suspectedCount)
form33 = r'"suspectedIncr":(.*?),'
suspectedIncr = re.findall(form33,data[0])[0]
print("较昨日:" + suspectedIncr + "\n")
list_incr.append(suspectedIncr)

form4 = r'"curedCount":(.*?),'
curedCount = re.findall(form4,data[0])[0]
print("累计治愈："+curedCount)
list_count.append(curedCount)
form44 = r'"curedIncr":(.*?),'
curedIncr = re.findall(form44,data[0])[0]
print("较昨日:" + curedIncr + "\n")
list_incr.append(curedIncr)

form5 = r'"deadCount":(.*?),'
deadCount = re.findall(form5,data[0])[0]
print("累计死亡：" + deadCount)
list_count.append(deadCount)
form55 = r'"deadIncr":(.*?),'
deadIncr = re.findall(form55,data[0])[0]
print("较昨日:" + deadIncr + "\n")
list_incr.append(deadIncr)

form6 = r'"seriousCount":(.*?),'
seriousCount = re.findall(form6,data[0])[0]
print("现存无症状："+seriousCount)
list_count.append(seriousCount)
form66 = r'"seriousIncr":(.*?),'
seriousIncr = re.findall(form66,data[0])[0]
print("较昨日:" + seriousIncr + "\n")
list_incr.append(seriousIncr)




#将数据存入excel表格
#data_all=pandas.DataFrame

workbook = xlwt.Workbook(encoding = 'ascii')
worksheet = workbook.add_sheet("National data")#给sheet命名
worksheet.write(1, 0, '总数')
worksheet.write(2, 0, '较昨日变化值')
for i in range(1,7):
    worksheet.write(0, i, list_name[i-1])
    worksheet.write(1, i, list_count[i-1])
    worksheet.write(2, i, list_incr[i-1] )

workbook.save('National_data.xls') # 保存文件 并命名


for i in range(len(list_count)):
    list_count[i] = int(list_count[i])
    list_incr[i] = int(list_incr[i])
print(list_name)

print(list_count)
print(list_incr)
#获得当天时间
import datetime
a =str(datetime.datetime.now())
a = a[0:10]
a = a.replace("-","")
print(a)
print(type(a))


conn = pymysql.connect("localhost","root","root","Chinanov")
#四个参数分别为主机名，用户名，密码，数据库名称
#根据需要修改即可
cur = conn.cursor();# 使用cursor()方法创建一个游标对象cursor
# 1). ************************创建数据表**********************************
try:
    create_sqli = "create table chinanovcond (day varchar(20) PRIMARY KEY, Total int(255), NowTotal int(255), Importfromabroad int(255), CumulativeCure int(255), CumulativeDeath int(255),Existingasymptomatic int(255)," \
                  "yeTotal int(255), yeNowTotal int(255), yeImportfromabroad int(255), yeCumulativeCure int(255), yeCumulativeDeath int(255), yeExistingasymptomatic int(255));"
    cur.execute(create_sqli)
except Exception as e:#表已存在
    print("创建数据表失败:", e)
else:
    print("创建数据表成功;")



try:
    insert_sqli = "insert into chinanovcond " \
                  "values('{0}','{1}','{2}',{3},{4},{5},{6},{7},{8},{9},{10},{11},{12})".format(
        a,list_count[1],list_count[0],list_count[2],list_count[3],list_count[4],list_count[5],
        list_incr[1], list_incr[0], list_incr[2], list_incr[3], list_incr[4], list_incr[5]
    )


    cur.execute(insert_sqli)
except Exception as e:
    print("插入数据失败:", e)
else:
    # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
    conn.commit()
    print("插入数据成功;")
