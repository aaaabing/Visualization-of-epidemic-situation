#构建倒排表
import xlrd
#读取国家excel
#提取其中文字信息，存入txt文本文档
rb = xlrd.open_workbook(r'National_data.xls', formatting_info=True)
# excel文件被打开为一个Book对象，即 rb（xlrd.book.Book类)
sheets = rb.sheet_names()
# 获取Book对象的属性：包含所有sheet表名的列表（xlrd.book.Book.sheet_names)
sheet1 = rb.sheet_by_index(0)
print(sheet1.name, sheet1.nrows, sheet1.ncols)
# sheet1的名称、行数、列数

list1 = sheet1.row_values(0)
list2 = sheet1.col_values(0)

#读取省份信息excel
rb2 = xlrd.open_workbook(r"Province_data.xls",formatting_info=True)
sheets2 = rb2.sheet_names()
sheet21 = rb2.sheet_by_index(0)
print(sheet21.name, sheet21.nrows, sheet21.ncols)
list3 = sheet21.row_values(0)
list4 = sheet21.col_values(0)
#读取城市信息excel
rb3 = xlrd.open_workbook(r"city_data.xls",formatting_info=True)
sheets3 = rb3.sheet_names()
lens = len(sheets3)
listsum = []
for i in range(lens):
    sheets31 = rb3.sheet_by_index(i)
    list5 = sheets31.row_values(0)
    list6 = sheets31.col_values(0)
    print(list6)
    listsum = listsum+list5+list6


listsum = listsum+list1+list2+list3+list4
listsum = set(listsum)
listsum = list(listsum)
print(sheet1.row_values(0), sheet1.col_values(0))
file=open('inverted_list.txt','w')
for i in listsum:
    file.write(i+"\n")