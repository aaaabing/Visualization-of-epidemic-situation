import pymysql
import requests,re
import xlwt

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

for i in range(len(data)):
    province = data[i]['provinceName']#省份名称
    city_list = data[i]['cities']
    print(province)
    urrentConfirmedCount = data[i]['currentConfirmedCount']#现存确诊
    print(urrentConfirmedCount)
    confirmedCount = data[i]['confirmedCount']#累计确诊
    curedCount = data[i]['curedCount']#治愈
    deadCount = data[i]['deadCount']#死亡
    worksheet = workbook.add_sheet(province)  # 给sheet命名  #每个省份放入一个sheet
    worksheet.write(0, 0, '数据类型/省份名称')
    worksheet.write(0, 1, '现存确诊')
    worksheet.write(0, 2, '累计确诊')
    worksheet.write(0, 3, '治愈')
    worksheet.write(0, 4, '死亡')
    for j in range(len(city_list)):
        cityName = city_list[j]['cityName']  # 城市名
        currentConfirmedCount = city_list[j]['currentConfirmedCount']  # 现存确诊
        confirmedCount = city_list[j]['confirmedCount']  # 累计确诊
        curedCount = city_list[j]['curedCount']  # 治愈
        deadCount = city_list[j]['deadCount']  # 死亡
        worksheet.write(j + 1, 0, cityName)
        worksheet.write(j+1, 1, urrentConfirmedCount)
        worksheet.write(j+1, 2, confirmedCount)
        worksheet.write(j+1, 3, curedCount)
        worksheet.write(j+1, 4, deadCount)
    workbook.save('city_data.xls')  # 保存文件 并命名

#获得当天时间
import datetime
a =str(datetime.datetime.now())
a = a[0:10]
a = a.replace("-","")

conn = pymysql.connect("localhost","root","root","Chinanov")
#四个参数分别为主机名，用户名，密码，数据库名称
#根据需要修改即可
cur = conn.cursor();# 使用cursor()方法创建一个游标对象cursor
# 1). ************************创建数据表**********************************
try:
    create_sqli = "create table citynovcond (cityName varchar(13) PRIMARY KEY," \
                  "Now int(255)," \
                  "Total int(255),curr int(255),death int(255));"

    cur.execute(create_sqli)
except Exception as e:#表已存在
    print("创建数据表失败:", e)
else:
    print("创建数据表成功;")


for i in range(len(data)):
    province = data[i]['provinceName']#省份名称
    city_list = data[i]['cities']
    for j in range(len(city_list)):
        cityName = city_list[j]['cityName']  # 城市名
        currentConfirmedCount = int(city_list[j]['currentConfirmedCount'])  # 现存确诊
        confirmedCount = int(city_list[j]['confirmedCount'])  # 累计确诊
        curedCount = int(city_list[j]['curedCount'])  # 治愈
        deadCount = int(city_list[j]['deadCount'])  # 死亡
        try:
            insert_sqli = "insert into  citynovcond(day,Province,CityName,Now,Total,curr,death)" \
                          "values({0},'{1}','{2}',{3},{4},{5},{6})".format(
                a,province,cityName, currentConfirmedCount, confirmedCount, curedCount, deadCount
            )
            

            cur.execute(insert_sqli)
        except Exception as e:
            print("插入数据失败:", e)
        else:
            # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
            conn.commit()
            print("插入数据成功;")

