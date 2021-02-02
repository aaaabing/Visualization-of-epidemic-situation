import requests,re
import xlwt
import pymysql

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

response = requests.get(url)
response.encoding='utf-8'
pattern = r'window.getAreaStat = ([\s\S]*?)</script>'
data_list = re.findall(pattern, response.text)
#print(data_list)
data = eval(data_list[0].replace('}catch(e){}',''))

print(data)
china_list = []
workbook = xlwt.Workbook(encoding='ascii')
worksheet = workbook.add_sheet("Province data")  # 给sheet命名
worksheet.write(0, 0, '数据类型/省份名称')
worksheet.write(0, 1, '现存确诊')
worksheet.write(0, 2, '累计确诊')
worksheet.write(0, 3, '治愈')
worksheet.write(0, 4, '死亡')
for i in range(len(data)):
    province = data[i]['provinceName']#省份名称
    print(province)
    urrentConfirmedCount = data[i]['currentConfirmedCount']#现存确诊
    print(urrentConfirmedCount)
    confirmedCount = data[i]['confirmedCount']#累计确诊
    curedCount = data[i]['curedCount']#治愈
    deadCount = data[i]['deadCount']#死亡
    worksheet.write(i+1, 0, province)

    worksheet.write(i+1, 1, urrentConfirmedCount)
    worksheet.write(i+1, 2, confirmedCount)
    worksheet.write(i+1, 3, curedCount)
    worksheet.write(i+1, 4, deadCount)

    workbook.save('Province_data.xls')  # 保存文件 并命名

    # 'curedCount'
    # 'deadCount'
import datetime
a =str(datetime.datetime.now())
a = a[0:10]
a = a.replace("-","")
print(a)
print(type(a))

conn = pymysql.connect("localhost","root","root","chinanov")
#四个参数分别为主机名，用户名，密码，数据库名称
#根据需要修改即可
cur = conn.cursor();# 使用cursor()方法创建一个游标对象cursor
# 1). ************************创建数据表**********************************
try:
    create_sqli = "create table provincenovcond (id int(11) PRIMARY KEY," \
                  "Province varchar(255),Now int(255)," \
                  "Total int(255),curr int(255),death int(255));"

    cur.execute(create_sqli)
except Exception as e:#表已存在
    print("创建数据表失败:", e)
else:
    print("创建数据表成功;")

for i in range(len(data)):
    province = data[i]['provinceName']#省份名称
    urrentConfirmedCount = int(data[i]['currentConfirmedCount'])#现存确诊
    confirmedCount = int(data[i]['confirmedCount'])#累计确诊
    curedCount = int(data[i]['curedCount'])#治愈
    deadCount = int(data[i]['deadCount'])#死亡
    try:
        insert_sqli = "insert into  provincenovcond (province,Now,Total,curr,death,day)" \
                      "values('{0}',{1},{2},{3},{4},{5})".format(
          province,urrentConfirmedCount,confirmedCount,curedCount,deadCount,a
        )

        cur.execute(insert_sqli)
    except Exception as e:
        print("插入数据失败:", e)
    else:
        # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
        conn.commit()
        print("插入数据成功;")


